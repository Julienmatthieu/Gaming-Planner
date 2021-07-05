from sys import setprofile

from resources import databaseSeparator


class Event(object):
    id = 0
    players = []
    players_id = []
    time = ''
    slots = 1
    role = ''
    authorId = 0
    step = 0
    game_id = 0
    late = []
    
    def __init__(self, id, players, time, slots, authorId, role, step, players_id, game_id, late):
        self.id = id
        self.players = []
        self.players_id = []
        self.late= []
        if players:
            for p in players.split(databaseSeparator):
                self.players.append(p)
        if players_id:
            for p in players_id.split(databaseSeparator):
                self.players_id.append(p)
        if late:
            for p in late.split(databaseSeparator):
                self.late.append(p)
        self.time = time
        self.slots = slots
        self.authorId = authorId
        self.role = role
        self.step = step
        self.game_id = game_id

    def merge(self, other):
        self.players = other.players
        self.players_id = other.players_id
        self.late = other.late
        self.time = other.time
        self.slots = other.slots
        self.authorId = other.authorId
        self.role = other.role
        self.step = other.step
        self.game_id = other.game_id

    def add_player(self, user):
        if user.displayName in self.players:
            return
        self.players_id.append(user.discord_id)
        self.players.append(user.displayName)

    def remove_player(self, user):
        size = len(self.players)
        if user.displayName in self.players:
            index = self.players.index(user.displayName)
            self.players.pop(index)
            self.players_id.pop(index)
            return True
        elif user.displayName in self.late:
            index = self.late.index(user.displayName)
            self.late.pop(index)
            return True
        return False

    def add_late_player(self, user):
        if self.is_present(user):
            self.remove_player(user)
        if user.displayName not in self.late:
            self.late.append(user.displayName)

    def remove_late_player(self, user):
        if user.displayName in self.late:
            index = self.late.index(user.displayName)
            self.late.pop(index)

    def is_present(self, user):
        return (user.displayName in self.players)
    
    def print(self):
        print(f"this is event {self.id}: \n\
                            \tplayers = {self.players} \n\
                            \tplayers_id = {self.players_id} \n\
                            \ttime = {self.time} \n\
                            \tslots = {self.slots} \n\
                            \tauthorId = {self.authorId} \n\
                            \trole = {self.role} \n\
                            \tgame_id = {self.game_id} \n\
                            `\tlate = {self.late} \n\
                            `\step = {self.step} \n\
                            \n")

class Location(object):
    id = 0
    guildId = "0"
    channelId = "0"
    messageId = None
    eventId = 0

    def __init__(self, id, guildId, channelId, messageId, eventId):
        self.id = id
        self.guildId = guildId
        self.channelId = channelId
        self.messageId = messageId
        self.eventId = eventId
