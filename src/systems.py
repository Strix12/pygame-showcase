from typing import List
from engine.ecs import System, ComponentFilter, Entity
from engine.display import RenderableComponent
from pygame import key, K_w, K_s, K_a, K_d
from .components import PlayerComponent, MovementComponent
from time import time

class QuitGameSystem(System):      
    def on_trigger(self, _: List[Entity]) -> None:
        exit(0)

class KeydownSystem(System):
    def __init__(self) -> None:
        self.__player_filter = ComponentFilter([PlayerComponent, MovementComponent])
        
    def on_trigger(self, entities: List[Entity]) -> None:
        keys = key.get_pressed()
        
        for entity in self.__player_filter.filter(entities):
            player_component = entity.get_component(MovementComponent)
            
            if keys[K_w]:
                player_component.velocity.y = -player_component.max_speed[1]
            elif keys[K_s]:
                player_component.velocity.y = player_component.max_speed[1]
            else:
                player_component.velocity.y = 0
                
            if keys[K_a]:
                player_component.velocity.x = -player_component.max_speed[0]
            elif keys[K_d]:
                player_component.velocity.x = player_component.max_speed[0]
            else:
                player_component.velocity.x = 0
                
class MovementSystem(System):
    def __init__(self) -> None:
        self.__movement_filter = ComponentFilter([MovementComponent, RenderableComponent])
        self.__last_movement = time()
        
    def delta_time(self) -> float:
        return time() - self.__last_movement
        
    def on_trigger(self, entities: List[Entity]) -> None:
        delta_time = self.delta_time()
        
        for entity in self.__movement_filter.filter(entities):
            entity_velocity = entity.get_component(MovementComponent).velocity
            entity.get_component(RenderableComponent).rect.move_ip(entity_velocity.x * delta_time, entity_velocity.y * delta_time)
            
        self.__last_movement = time()