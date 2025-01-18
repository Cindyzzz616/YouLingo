from backend.Entities import User


class FetchUserData:
    """
    Return all the data associated with a user when provided with an email.
    """
    email: str

    def __init__(self, email: str) -> None:
        self.email = email

    # make this into a class method instead?

    def get_user(self) -> User:
        # iterate through the database to find the user that has the right email?
        # get the list of users from the database as a dict or list first?
        return

    def get_user_data(self) -> dict:
        user = self.get_user()
        # have to figure out what to return
        return user
