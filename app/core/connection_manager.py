#handle the pull for websockets

from typing import Dict, Optional, List
from fastapi import WebSocket, WebSocketDisconnect
import json
from datetime import datetime


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Dict[str, WebSocket]]
        """
        Structure is something like that:
        {
            room_id: {
                player_id: Websocket_connection_object
            }
        }
        """
    
    async def connect(self, room_id: str, player_id: str, websocket: WebSocket):
        await websocket.accept()
        pass


    async def disconnect(self, room_id: str, player_id:str, websocket: WebSocket):
        pass


    async def disconnect_expired_sessions(self):
        pass

    
    