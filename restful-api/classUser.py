#!/usr/bin/python3
"""
create a user class
"""

class User(Basemodel):
    """
    create a new_user
    """

    def __init(self, name="", last_name="", mail, password):
        """
        init inscription new user
        """


        self.name = name
        self.last_name = last_name
        self.mail = mail
        self.password = password