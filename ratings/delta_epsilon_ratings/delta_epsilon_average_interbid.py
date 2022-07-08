class AverageInterbid:

    # hitung avg interbid per bidder untuk suatu auction

    def __init__(self, interbid_array, bid_by_suspect_number):
        self.interbid_array = interbid_array 
        self.bid_by_suspect_number = bid_by_suspect_number 

    def average_interbid(self):
        total_interbid = 0

        for interbid in self.interbid_array:
            total_interbid += interbid
        average_interbid_result = total_interbid / self.bid_by_suspect_number

        return average_interbid_result

        