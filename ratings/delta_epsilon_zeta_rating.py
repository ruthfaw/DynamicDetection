from array import array

class DeltaEpsilonZetaRating:

# untuk hitung delta rating per auction

    # 1. Hitung jumlah auction yang diikuti suspect bidder
    #     - Periksa auction -> kurangin jumlah total auction dengan jumlah total menang
    # 2. Untuk masing2 auction :
    #     - kalau jumlah bid dalam auction = 1, waktu interbid = 0
    #     - kalau jumlah bid > 1, waktu interbid = waktu bid supect - waktu bid sblmnya
    #    Kumpulin waktu interbidnya dlm bentuk array
    # 3. Hitung jumlah semua waktu interbid dalam array per auction
    # 4. Hitung jumlah bid yang diajukan suspect bidder per auction
    # 5. Hitung rata2 interbid time untuk suspect bidder per auction = jumlah waktu interbid / jumlah bid yang diajukan bidder
    # 6. Hitung juga rata2 interbid time untuk bidder lain, dan pilih yang max dan min
    # 7. Normalisasi = (rata2 interbid suspect - rata2 interbid min) / (rata2 interbid max - rata2 interbid min) -> lakukan untuk tiap auction
    # 8. Hitung rata2 interbid pada tiap auction = jumlah semua normalisasi pada setiap auction / jumlah auction
    # 9. kalkulasi rating = 1 - rata2 interbid per auction

    def __init__(self, participate_auction_number, bid_winning_number, normalization_array):
        self.participate_auction_number = participate_auction_number #f1
        self.bid_winning_number = bid_winning_number #f1
        self.normalization_array = normalization_array
        

    def not_winning_participation(self):
        total_participate = self.participate_auction_number - self.bid_winning_number

        return total_participate
    
    def calculate_delta_epsilon_zeta_rating(self):
        total_normalization = 0

        for normalization in self.normalization_array:
            total_normalization += normalization
        
        delta_epsilon_zeta_rating = total_normalization / self.not_winning_participation()

        return 1 - delta_epsilon_zeta_rating


       


   



    