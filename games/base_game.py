# gamehub/games/base_game.py

from abc import ABC, abstractmethod

class BaseGame(ABC):
    """
    Abstract base class for all games in the GameHub.
    Each game should implement the play method.
    """
    
    @abstractmethod
    def play(self):
        pass
