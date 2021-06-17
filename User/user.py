from sys import setprofile

databaseSeparator='⠀' # Not a space (U+2800)

class User(object):
    id = 0
    name = ""
    discordId = ""
    avatarUrl = ""
    displayName = ""
    mention = ""

    def __init__(self, id, name, discordId, avatarUrl, displayName, mention):
        self.id = id
        self.name = name
        self.discordId = discordId
        self.avatarUrl = avatarUrl
        self.displayName = displayName
        self.mention = mention

        #testing 
    def print(self):
        print(f"this is user {self.id}: \n\
                            \t name = {self.name} \n\
                            \t discordId = {self.discordId} \n\
                            \t avatarUrl = {self.avatarUrl} \n\
                            \t displayName = {self.displayName} \n\
                            \t mention = {self.mention} \n\
                            \n")
