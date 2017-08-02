# -*- encoding: utf-8 -*-

class Chat(object):
    '''Class for chat'''
    IDs = [1]
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.ID = Chat.IDs[len(Chat.IDs)-1]
        self.members = [self.owner]
        Chat.IDs.append(self.ID + 1)
    def join(self, user):
        self.members.append(user)
        return self.members
    def say(self, user):
        result = []
        for member in self.members:
            if member != user:
                result.append(member)
        return result
    def leave(self, user):
        for i in range(0, len(self.members)):
            if self.members[i] == user:
                del self.members[i]
                break
        else:
            return False
        return self.members
