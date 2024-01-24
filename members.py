from clashAPI.wrapper import apiWrapper
from definitions import *

class memberProcessing:
    apiClient = None

    def getMemberDonations(self,tag):
        memberList = []
        members = self.apiClient.getAllClanMembersByClanTag(tag)
        for member in members["items"]:
            memberList.append(Member(member["name"],member["tag"],member["donationsReceived"],member["donations"]))
        memberList.sort(key=lambda x: x.donations,reverse=True)
        return memberList
    def __init__(self):
        self.apiClient = apiWrapper()