from dataclasses import dataclass
from engine.ecs import Component
from typing import Tuple

@dataclass
class Velocity:
    x: int
    y: int
    
@dataclass
class MovementComponent(Component):
    velocity = Velocity(0, 0)
    max_speed: Tuple[int, int]
    
@dataclass
class PlayerComponent(Component):
    pass