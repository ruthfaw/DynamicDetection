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


#lakukan perhitungan rating untuk setiap bidder yang diperiksa

# -- globally needed variable --

# auction information
total_auction_number = 8
total_bidder_number = 10

# bidder information
# BIDDER 1
# participate_auction_number = 3
# win_auction_number = 1
# BIDDER 2
# participate_auction_number = 4
# win_auction_number = 1
# BIDDER 3
# participate_auction_number = 5
# win_auction_number = 1
# BIDDER 4
# participate_auction_number = 8
# win_auction_number = 0
# BIDDER 5
# participate_auction_number = 7
# win_auction_number = 2
# BIDDER 6
# participate_auction_number = 2
# win_auction_number = 0
# BIDDER 7
# participate_auction_number = 4
# win_auction_number = 1
# BIDDER 8
# participate_auction_number = 1
# win_auction_number = 0
# BIDDER 9
# participate_auction_number = 6
# win_auction_number = 1
# BIDDER 10
participate_auction_number = 8
win_auction_number = 1

# -- calculate alpha rating --

alpha_rating_obj = AlphaRating(participate_auction_number, win_auction_number, total_auction_number)
alpha_rating_result = alpha_rating_obj.calculate_alpha_rating()
print(alpha_rating_result)

# -- calculate beta rating --

# -- locally needed variale --

total_bid_per_auction = array('i', [24, 27, 37, 35, 26, 29, 31, 28])

# BIDDER 1
# bid_by_suspect_number = array('i', [0, 0, 2, 0, 3, 0, 0, 0])
# BIDDER 2
# bid_by_suspect_number = array('i', [0, 2, 6, 0, 0, 0, 1, 0])
# BIDDER 3
# bid_by_suspect_number = array('i', [0, 0, 0, 0, 3, 2, 2, 5])
# BIDDER 4
# bid_by_suspect_number = array('i', [10, 9, 7, 10, 7, 6, 8, 7])
# BIDDER 5
# bid_by_suspect_number = array('i', [2, 5, 1, 0, 0, 3, 0, 1])
# BIDDER 6
# bid_by_suspect_number = array('i', [0, 0, 3, 0, 0, 0, 4, 0])
# BIDDER 7
# bid_by_suspect_number = array('i', [2, 3, 0, 4, 0, 0, 0, 0])
# BIDDER 8
# bid_by_suspect_number = array('i', [0, 0, 0, 0, 0, 0, 5, 0])
# BIDDER 9
# bid_by_suspect_number = array('i', [0, 0, 5, 4, 3, 7, 0, 7])
# BIDDER 10
bid_by_suspect_number = array('i', [2, 2, 5, 5, 5, 4, 6, 0])

beta_rating_obj = BetaRating(participate_auction_number, win_auction_number, total_bid_per_auction, bid_by_suspect_number)
beta_rating_result = beta_rating_obj.calculate_beta_rating()
print(beta_rating_result)


# -- calculate gamma rating --

gamma_rating_obj = GammaRating(participate_auction_number, win_auction_number)
gamma_rating_result = gamma_rating_obj.calculate_gamma_rating()
print(gamma_rating_result)


# -- calculate delta rating --

# BIDDER 1
# array_normalization = [0, 0, 0.108, 0, 0.453, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.383, 0.276, 0, 0, 0, 0.182, 0]
# BIDDER 3
# array_normalization = [0, 0, 0, 0, 0.276, 0.112, 0.101, 1]
# BIDDER 4
# array_normalization = [0.042, 0.092, 0.037, 0.093, 0.087, 0.081, 0.029, 0.152]
# BIDDER 5
# array_normalization = [1, 0.263, 0.225, 0, 0, 1, 0, 0.078]
# BIDDER 6
# array_normalization = [0, 0, 1, 0, 0, 0, 0.790, 0]
# BIDDER 7
# array_normalization = [0.197, 0.733, 0, 1, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0, 0, 0, 0, 0, 0, 1, 0]
# BIDDER 9
# array_normalization = [0, 0, 0.189, 0.508, 1, 0.279, 0, 0.324]
# BIDDER 10
array_normalization = [0.279, 1, 0.148, 0.274, 0.168, 0.946, 0.405, 0]

delta_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
delta_rating_result = delta_rating_obj.calculate_delta_epsilon_zeta_rating()
print(delta_rating_result)


# -- calculate epsilon rating -> use DeltaEpsilonRating --

# BIDDER 1
# array_normalization = [0, 0, 0.35, 0, 0.59, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.45, 0.18, 0, 0, 0, 0.92, 0]
# BIDDER 3
# array_normalization = [0, 0, 0, 0, 0.56, 0.13, 0.56, 0.43]
# BIDDER 4
# array_normalization = [0.07, 0.06, 0.11, 0.10, 0.13, 0.07, 0.14, 0.10]
# BIDDER 5
# array_normalization = [0.93, 0.57, 1, 0, 0, 0.13, 0, 0.39]
# BIDDER 6
# array_normalization = [0, 0, 0.38, 0, 0, 0, 1, 0]
# BIDDER 7
# array_normalization = [1, 0.75, 0, 1, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0, 0, 0, 0, 0, 0, 0.96, 0]
# BIDDER 9
# array_normalization = [0, 0, 0.74, 0.44, 1, 0.41, 0, 0.44]
# BIDDER 10
array_normalization = [0.27, 1, 0.51, 0.22, 0.47, 0.13, 0.83, 0]

epsilon_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
epsilon_rating_result = epsilon_rating_obj.calculate_delta_epsilon_zeta_rating()
print(epsilon_rating_result)


# -- calculate zeta rating --
# BIDDER 1
# array_normalization = [0, 0, 0.35, 0, 0.428, 0, 0, 0]
# BIDDER 2
# array_normalization = [0, 0.439, 0.733, 0, 0, 0, 0.487, 0]
# BIDDER 3
# array_normalization = [0, 0, 0, 0, 0.746, 0.556, 0.776, 0.687]
# BIDDER 4
# array_normalization = [1, 1, 1, 1, 0.959, 1, 0.9, 1]
# BIDDER 5
# array_normalization = [0.439, 0.609, 0.317, 0, 0, 0.755, 0, 0.445]
# BIDDER 6
# array_normalization = [0, 0, 0.167, 0, 0, 0, 0.882, 0]
# BIDDER 7
# array_normalization = [0.633, 0.916, 0, 0.581, 0, 0, 0, 0]
# BIDDER 8
# array_normalization = [0, 0, 0, 0, 0, 0, 1, 0]
# BIDDER 9
# array_normalization = [0, 0, 0.468, 0.719, 0.487, 0.504, 0, 0.584]
# BIDDER 10
array_normalization = [0.754, 0.803, 0.678, 0.687, 0.657, 0.729, 0.73, 0]

zeta_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
zeta_rating_result = zeta_rating_obj.calculate_delta_epsilon_zeta_rating()
print(zeta_rating_result)


# -- calculate shill score
shill_score_obj = ShillScore(alpha_rating_result, beta_rating_result, gamma_rating_result, delta_rating_result, epsilon_rating_result, zeta_rating_result)
shill_score = shill_score_obj.calculate_shill_score()
print(shill_score) 
# determine_bidder = shill_score_obj.isAShill()













