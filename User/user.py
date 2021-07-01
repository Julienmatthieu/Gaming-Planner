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

        print(" ---  ENTERING NEED UPDATE --- ")
        self.print()
        source.print()

        print(f"1 - {self.name != source.name}")
        print(f"2 - \"self.avatarUrl != source.avatarUrl\" {self.avatarUrl != source.avatarUrl}")
        type(self.avatarUrl)
        type(source.avatarUrl)
        print(f'2 - \"Source print self\" {source.avatarUrl != "https://cdn.discordapp.com/avatars/225743846934446081/afc9af98a91cb4a6f1d24d9a7c9982dc.webp?size=1024"}')
        print(f'2 - \"Source print sour\" {source.avatarUrl != "https://cdn.discordapp.com/avatars/225743846934446081/afc9af98a91cb4a6f1d24d9a7c9982dc.webp?size=1024"}')
        print(f'2 - \"self.avatarUrl != self.avatarUrl\" {self.avatarUrl != "https://cdn.discordapp.com/avatars/225743846934446081/afc9af98a91cb4a6f1d24d9a7c9982dc.webp?size=1024"}')
        print(f"2 self.avatarUrl- \"{self.avatarUrl}\"")
        print(f"2 sour.avatarUrl- \"{source.avatarUrl}\"")
        print(f"3 - {self.displayName != source.displayName}")
        print(f"4 - {self.mention != source.mention}")

        if self.name != source.name or self.avatarUrl != source.avatarUrl or self.displayName != source.displayName or self.mention != source.mention :
            print("true")
            return True
        print("false")
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