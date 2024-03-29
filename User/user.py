from sys import setprofile

class User(object):
    id = 0
    name = ""
    discord_id = ""
    avatarUrl = ""
    displayName = ""
    mention = ""

    def __init__(self, id, name, discordId, avatarUrl, displayName, mention):
        self.id = id
        self.name = name
        self.discord_id = discordId
        self.avatarUrl = avatarUrl
        self.displayName = displayName
        self.mention = mention

    def need_update(self, source):

        if self.name != source.name or self.avatarUrl != source.avatarUrl or self.displayName != source.displayName or self.mention != source.mention :
            return True
        return False

    def print(self):
        print(f"this is user {self.id}: \n\
                            \t name = {self.name} \n\
                            \t discordId = {self.discord_id} \n\
                            \t avatarUrl = {self.avatarUrl} \n\
                            \t displayName = {self.displayName} \n\
                            \t mention = {self.mention} \n\
                            \n")

    def copy(self, source):
        self.name = source.name
        self.discord_id = source.discord_id
        self.avatarUrl = source.avatarUrl
        self.displayName = source.displayName
        self.mention = source.mention