from typing import List
from .entity import Entity

class System:
    def on_trigger(self, _: List[Entity]) -> None:
        pass