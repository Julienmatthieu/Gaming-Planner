class Event(object):
    id = 0
    players = ''
    time = ''

    def __init__(self, id, player, time):
        self.id = id
        self.players = player
        self.time = time
   
def build_event(id, players, time):
    return Event(id, players, time)

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