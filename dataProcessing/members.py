from ..clashAPI.wrapper import apiWrapper

class memberProcessing:
    apiClient = None

    def getMemberDonations(self,tag):
        members = self.piClient.getAllClanMembersByClanTag(self, tag)
        for member in members:
            print(member["name"])

    def __init__(self):
        self.apiClient = apiWrapper()

process = memberProcessing()
process.getMemberDonations("#2QQL2VYQ2")