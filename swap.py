class instru(object):
    def __init__(self, rates):
        self.rates =rates
    def floating(self):
        return 1
    def fixed(self, rates):
        return sum([1/((1+rate)**t) for t,rate in enumerate(rates)])
    def annuity(self):

    def bond(self):
        return self.fixed(rates)

class instrument(legs):
    def __init__(self, rates):
        self.rates = rates
    def simple_bond(self):
        return super(simple_bond, self).fixed(self.rates)