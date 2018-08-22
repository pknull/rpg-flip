import random

class Tosser:
    def __init__(self, castee):
        self.castee = castee

    def toss(self, ntoss=1, unique=False):
        if unique:
            if ntoss > len(self.castee.SIDES):
                result = self.castee.SIDES
            else:
                result = random.sample(self.castee.SIDES, ntoss)
        else:
            result = []
            for x in range(0, ntoss):
                result.append(random.choice(self.castee.SIDES))
        return result


