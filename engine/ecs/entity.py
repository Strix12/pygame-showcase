from typing import List, Set, Type, TypeVar
from .component import Component

T = TypeVar("T")

class ComponentIdInvalid(Exception):
    def __init__(self, id: int) -> None:
        super().__init__(f"Component of id {id} does not exist in entity.")
        
class ComponentDoesNotExist(Exception):
    def __init__(self, component_type: Type[Component]) -> None:
        super().__init__(f"Component of type {component_type} does not exist in entity.")

class Entity:
    def __init__(self):
        self.__components: List[Component | None] = []
        self.__components_set: Set[Type[Component]] = set()
        
    def push_empty_component(self) -> None:
        self.__components.append(None)
        
    def add_component(self, component: Component, id: int) -> None:
        try:
            self.__components[id] = component
            self.__components_set.add(component.__class__)
        except:
            raise ComponentIdInvalid(id)
        
    def get_component(self, component_type: Type[T]) -> T:
        if not self.has_component(component_type):
            raise ComponentDoesNotExist(component_type)
        
        return next(component for component in self.__components if isinstance(component, component_type))
        
    def has_component(self, component_type: Type[Component]) -> bool:
        return component_type in self.__components_set
        