from typing import List, Type, Dict, Set
from .entity import Entity
from .component import Component
from .system import System

class ComponentNotRegistered(Exception):
    def __init__(self, component_type: Type[Component]) -> None:
        super().__init__(f"Component {component_type} is not registered.")

class World:
    def __init__(self) -> None:
        self.__entities: List[Entity] = []
        self.__component_map: Dict[Type[Component], int] = {}
        self.__systems: Dict[int, List[System]] = {}
        
    def create_entity(self) -> int:
        id = len(self.__entities)
        self.__entities.append(Entity())
        
        for _ in self.__component_map:
            self.__entities[id].push_empty_component()
        
        return id
    
    def bind_system(self, system: System, event_id: int) -> None:
        if self.__systems.get(event_id) == None:
            self.__systems[event_id] = []
            
        self.__systems[event_id].append(system)
    
    def add_component(self, entity_id: int, component: Component) -> None:
        if not component.__class__ in self.__component_map.keys():
            self.register_component(component.__class__)
            
            for entity in self.__entities:
                entity.push_empty_component()
                
        self.__entities[entity_id].add_component(component, self.get_component_id(component.__class__))
        
    def register_component(self, component_type: Type[Component]) -> int:
        id = len(self.__component_map)
        self.__component_map[component_type] = id
            
        for entity in self.__entities:
            entity.push_empty_component()
        
        return id
        
    def get_component_id(self, component_type: Type[Component]) -> int:
        if not component_type in self.__component_map.keys():
            raise ComponentNotRegistered(component_type)
        
        return self.__component_map[component_type]
    
    def notify_systems(self, event_id: int) -> None:
        if self.__systems.get(event_id) == None:
            return
        
        for system in self.__systems[event_id]:
            system.on_trigger(self.__entities)
