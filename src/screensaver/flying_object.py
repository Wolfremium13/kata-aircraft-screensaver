from abc import ABC, abstractmethod

from src.screensaver.position import Position


class FlyingObject(ABC):
    @abstractmethod
    def current_position(self) -> Position:
        pass

    @abstractmethod
    def is_colliding_with(self, flying_object) -> bool:
        pass
