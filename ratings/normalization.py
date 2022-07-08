class Normalization:

    #1. passing array avg_interbid untuk bidder-bidder pada suatu auction, tentuin max dan min nya

    def __init__(self, avg_interbid_array, suspect_bidder_avg_interbid):
        self.max_avg_interbid = max(avg_interbid_array)
        self.min_avg_interbid = min(avg_interbid_array)
        self.suspect_bidder_avg_interbid = suspect_bidder_avg_interbid 

    def normalize_avg_interbid(self):
        normalization_result = (self.suspect_bidder_avg_interbid - self.min_avg_interbid) / (self.max_avg_interbid - self.min_avg_interbid)

        return normalization_result
