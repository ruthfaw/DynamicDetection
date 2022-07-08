from array import array

class BetaRating:

    # 1. Ada berapa auction yang diikuti
    #     - Periksa auction -> kurangin jumlah total auction dengan jumlah total menang
    # 2. Untuk masing2 auction hitung jumlah bid yang diajukan semua bidder, kemudian hitung worst case (jumlah bid / 2)
    # 3. hitung jumlah bid yang diajukan suspected bidder
    # 4. hitung persentase bid yang diajukan suspected bidder (jumlah bid yang diajukan suspected bidder / worst case)
    # 5. kalkulasi rating
    #     - klo jumlah total auction stlh dikurangin abis -> bRating = 0
    #     - klo masih ada, itung rata bRating (jumlah persentase bid dr suspected bidder / jumlah total auction yang diikuti)

    def __init__(self, participate_auction_number, winning_auction_number, total_bid_per_auction, bid_by_suspect_number):
        self.participate_auction_number = participate_auction_number #f1
        self.winning_auction_number = winning_auction_number #f1
        self.total_bid_per_auction = total_bid_per_auction #musi array #f2
        self.bid_by_suspect_number = bid_by_suspect_number #musi array #f3
    
    def not_winning_participation(self):
        total_participate = self.participate_auction_number - self.winning_auction_number

        return total_participate
    
    def worst_case_per_auction(self):
        #ada for buat arraynya
        worst_case_number = []

        for total_bid in self.total_bid_per_auction:
            worst_case_number.append(total_bid / 2)

        return worst_case_number
    
    def bid_percentage_per_auction(self):
        bid_percentage_number = []
        worst_case_number = self.worst_case_per_auction()

        for bid_suspect, worst_case in zip(self.bid_by_suspect_number, worst_case_number):
            bid_percentage_number.append(bid_suspect / worst_case)
    
        return bid_percentage_number

    def calculate_beta_rating(self):
        bid_percentage_number = self.bid_percentage_per_auction()
        total_bid_percentage = 0

        for bid_percentage in bid_percentage_number:
            total_bid_percentage += bid_percentage

        beta_rating = total_bid_percentage /  self.not_winning_participation()
        
        return beta_rating


     

       

    