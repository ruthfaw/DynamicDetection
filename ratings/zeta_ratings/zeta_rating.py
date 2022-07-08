class ZetaRating:

    # 1. Hitung jumlah auction yang diikuti suspect bidder
    #     - Periksa auction -> kurangin jumlah total auction dengan jumlah total menang
    # 2. Untuk masing2 auction :
        # - hitung selisih waktu ekspirasi dengan waktu awal bid untuk setiap bidder (krn kita akan ambil selisih suspect bidder, max, dan min)
        # - hitung hasil normalisasi untuk bidder trsbt ( (selisih suspect - selisih min)/(selisih max - selisih min) )
    # 3. Jumlah hasil normalisasi untuk semua auction / jumlah auction yang diikuti = zeta rating

    def __init__(self, participate_auction_number, bid_winning_number, normalization_array):
        self.participate_auction_number = participate_auction_number #f1
        self.bid_winning_number = bid_winning_number #f1
        