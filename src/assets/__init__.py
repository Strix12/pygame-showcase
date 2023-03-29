from pygame import image, Surface
from typing import Tuple, Dict

def load_asset(image: Surface, position: Tuple[int, int], size: Tuple[int, int] = (1, 1)) -> Surface:
    return image.subsurface((position[0] * 16, position[1] * 16, size[0] * 16, size[1] * 16))

SPRITESHEET = image.load("./assets/spritesheet.png")
TILEMAP = image.load("./assets/tilemap.png")

ASSETS: Dict[str, Surface] = {
    "EYEBALL_FRAME_0": load_asset(SPRITESHEET, (0, 0)),
    "EYEBALL_FRAME_1": load_asset(SPRITESHEET, (1, 0)),
    "EYEBALL_FRAME_2": load_asset(SPRITESHEET, (2, 0)),
    "EYEBALL_FRAME_3": load_asset(SPRITESHEET, (3, 0)),
    "BOMB_FRAME_0": load_asset(SPRITESHEET, (0, 4)),
    "BOMB_FRAME_1": load_asset(SPRITESHEET, (0, 5)),
    "BOMB_FRAME_2": load_asset(SPRITESHEET, (0, 6)),
    "BOMB_FRAME_3": load_asset(SPRITESHEET, (0, 7)),
    "BOMB_FRAME_4": load_asset(SPRITESHEET, (0, 8)),
    "BOMB_FRAME_5": load_asset(SPRITESHEET, (0, 9)),
    "BOMB_FRAME_6": load_asset(SPRITESHEET, (0, 10)),
    "BOMB_FRAME_7": load_asset(SPRITESHEET, (0, 11)),
    "BOMB_FRAME_8": load_asset(SPRITESHEET, (0, 12)),
    "BOMB_FRAME_9": load_asset(SPRITESHEET, (0, 13)),
}
