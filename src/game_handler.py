from time import sleep, time
from engine.display import RenderableComponent, Scene
from pygame import Surface, QUIT, event
from .components import MovementComponent, PlayerComponent
from .systems import MovementSystem, KeydownSystem, QuitGameSystem

class GameHandler:
    RESOLUTION = (1280, 720)
    FRAMERATE = 1 / 144

    def __init__(self) -> None:
        self.__main_scene = Scene(self.RESOLUTION)
        player_entity = self.__main_scene.create_entity()
        self.__last_render = time()
        
        player_surf = Surface((100, 100))
        player_surf.fill('purple')
        
        self.__main_scene.add_component(player_entity, RenderableComponent(player_surf, (0, 0)))
        self.__main_scene.add_component(player_entity, MovementComponent((200, 200)))
        self.__main_scene.add_component(player_entity, PlayerComponent())
        
        self.__main_scene.bind_system(MovementSystem(), self.__main_scene.NEXT_FRAME_EVENT)
        self.__main_scene.bind_system(KeydownSystem(), self.__main_scene.NEXT_FRAME_EVENT)
        self.__main_scene.bind_system(QuitGameSystem(), QUIT)

    def start_game(self) -> None:
        while True:
            delta_time = time() - self.__last_render
            
            for e in event.get():
                self.__main_scene.notify_systems(e.type)
                
            self.__main_scene.render()
            self.__last_render = time()
            
            if delta_time < self.FRAMERATE:
                sleep(self.FRAMERATE - delta_time)