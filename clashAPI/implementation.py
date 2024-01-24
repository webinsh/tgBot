from cocapi import CocApi

class clashAPI:
    token = None
    apiClient = None

    def getClanMembersByClanTag(self, tag):
        return self.apiClient.clan_members(tag)
    
    def __init__(self,token,timeout=60):
        self.token = token
        self.apiClient = CocApi(token,timeout)