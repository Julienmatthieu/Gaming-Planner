class Event(object):
    id = 0
    players = ''
    time = ''

    def __init__(self, id, player, time):
        self.id = id
        self.players = player
        self.time = time

def make_event(id, players, time):
    event = Event(id, players, time)
    return event