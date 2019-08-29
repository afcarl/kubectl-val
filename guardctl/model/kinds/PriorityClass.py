from poodle import Object
from guardctl.model.system.primitives import Type, String


class PriorityClass(Object):
    metadata_name: String

    priority: int
    preemptionPolicy: Type

    @property
    def value(self):
        pass
    @value.setter 
    def value(self, value):
        if value > 1000: value = 1000
        self.priority = value

