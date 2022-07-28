from array import array

# alpha rating
from ratings.alpha_rating import AlphaRating
# beta rating
from ratings.beta_rating import BetaRating
# gamma rating 
from ratings.gamma_rating import GammaRating
# delta rating
from ratings.delta_epsilon_ratings.delta_epsilon_average_interbid import AverageInterbid
from ratings.normalization.normalization import Normalization
from ratings.delta_epsilon_zeta_rating import DeltaEpsilonZetaRating
from shills.shill_score import ShillScore

from collusion.alternating_auction import AlternatingAuction
from collusion.alternating_bid import AlternatingBid


#lakukan perhitungan rating untuk setiap bidder yang diperiksa

# -- globally needed variable --

# auction information
total_auction_number = 8
total_bidder_number = 10

# bidder information
# BIDDER 4 & 9
# participate_auction_number = 6
# win_auction_number = 0
# BIDDER 1
participate_auction_number = 3
win_auction_number = 1
# BIDDER 2 & 7 & 8
# participate_auction_number = 4
# win_auction_number = 1
# BIDDER 3 & 5 & 10
# participate_auction_number = 5
# win_auction_number = 1
# BIDDER 6
# participate_auction_number = 2
# win_auction_number = 1


# Ratings for bidder number 1

# -- calculate alpha rating --

alpha_rating_obj = AlphaRating(participate_auction_number, win_auction_number, total_auction_number)
alpha_rating_result = alpha_rating_obj.calculate_alpha_rating()
# print(alpha_rating_result)

# -- calculate beta rating --

# -- locally needed variale --
total_bid_per_auction = array('i', [17, 20, 25, 9, 18, 17, 12, 22])
# BIDDER 4
# bid_by_suspect_number = array('i', [2, 3, 1, 0, 4, 1, 0, 5])
# BIDDER 9
# bid_by_suspect_number = array('i', [2, 4, 2, 0, 3, 2, 0, 6])
# BIDDER 1
bid_by_suspect_number = array('i', [0, 0, 2, 0, 3, 0, 0, 0])
# BIDDER 2
# bid_by_suspect_number = array('i', [0, 2, 6, 0, 0, 0, 1, 0])
# BIDDER 3
# bid_by_suspect_number = array('i', [0, 0, 6, 0, 0, 2, 2, 5])
# BIDDER 5
# bid_by_suspect_number = array('i', [2, 0, 0, 0, 5, 3, 0, 1])
# BIDDER 6
# bid_by_suspect_number = array('i', [0, 0, 3, 0, 0, 0, 0, 0])
# BIDDER 7
# bid_by_suspect_number = array('i', [2, 3, 0, 4, 0, 0, 0, 0])
# BIDDER 8
# bid_by_suspect_number = array('i', [2, 0, 1, 0, 0, 0, 5, 0])
# BIDDER 10
# bid_by_suspect_number = array('i', [2, 2, 0, 3, 0, 4, 0, 0])

beta_rating_obj = BetaRating(participate_auction_number, win_auction_number, total_bid_per_auction, bid_by_suspect_number)
beta_rating_result = beta_rating_obj.calculate_beta_rating()
# print(beta_rating_result)


# -- calculate gamma rating --

gamma_rating_obj = GammaRating(participate_auction_number, win_auction_number)
gamma_rating_result = gamma_rating_obj.calculate_gamma_rating()
# print(gamma_rating_result)


# -- calculate delta rating --
# BIDDER 4 
# array_normalization = [0.516, 0.430, 0.874, 0, 0.462, 0.667, 0, 0.802]
# BIDDER 9
# array_normalization = [0.366, 0.598, 0.661, 0, 1, 0.703, 0, 1]
# BIDDER 1
array_normalization = [0, 0, 1, 0, 0.719, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.721, 0.687, 0, 0, 0, 1, 0]
# BIDDER 3
# array_normalization = [0, 0, 0.865, 0, 0, 0.591, 0.555, 0.984]
# BIDDER 5
# array_normalization = [1, 0, 0, 0, 0.826, 0.847, 0, 0.808]
# BIDDER 6
# array_normalization = [0, 0, 0.463, 0, 0, 0, 0, 0]
# BIDDER 7
# array_normalization = [0.857, 0.733, 0, 0, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0.825, 0, 0.630, 0, 0, 0, 0.673, 0]
# BIDDER 10
# array_normalization = [0.884, 1, 0, 0.645, 0, 1, 0, 0]

