class Event(object):
    id = 0
    players = ''
    time = ''
    slots = 1

    def __init__(self, id, player, time, slots):
        self.id = id
        self.players = player
        self.time = time
        self.slots = slots

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
