from sys import setprofile

databaseSeparator='⠀' # Not a space (U+2800)

class User(object):
    id = 0
    name = ""
    discordId = ""
    avatarUrl = ""
    displayName = ""
    mention = ""

    def __init__(self, id, name, discordId, avaterUrl, displayName, mention):
        self.id = id
        self.discordId = discordId
        self.avaterUrl = avaterUrl
        self.displayName = displayName
        self.mention = mention
