from collusion.alternating_auction import AlternatingAuction
from collusion.alternating_bid import AlternatingBid

# collusion rating
# total_bidder_number = 5
# total_bidder_number = 6
total_bidder_number = 7

#  total_auction_number = 3
# total_auction_number = 3
total_auction_number = 4

# participate_auction_array = [[1, 1, 1], [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
# participate_auction_array = [[1, 1, 1], [1, 1, 1], [1, 1, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
participate_auction_array = [[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# binding factor
b_rating_bidder1 = 0.9 #CONTOH
b_rating_bidder2 = 0.8 #CONTOH

# grouping bidder based on collusion rating
error_factor = 0


# alternating bid

# alternating_bid_obj = AlternatingBid(total_bidder_number, total_auction_number, participate_auction_array, error_factor) 
# alternating_bid_result = alternating_bid_obj.calculate_edges_weight()
# b_rating_array = [0.9, 0.9, 0.8, 0.7, 0.6]

b_rating_array = [0.9, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]
# alternating_bid_result = alternating_bid_obj.calculate_binding_factor_rating(b_rating_array)
# print(alternating_bid_result)

# binding_factor = alternating_bid_obj.calculate_binding_factor(b_rating_bidder1, b_rating_bidder2)
# print(binding_factor)


# alternating auction
alternating_auction_obj = AlternatingAuction(total_bidder_number, total_auction_number, participate_auction_array, error_factor)
alternating_auction_result = alternating_auction_obj.calculate_binding_factor_rating(b_rating_array)
print(alternating_auction_result)











