# Data Model Methods(Double underscore methods) are used to implement some behaviour
# Using underscore methods on such top-level syntax(like objects), we replicate basic low-level syntax


class Polynomial:
    def __init__(self, *coefs):
        self.coefs = coefs

    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coefs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coefs, other.coefs)))

    def __len__(self):
        return len(self.coefs)


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(2, 3, 4)
