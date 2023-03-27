from typing import Tuple, List
from pygame import Surface, Rect
from ..ecs import Component, System, ComponentFilter, Entity

class RenderableComponent(Component):   
    def __init__(self, image: Surface, position: Tuple[int, int]) -> None:
        self.image = image
        self.rect = Rect(image.get_size(), position)
        
class AnimatedComponent(RenderableComponent):
    def __init__(self, frames: List[Surface], position: Tuple[int, int]) -> None:
        self.frames = frames
        self.current_frame = 0
        super().__init__(self.frames[self.current_frame], position)
        
class AnimateSystem(System):
    def __init__(self, surface: Surface) -> None:
        self.__filter = ComponentFilter([AnimatedComponent])
        self.__surface = surface
        
    def on_trigger(self, entities: List[Entity]) -> None:
        for entity in self.__filter.filter(entities):
            component = entity.get_component(AnimatedComponent)
            component.current_frame += 1
            component.current_frame %= len(component.frames)
            component.image = component.frames[component.current_frame]
            self.__surface.blit(component.image, component.rect)
            
class RenderSystem(System):
    def __init__(self, surface: Surface) -> None:
        self.__filter = ComponentFilter([RenderableComponent])
        self.__surface = surface
        
    def on_trigger(self, entities: List[Entity]) -> None:
        for entity in self.__filter.filter(entities):
            component = entity.get_component(RenderableComponent)
            self.__surface.blit(component.image, component.rect)