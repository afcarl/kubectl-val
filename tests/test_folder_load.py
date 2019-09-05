import pytest
from guardctl.model.kubernetes import KubernetesCluster
from guardctl.model.kinds.Pod import Pod
from guardctl.model.kinds.Service import Service
from guardctl.model.kinds.Node import Node
from guardctl.model.kinds.DaemonSet import DaemonSet
from guardctl.misc.object_factory import labelFactory
from guardctl.misc.const import *

import logzero
logzero.logfile("./test.log", disableStderrLogger=True)

TEST_PODS = "./tests/kube-config/pods.yaml"
TEST_NODES = "./tests/kube-config/nodes.yaml"
TEST_DEPLOYMENTS = "./tests/kube-config/deployments.yaml"

TEST_CLUSTER_FOLDER = "./tests/daemonset_eviction/cluster_dump"
TEST_DAEMONET = "./tests/daemonset_eviction/daemonset_create.yaml"

def test_load_pods():
    k = KubernetesCluster()
    k.load(open(TEST_PODS).read())
    k._build_state()
    assert k.state_objects

def test_load_nodes():
    k = KubernetesCluster()
    k.load(open(TEST_NODES).read())
    k._build_state()
    assert k.state_objects

def test_load_deployments():
    k = KubernetesCluster()
    k.load(open(TEST_NODES).read())
    k.load(open(TEST_PODS).read())
    k.load(open(TEST_DEPLOYMENTS).read())
    k._build_state()
    assert k.state_objects

# @pytest.mark.filterwarnings("ignore:*")
def test_load_pods_new():
    k = KubernetesCluster()
    k.load(open(TEST_PODS).read())
    k._build_state()
    # TODO: check if pod is fully loaded
    pod = k.state_objects[2]
    assert isinstance(pod, Pod)
    assert len(pod.metadata_labels._get_value()) > 0
    assert pod.status_phase == STATUS_POD_RUNNING

    assert k.state_objects

def test_load_folder():
    k = KubernetesCluster()
    k.load_dir(TEST_CLUSTER_FOLDER)
    k._build_state()
    # check that no pods are orphan
    pods = list(filter(lambda x: isinstance(x, Pod), k.state_objects))
    assert pods
    for pod in pods:
        assert pod.atNode._property_value != Node.NODE_NULL

def test_load_folder_create_labels():
    k = KubernetesCluster()
    # k.load_dir(TEST_CLUSTER_FOLDER)
    k.create_resource(open(TEST_DAEMONET).read())
    k._build_state()
    for ds in filter(lambda x: isinstance(x, DaemonSet), k.state_objects):
        if labelFactory.get("k8s-app", "fluentd-logging") in ds.metadata_labels._get_value():
            return
    raise Exception("Can not check labels load")

def test_load_folder_load_pod_labels():
    k = KubernetesCluster()
    k.load_dir(TEST_CLUSTER_FOLDER)
    k._build_state()
    for ds in filter(lambda x: isinstance(x, Pod), k.state_objects):
        if labelFactory.get("app", "redis-evict") in ds.metadata_labels._get_value():
            return
    raise Exception("Can not check labels load")

def test_spec_selector_labels():
    k = KubernetesCluster()
    k.load_dir(TEST_CLUSTER_FOLDER)
    k._build_state()
    for ds in filter(lambda x: isinstance(x, Service), k.state_objects):
        if labelFactory.get("app", "redis-evict") in ds.spec_selector._get_value():
            return
    raise Exception("Can not check labels load")

def test_load_nodes_properties():
    pass
