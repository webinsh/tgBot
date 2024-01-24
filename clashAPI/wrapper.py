from .implementation import *
from .config import *

class apiWrapper:
    apiObject = None

    def getAllClanMembersByClanTag(self, tag):
        return self.apiObject.getClanMembersByClanTag(tag)
    
    def __init__(self):
        self.apiObject = clashAPI(TOKEN)