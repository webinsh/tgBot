class Member:
    def __init__(self, name, tag, receivedDonations, donations):
        self.name = name
        self.tag = tag
        self.receivedDonations = receivedDonations
        self.donations = donations
    
    def debugPrint(self):
        print(f"Tag: {self.tag} Name: {self.name} ReceivedDonations: {self.receivedDonations} Donations: {self.donations}")