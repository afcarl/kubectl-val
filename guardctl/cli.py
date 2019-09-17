import click
import os
from guardctl.model.kubernetes import KubernetesCluster
from guardctl.model.search import AnyServiceInterrupted 
from guardctl.model.scenario import Scenario
# from yaspin import yaspin
# from yaspin.spinners import Spinners
from sys import stdout
from guardctl.model.search import EXCLUDED_SERV, mark_excluded_service
from guardctl.model.system.primitives import TypeServ

# @click.group()
# def cli():
#     pass

# @click.command()
@click.group(invoke_without_command=True)
@click.option("--from-dir", "-d", help="Directory with cluster resources definitions", \
                type=str, required=True)
@click.option("--output", "-o", help="Select output format", \
                type=click.Choice(["json", "yaml", "wide"]), required=False, default="wide")
@click.option("--filename", "-f", help="Create new resource from YAML file", \
                type=str, required=False, multiple=True)
@click.option("--timeout", "-t", help="Set AI planner timeout in seconds", \
                type=int, required=False, default=150)
@click.option("--exclude", "-e", help="-e <Kind1>:<name1>,<Kind2>:<name2>,...", \
                required=False, default=None)
def run(from_dir, output, filename, timeout, exclude):

    k = KubernetesCluster()

    click.echo(f"# Loading cluster definitions from {from_dir} ...")
    k.load_dir(from_dir)

    for f in filename:
        click.echo(f"# Creating resource from {f} ...")
        k.create_resource(open(f).read())

    click.echo(f"# Building abstract state ...")
    k._build_state()
    excludeDict = {}
    if exclude != None:
         excludeDict = {}
         for kn in exclude.split(","):
             kinda = kn.split(":")[0]
             name = kn.split(":")[1]
             excludeDict[name] = TypeServ(name)
    mark_excluded_service(k.state_objects, excludeDict)
    p = AnyServiceInterrupted(k.state_objects)
    # p.select_target_service()

    click.echo("# Solving ...")

    if stdout.isatty():
        # with yaspin(Spinners.earth, text="") as sp:
            p.run(timeout=timeout, sessionName="cli_run")
            if not p.plan:
                # sp.ok("✅ ")
                click.echo("# No scenario was found.")
            else:
                # sp.fail("💥 ")
                click.echo("# Scenario found.")
                click.echo(Scenario(p.plan).asyaml())
    else:
        p.run(timeout=timeout, sessionName="cli_run")
        click.echo(Scenario(p.plan).asyaml())

@click.command()
@click.option("-f", help="Create new resource from YAML file", type=str, required=False, multiple=True)
def fetch(f):
    c = KubernetesCluster()

    click.echo("Fetching cluster state ...")

    c.fetch_state_default()

    scenario = c.run()

    if scenario: click.echo(scenario.yaml())
    else: click.echo("Cluster clean!")

# cli.add_command(test)
# cli.add_command(run)
