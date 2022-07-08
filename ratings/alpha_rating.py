class AlphaRating:

    # 1. hitung jumlah auction yang diselenggarakan suspected seller dan diikuti suspected bidder
    # 2. hitung jumlah kemenangan suspected bidder pada auction2 tersebut
    # 3. hitung jumlah auction yang diselenggarakan suspected seller
    # 4. aRating = (jumlah no.1 - jumlah no.2) / jumlah no.3 
    
    def __init__(self, participate_auction_number, win_auction_number, total_auction_number):
        self.participate_auction_number = participate_auction_number
        self.win_auction_number = win_auction_number
        self.total_auction_number = total_auction_number
    
    def calculate_alpha_rating(self):
        alpha_rating = (self.participate_auction_number - self.win_auction_number) / self.total_auction_number
        
        return alpha_rating

    
