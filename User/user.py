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

    def print(self):
        print(f"this is user {self.id}: \n\
                            \t name = {self.name} \n\
                            \t discordId = {self.discord_id} \n\
                            \t avatarUrl = {self.avatarUrl} \n\
                            \t displayName = {self.displayName} \n\
                            \t mention = {self.mention} \n\
                            \n")
