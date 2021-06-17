class Event(object):
    id = 0
    players = ''
    time = ''
    slots = 1
    gameName = ''
    role = ''
    author = ''

    def __init__(self, id, gameName, slots, time, author, player, role):
        self.id = id
        self.players = player
        self.time = time
        self.slots = slots
        self.gameName = gameName
        self.author = author
        self.role = role

class Location(object):
    id = 0
    guildId = 0
    channelId = 0
    messageId = 0
    eventId = 0
    def __init__(self, id, guildId, channelId, messageId, eventId):
        self.id = id
        self.guildId = guildId
        self.channelId = channelId
        self.messageId = messageId
        self.eventId = eventId
