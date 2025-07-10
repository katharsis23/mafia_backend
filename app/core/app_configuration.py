#file which represents the settings of the Fastapi app instance. In advance i shall use it for main.py to launch the server

from sqlalchemy.exc import SQLAlchemyError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..database import ENGINE
from sqlalchemy.orm import declarative_base
Base_decl=declarative_base()

ORIGINS=["http://localhost:3000"] 
# DO NOT USE IN PRODUCTION!!! ONLY FOR LOCAL DEVELOPING


class App_Configuration:
    def __init__(self):
        self.app_core=FastAPI(
            title="Mafia-backend",
            version="0.1.0"
        )

        cors_middleware=self.app_core.add_middleware(
           CORSMiddleware,
            allow_origins=ORIGINS,
            allow_methods=["PUT", "GET", "POST", "DELETE"],
            allow_credentials=True,
            allow_headers=["*"]
        )

        self._register_events()
        self._regiter_routes()

    def _register_events(self):
        @self.app_core.on_event("startup")
        async def startup():
            try:
                async with ENGINE.begin() as connection:
                    await connection.run_sync(Base_decl.metadata.create_all)
            except SQLAlchemyError as database_error:
                print(f"Failed to create tables: {database_error}")


    def _regiter_routes(self):
        #self.app_core.include_router()
        pass

    @property
    def get_app(self)->FastAPI:
        return self.app_core