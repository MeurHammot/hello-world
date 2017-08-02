# -*- encoding: utf-8 -*-

class User(object):
    IDs = [1]
    def __init__(self, login):
        self.login = login
        self.chat_rooms = []
        self.ID = User.IDs[len(User.IDs)-1]
        User.IDs.append(self.ID + 1)