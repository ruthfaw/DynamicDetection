class GammaRating:

    # 1. Hitung jumlah semua auction yang telah diikuti bidder bersangkutan
    # 2. Hitung jumlah auction yang dimenangkan bidder bersangkutan

    def __init__(self, participate_auction_number, win_auction_number):
        self.win_auction_number = win_auction_number
        self.participate_auction_number = participate_auction_number
       
    def calculate_gamma_rating(self):
        gamma_rating = 1 - (self.win_auction_number/self.participate_auction_number)

        return gamma_rating


