class ShillScore:
    
    def __init__(self, alpha_rating, beta_rating, gamma_rating, delta_rating, epsilon_rating, zeta_rating):
        # ratings
        self.alpha_rating = alpha_rating
        self.beta_rating = beta_rating
        self.gamma_rating = gamma_rating
        self.delta_rating = delta_rating
        self.epsilon_rating = epsilon_rating
        self.zeta_rating = zeta_rating
        # weights
        self.alpha_weight = 9
        self.beta_weight = 1
        self.gamma_weight = 7
        self.delta_weight = 3
        self.epsilon_weight = 3
        self.zeta_weight = 1
    
    def calculate_shill_score(self):
        shill_score = (((self.alpha_weight * self.alpha_rating) + (self.beta_weight * self.beta_rating) + (self.gamma_weight * self.gamma_rating) + (self.delta_weight * self.delta_rating) + (self.epsilon_weight * self.epsilon_rating) + (self.zeta_weight * self.zeta_rating)) / (self.alpha_weight + self.beta_weight + self.gamma_weight + self.delta_weight + self.epsilon_weight + self.zeta_weight)) * 10

        return shill_score
    
    def isAShill(self):
        shill_score = self.calculate_shill_score()

        if shill_score > 7:
            print('this is a shill bidder')
        else:
            print('this is a legal bidder')

