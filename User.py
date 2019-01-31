from flask import current_app
from applo

class User:

    def __init__(self, username, password, emal):
        self.username = username
        self.password password
        self.email = email

    def print_info(self):
        current_app.logger.info('Username: {}', self.username)
        current_app.logger.info('Password: {}', self.password)
        current_app.logger.info('Email: {}', self.email)

