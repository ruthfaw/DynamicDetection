from array import array

# alpha rating
from ratings.alpha_rating import AlphaRating
# beta rating
from ratings.beta_rating import BetaRating
# gamma rating 
from ratings.gamma_rating import GammaRating
# delta rating
from ratings.delta_epsilon_ratings.delta_epsilon_average_interbid import AverageInterbid
from ratings.normalization import Normalization
from ratings.delta_epsilon_zeta_rating import DeltaEpsilonZetaRating
# epsilon rating
# zeta rating

#lakukan perhitungan rating untuk setiap bidder yang diperiksa

# -- globally needed variable --

participate_auction_number = 8
win_auction_number = 0


# -- calculate alpha rating --

# alpha_rating_obj = AlphaRating(participate_auction_number, win_auction_number, 8)
# alpha_rating_result = alpha_rating_obj.calculate_alpha_rating()
## print(alpha_rating_result)


# -- locally needed variale --

# total_bid_per_auction = array('i', [24, 27, 37, 35, 26, 29, 31, 28])
# bid_by_suspect_number = array('i', [10, 9, 7, 10, 7, 6, 8, 7])

# -- calculate beta rating --

# beta_rating_obj = BetaRating(participate_auction_number, win_auction_number, total_bid_per_auction, bid_by_suspect_number)
# beta_rating_result = beta_rating_obj.calculate_beta_rating()
## print(beta_rating_result)


# -- calculate gamma rating --

# gamma_rating_obj = GammaRating(participate_auction_number, win_auction_number)
# gamma_rating_result = gamma_rating_obj.calculate_gamma_rating()
# print(gamma_rating_result)


# -- calculate delta rating --

# calculate avg suspect bidder (for ex : auction 1)
array_interbid_suspect = [0, 3, 2, 6, 7, 2, 7, 5, 3, 2]
avg_interbid_suspect = AverageInterbid(array_interbid_suspect, len(array_interbid_suspect))
avg_interbid_suspect_result = avg_interbid_suspect.average_interbid()
print(avg_interbid_suspect_result) # 3.7

# calculate normalization -> for all bidder in an auction (for ex.auction 1)
array_avg_interbid = [avg_interbid_suspect_result, 3.6, 3.4, 3.57, 3.2] # MASIH ASAL # banyaknya harus sama kaya jumlah participant di auction itu
avg_interbid_normalization = Normalization(array_avg_interbid, avg_interbid_suspect_result)
normalization_result = avg_interbid_normalization.normalize_avg_interbid()
print(normalization_result) # 1 # result between 0 to 1

# calculate delta rating 
array_normalization = [1, 0.2, 0.1, 1, 0.05, 0, 0.4, 0.13]
delta_rating_obj = DeltaEpsilonZetaRating(participate_auction_number, win_auction_number, array_normalization)
delta_rating_result = delta_rating_obj.calculate_delta_epsilon_zeta_rating()
print(delta_rating_result)


# -- calculate epsilon rating -> use DeltaEpsilonRating --



# -- calculate zeta rating --










