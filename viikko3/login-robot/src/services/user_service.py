from entities.user import User
import sys, pdb

class UserInputError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        # pysäytetään ohjelman suoritus tälle riville
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if username in self._user_repository.find_by_username(username):
            raise UserInputError(f"Username {username} already exists")

        if len(username) <= 3:
            raise UserInputError(f"Username is too short, minimum length is 3")

        if len(password) <= 3:
            raise UserInputError(f"Password is too short, minimum length is 8")

        if password.isalpha():
            raise UserInputError("Password must contain at least one number")