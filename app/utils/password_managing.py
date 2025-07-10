#Password manager class to verify and hash the passwords


from passlib.hash import bcrypt


class Password_Manager:
    @staticmethod
    def hash_password(init_password:str)->str:
        return bcrypt.hash(init_password)

    @staticmethod
    def verify_password(init_password: str, secret: str)->bool:
        return bcrypt.verify(init_password, secret)