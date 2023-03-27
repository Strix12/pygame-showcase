from typing import List, Tuple
from dataclasses import dataclass
from time import sleep, time
from engine import ecs, display
import pygame

RESOLUTION = (1280, 720)
FRAMERATE = 1 / 240

@dataclass
class Velocity:
    x: int
    y: int
    
@dataclass
class MovementComponent(ecs.Component):
    velocity = Velocity(0, 0)
    max_speed: Tuple[int, int]
    
@dataclass
class PlayerComponent(ecs.Component):
    pass

class QuitGameSystem(ecs.System):      
    def on_trigger(self, _: List[ecs.Entity]) -> None:
        exit(0)

class KeydownSystem(ecs.System):
    def __init__(self) -> None:
        self.__player_filter = ecs.ComponentFilter([PlayerComponent, MovementComponent])
        
    def on_trigger(self, entities: List[ecs.Entity]) -> None:
        keys = pygame.key.get_pressed()
        
        for entity in self.__player_filter.filter(entities):
            player_component = entity.get_component(MovementComponent)
            
            if keys[pygame.K_w]:
                player_component.velocity.y = -player_component.max_speed[1]
            elif keys[pygame.K_s]:
                player_component.velocity.y = player_component.max_speed[1]
            else:
                player_component.velocity.y = 0
                
            if keys[pygame.K_a]:
                player_component.velocity.x = -player_component.max_speed[0]
            elif keys[pygame.K_d]:
                player_component.velocity.x = player_component.max_speed[0]
            else:
                player_component.velocity.x = 0
                
class MovementSystem(ecs.System):
    def __init__(self) -> None:
        self.__movement_filter = ecs.ComponentFilter([MovementComponent, display.RenderableComponent])
        self.__last_movement = time()
        
    def delta_time(self) -> float:
        return time() - self.__last_movement
        
    def on_trigger(self, entities: List[ecs.Entity]) -> None:
        delta_time = self.delta_time()
        
        for entity in self.__movement_filter.filter(entities):
            entity_velocity = entity.get_component(MovementComponent).velocity
            entity.get_component(display.RenderableComponent).rect.move_ip(entity_velocity.x * delta_time, entity_velocity.y * delta_time)
            
        self.__last_movement = time()
        
def main():
    main_scene = display.Scene(RESOLUTION)
    player_entity = main_scene.create_entity()
    last_render = time()
    
    player_surf = pygame.Surface((100, 100))
    player_surf.fill('purple')
    
    main_scene.add_component(player_entity, display.RenderableComponent(player_surf, (0, 0)))
    main_scene.add_component(player_entity, MovementComponent((200, 200)))
    main_scene.add_component(player_entity, PlayerComponent())
    
    main_scene.bind_system(MovementSystem(), main_scene.NEXT_FRAME_EVENT)
    main_scene.bind_system(KeydownSystem(), main_scene.NEXT_FRAME_EVENT)
    main_scene.bind_system(QuitGameSystem(), pygame.QUIT)
    
    while True:
        delta_time = time() - last_render
        
        for e in pygame.event.get():
            main_scene.notify_systems(e.type)
            
        main_scene.render()
        last_render = time()
        
        if delta_time < FRAMERATE:
            sleep(FRAMERATE - delta_time)
    
if __name__ == "__main__":
    pygame.display.set_mode(RESOLUTION, vsync=1)
    main()