from abc import  ABC, abstractmethod
from typing import Dict, Any




class BaseRole(ABC):
    def __init__(self, player_info):
        self.player_info=player_info
    

    @abstractmethod
    def vote(self, target_player):
        pass

    @abstractmethod
    def on_night_event(self):
        pass

    @abstractmethod
    def write_in_chat(self, message):
        pass

    @abstractmethod
    def get_role_info(self, message):
        pass
    

    