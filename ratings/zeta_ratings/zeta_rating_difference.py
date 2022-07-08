class Difference:

    def __init__(self, firstbid_time_suspect, auction_expiration_time):
        self.firstbid_time_suspect = firstbid_time_suspect
        self.auction_expiration_time = auction_expiration_time

    def difference_bid_time(self):
        difference_bid_time = self.auction_expiration_time - self.firstbid_time_suspect
        
        return difference_bid_time
