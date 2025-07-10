#User Model from DB
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from ..core.app_configuration import Base_decl
from ..utils.password_managing import Password_Manager



class UserManager(Base_decl):

    """
    Handles the user model from the database
    
    """
    __tablename__="users"

    id=Column(
         UUID(as_uuid=True),
         server_default="uuid_generate_v4()",
         primary_key=True,
     )

    username=Column(String(30), nullable=False)

    password_hash=Column(Text, nullable=False)

    bonus_points=Column(Integer, default=0)

    games_played=Column(Integer, default=0)

    games_won=Column(Integer, default=0)



class User(UserManager):
    pass











