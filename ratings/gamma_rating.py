class GammaRating:

    # 1. Hitung jumlah semua auction yang telah diikuti bidder bersangkutan
    # 2. Hitung jumlah auction yang dimenangkan bidder bersangkutan

    def __init__(self, participate_auction_number, win_auction_number):
        self.win_auction_number = win_auction_number
        self.participate_auction_number = participate_auction_number
    
    def calculate_lost_auction(self) :
        lost_auction_number = self.participate_auction_number - self.win_auction_number

        return lost_auction_number
        
    def calculate_gamma_rating(self):
        #permit 25% loss to winning ration without penalty
        ratio_loss_win = (4 * (self.win_auction_number + 0.25)) / self.calculate_lost_auction()
        gamma_rating = 1 - ratio_loss_win

        return gamma_rating


