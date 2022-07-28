class Hybrid:

    def __init__(self, total_bidder_number, total_auction_number, participate_auction_array, error_factor):
        self.total_bidder_number = total_bidder_number
        self.total_auction_number = total_auction_number
        self.participate_auction_array = participate_auction_array
        self.error_factor = error_factor
    
    # for collusion rating
    def calculate_edges_weight(self):
        weight_array = [0] * self.total_bidder_number
        addition_limit = self.total_bidder_number-1

        for x in range(0, self.total_bidder_number):
            z = 1
            while z <= addition_limit:
                for y in range(0, self.total_auction_number):
                    if self.participate_auction_array[x][y] == 1 and self.participate_auction_array[x+z][y] == 1:
                        weight_array[x] += 1
                        weight_array[x+z] += 1
                z += 1
            addition_limit -= 1

        return weight_array
    
    # for collusion rating
    def normalize_weight(self):
        weight_array = self.calculate_edges_weight()
        max_weight = max(weight_array)
        min_weight = min(weight_array)

        normalize_result_array = []

        for weight in weight_array:
            normalize_result_number = (weight - min_weight) / (max_weight - min_weight)
            normalize_result_array.append(normalize_result_number)

        return normalize_result_array
    
     # created based on my own perception, because there is no efficient information about grouping bidders
    def grouping_bidders(self):
        normalize_array = self.normalize_weight()
        addition_limit = self.total_bidder_number

        rows, cols = (self.total_bidder_number, self.total_bidder_number) 
        group_array = [[-1 for i in range(cols)] for j in range(rows)]

        group_index_first = 0
        last_number = 0

        for x in range(0, self.total_bidder_number):
            addition_limit -= 1
            if(x < last_number + 1 and x != 0): 
                continue

            z = 1
            last_number = 0

            group_array[group_index_first][0] += (x+1)
            while z <= addition_limit:
                if normalize_array[x] == 0:
                    break
                elif normalize_array[x] == normalize_array[x+z] + self.error_factor or normalize_array[x] == normalize_array[x+z] - self.error_factor:
                    group_array[group_index_first][z] += (x+z+1)
                    last_number = x+z 
                z += 1
            group_index_first += 1

        return group_array
    
    # used for avg rating and binding factor
    def calculate_binding_factor_rating(self, b_rating_array):
        avg_binding_factor = []
        group_array = self.grouping_bidders()

        for x in range(0, self.total_bidder_number):
            if group_array[x][0] == -1:
                continue
            
            addition_limit = self.total_bidder_number
            total_per_group = 0
            size = 0

            for y in range(0, self.total_bidder_number):
                addition_limit -= 1
                z = 1
                while z < addition_limit:
                    if group_array[x][y+z] == -1:
                        break
                    index_first = group_array[x][y]
                    index_last = group_array[x][y+z]
                    total_per_group += (min(b_rating_array[index_first], b_rating_array[index_last]) / max(b_rating_array[index_first], b_rating_array[index_last]))
                    z += 1
                    size += 1
            if size == 0:
                avg_binding_factor.append(0)
            else:
                avg_binding_factor.append(total_per_group / size)
        
        return avg_binding_factor

    def calculate_avg_rating(self, rating_array):
        total_rating = 0

        for binding_factor in rating_array:
            total_rating += binding_factor
        
        avg_binding_factor_rating = total_rating / len(rating_array)

        return avg_binding_factor_rating
    
    def calculate_collusion_score(self, avg_gamma_rating, avg_delta_rating, avg_epsilon_rating, avg_zeta_rating, collusion_rating, binding_factor_b, binding_factor_a):
        # can be changed later (must be 1-7)
        gamma_weight = 1
        delta_weight = 3
        epsilon_weight = 3
        zeta_weight = 1
        collusion_rating_weight = 7
        binding_factor_b_weight = 7
        binding_factor_a_weight = 7

        collusion_score = (((avg_gamma_rating * gamma_weight) + (avg_delta_rating * delta_weight) + (avg_epsilon_rating * epsilon_weight) + (avg_zeta_rating * zeta_weight) + (collusion_rating * collusion_rating_weight) + (binding_factor_b * binding_factor_b_weight) + (binding_factor_a * binding_factor_a_weight)) / (gamma_weight + delta_weight + epsilon_weight + zeta_weight + collusion_rating_weight + binding_factor_b_weight + binding_factor_a_weight)) * 10

        return collusion_score