from typing import Tuple

from pygame import Surface, display

from ..ecs import World
from .util import (AnimatedComponent, AnimateSystem, RenderableComponent,
                   RenderSystem)


class Scene(World):
    NEXT_FRAME_EVENT = 0
    
    def __init__(self, resolution: Tuple[int, int]) -> None:
        super().__init__()
        self.__surface = Surface(resolution)
        self.register_component(RenderableComponent)
        self.register_component(AnimatedComponent)
        self.bind_system(RenderSystem(self.__surface), self.NEXT_FRAME_EVENT)
        self.bind_system(AnimateSystem(self.__surface), self.NEXT_FRAME_EVENT)
    
    def render(self) -> None:
        self.__surface.fill("black")
        self.notify_systems(self.NEXT_FRAME_EVENT)
        display.get_surface().blit(self.__surface, (0, 0))
        display.update(self.__surface.get_rect())
    