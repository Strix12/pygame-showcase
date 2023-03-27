from typing import List, Type, Callable
from .component import Component
from .entity import Entity

class ComponentFilter:
    def __init__(self, component_types: List[Type[Component]]) -> None:
        self.__filter: Callable[[List[Entity]], List[Entity]] = lambda entities: [e for e in entities if all([e.has_component(component_type) for component_type in component_types])]
        
    def filter(self, entities: List[Entity]) -> List[Entity]:
        return self.__filter(entities)