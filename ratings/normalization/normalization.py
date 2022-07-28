class Normalization:

    def __init__(self, suspect_bidder_avg_interbid, max_avg_interbid, min_avg_interbid):
        self.suspect_bidder_avg_interbid = suspect_bidder_avg_interbid 
        self.max_avg_interbid = max_avg_interbid
        self.min_avg_interbid = min_avg_interbid

    def normalize_avg_interbid(self):
        normalization_result = (self.suspect_bidder_avg_interbid - self.min_avg_interbid) / (self.max_avg_interbid - self.min_avg_interbid)

        return normalization_result
