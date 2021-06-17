from sys import setprofile


databaseSeparator='⠀' # Not a space (U+2800)

class Event(object):
    id = 0
    players = ''
    time = ''
    slots = 1
    gameName = ''
    role = ''
    authorId = 0
    step = 0
    
    def __init__(self, id, player, time, slots, gameName, authorId, role, step):
        self.id = id
        self.players = player
        self.time = time
        self.slots = slots
        self.gameName = gameName
        self.authorId = authorId
        self.role = role
        self.step = step
    
    def merge(self, other):
        self.players = other.players
        self.time = other.time
        self.slots = other.slots
        self.gameName = other.gameName
        self.authorId = other.authorId
        self.role = other.role
        self.step = other.step

    def get_list_players(self):
        players = list()
        for player in self.players.split(databaseSeparator):
            players.append(player)
        return players

    def AddUserToEvent(self, userName):
        if len(get_list_players()) < slots:
            self.players += databaseSeparator + userName


    #def RemoveUserFromEvent(user):
    #    global author
#
    #    players.remove(user.name)
    #    if user.name == author and len(players) > 0:
    #        author = players[0]

    #testing 
    def print(self):
        print(f"this is event {self.id}: \n\
                            \tplayers = {self.players} \n\
                            \ttime = {self.time} \n\
                            \tslots = {self.slots} \n\
                            \tgameName = {self.gameName} \n\
                            \tauthorId = {self.authorId} \n\
                            \trole = {self.role} \n\
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
