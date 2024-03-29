from poodle import Object
from guardctl.model.system.primitives import TypePolicy
from guardctl.misc.const import *


class PriorityClass(Object):
    metadata_name: str

    priority: int
    preemptionPolicy: TypePolicy

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.preemptionPolicy = POLICY["PreemptLowerPriority"]
        self.priority = 0

    @property
    def value(self):
        pass
    @value.setter 
    def value(self, value):
        if value > 1000: value = 1000
        self.priority = value


zeroPriorityClass = PriorityClass("ZERO")
zeroPriorityClass.metadata_name = "Normal-zero"
