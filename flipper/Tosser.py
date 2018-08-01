import random

class Tosser:
    def __init__(self, castee):
        self.castee = castee

    def toss(self, ntoss=1):
        result = []
        for x in range(0, ntoss):
            result.append(random.choice(self.castee.SIDES))
        return result


