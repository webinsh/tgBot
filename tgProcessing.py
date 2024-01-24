from members import memberProcessing
import prettytable as pt
import numpy as np

class dataProcessing:
    profileLinkTemplate = "https://link.clashofclans.com/en/?action=OpenPlayerProfile&tag="
    def getTelegramMessageMemberDonations(self):
        memberObject = memberProcessing()
        members = memberObject.getMemberDonations(self.clanTag)
        table = pt.PrettyTable(['№', 'Ник', 'Тэг', 'Задонатил', 'Скомуниздил'])
        table.align['№'] = 'l'
        table.align['Ник'] = 'r'
        table.align['Ссылка'] = 'r'
        table.align['Задонатил'] = 'r'
        table.align['Скомуниздил'] = 'r'

        for idx, member in enumerate(members):
            member.tag = member.tag.replace('#','')
            #memberList.append(Member(member["name"],member["tag"],member["donationsReceived"],member["donations"]))
            table.add_row([idx,member.name,member.tag, member.donations,member.receivedDonations])
        
        return table
    
    def __init__(self,clanTag):
        self.clanTag = clanTag

def getMemberDonations(self,tag):
    table = pt.PrettyTable(['№', 'Ник', 'Тэг', 'Задонатил', 'Скомуниздил'])
    table.align['№'] = 'l'
    table.align['Ник'] = 'r'
    table.align['Тэг'] = 'r'
    table.align['Задонатил'] = 'r'
    table.align['Скомуниздил'] = 'r'

    members = self.apiClient.getAllClanMembersByClanTag(tag)
    for idx, member in enumerate(members["items"]):
        #memberList.append(Member(member["name"],member["tag"],member["donationsReceived"],member["donations"]))
        table.add_row([idx,member["name"],member["tag"], member["donationsReceived"],member["donations"]])
    return table