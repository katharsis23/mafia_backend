#defines chat behaviour
from typing import Dict


class Chat:
    def __init__(self, mode: str="day"):
        self.messages: Dict[str, str]
        """
        Structure is going to be like that:

        username: message
        """

    
    def append_new_message(self):
        pass

    @setattr
    def switch_mode(self):
        if self.mode=="day":
            self.mode="night"
        elif self.mode=="night":
            self.mode="day"
        else:
            raise ValueError("Corrupted mode of the chat")