delta_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
delta_rating_result = delta_rating_obj.calculate_delta_epsilon_zeta_rating()
# print(delta_rating_result)


# -- calculate epsilon rating -> use DeltaEpsilonRating --
# BIDDER 4
# array_normalization = [0.138, 0.171, 1, 0, 0.295, 0.625, 0, 0.353]
# BIDDER 9
# array_normalization = [0.379, 0.410, 0.4, 0, 1, 0.5, 0, 1]
# BIDDER 1
array_normalization = [0, 0, 0.6, 0, 0.607, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.308, 0.5, 0, 0, 0, 0.909, 0]
# BIDDER 3
# array_normalization = [0, 0, 0.467, 0, 0, 0.750, 1, 0.186]
# BIDDER 5
# array_normalization = [0.655, 0, 0, 0, 0.857, 1, 0, 0.343]
# BIDDER 6
# array_normalization = [0, 0, 0.833, 0, 0, 0, 0, 0]
# BIDDER 7
# array_normalization = [0.345, 0.239, 0, 0.460, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0.276, 0, 0.5, 0, 0, 0, 0.945, 0]
# BIDDER 10
# array_normalization = [1, 1, 0, 1, 0, 0.875, 0, 0, 0]

epsilon_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
epsilon_rating_result = epsilon_rating_obj.calculate_delta_epsilon_zeta_rating()
# print(epsilon_rating_result)


# -- calculate zeta rating --
# BIDDER 4 
# array_normalization = [1, 1, 0.683, 0, 1, 0.956, 0, 0.823]
# BIDDER 9
# array_normalization = [0.972, 0.984, 0.647, 0, 0.951, 0.938, 0, 0.790]
# BIDDER 1
array_normalization = [0, 0, 0.999, 0, 0.301, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.692, 0.748, 0, 0, 0, 0.714, 0]
# BIDDER 3
# array_normalization = [0, 0, 0.634, 0, 0, 0.984, 0.5, 1]
# BIDDER 5
# array_normalization = [0.801, 0, 0, 0, 0.704, 0.972, 0, 0.965]
# BIDDER 6
# array_normalization = [0, 0, 1, 0, 0, 0, 0, 0]
# BIDDER 7
# array_normalization = [0.499, 0.688, 0, 1, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0.541, 0, 0.439, 0, 0, 0, 1, 0]
# BIDDER 10
# array_normalization = [0.221, 0.599, 0, 0.853, 0, 0.211, 0, 0]

zeta_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
zeta_rating_result = zeta_rating_obj.calculate_delta_epsilon_zeta_rating()
# print(zeta_rating_result)


# -- calculate shill score for bidder 1
shill_score_obj = ShillScore(alpha_rating_result, beta_rating_result, gamma_rating_result, delta_rating_result, epsilon_rating_result, zeta_rating_result)
shill_score = shill_score_obj.calculate_shill_score()
# print(shill_score) 
# determine_bidder = shill_score_obj.isAShill()

participate_auction_array = [[0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 0, 0, 0], 
                             [1, 1, 0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0], 
                            [1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 0], 
                            [1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], 
                            [1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 1]]

error_factor = 0

alternating_bid_obj = AlternatingAuction(total_bidder_number, total_auction_number, participate_auction_array, error_factor) 
alternating_bid_result = alternating_bid_obj.normalize_weight()
print(alternating_bid_result)
# [0.2857142857142857, 0.7142857142857143, 0.8571428571428571, 1.0, 0.8095238095238095, 0.0, 0.6190476190476191, 0.5714285714285714, 1.0, 0.9047619047619048]

b_rating_array = [0.247, 0.282, 0.376, 0.272, 0.309, 0.25, 0.48, 0.384, 0.32, 0.393]
a_rating_array = [0.25, 0.375, 0.5, 0.75, 0.5, 0.125, 0.375, 0.375, 0.75, 0.5]
alternating_bid_result1 = alternating_bid_obj.calculate_binding_factor_rating(a_rating_array)
print(alternating_bid_result1)















