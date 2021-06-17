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
   
def build_event(id, players, time, slots):
    return Event(id, players, time, slots)

class Location(object):
    id = 0
    serverId = 0
    channelId = 0
    messageId = 0
    eventId = 0
    def __init__(self, id, serverId, channelId, messageId, eventId):
        self.id = id
        self.serverId = serverId
        self.channelId = channelId
        self.messageId = messageId
        self.eventId = eventId

def build_location(id, serverId, channelId, messageId, eventId):
    return Location(id, serverId, channelId, messageId, eventId)