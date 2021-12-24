class Delta(object):

    def __init__(self, transition):
        self.transition = transition

    def next(self, state, symbol):
        return self.transition[state][symbol]
