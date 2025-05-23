class Calc:
    def __init__(self, p, re, ra, to):
        self.p = p
        self.re = re
        self.ra = ra 
        self.to = to
        calc_score(p, re, ra, to)

def calc_score(p, re, ra, to):
    return calc_price(p) + calc_review(re) + calc_interest(ra, to)

def calc_price(price):
    if price >= 0 and price <= 5:
        return 5
    elif price > 5 and price <= 10:
        return 4
    elif price > 10 and price <= 20:
        return 3
    elif price > 20 and price <= 40:
        return 2
    elif price > 40 and price <= 60:
        return 1
    return 0

def calc_review(review):
    if review <= 100 and review >= 95:
        return 5
    elif review < 95 and review >= 90:
        return 4
    elif review < 90 and review >= 85:
        return 3
    elif review < 85 and review >= 80:
        return 2
    elif review < 80 and review >= 70:
        return 1
    return 0

def calc_interest(ranking, rank_total):
    rank = (ranking // rank_total) * 100
    if rank >= 0 and rank <= 10:
        return 5
    elif rank >= 10 and rank <= 25:
        return 4
    elif rank >= 25 and rank <= 40:
        return 3
    elif rank >= 40 and rank <= 65:
        return 2
    elif rank >= 80 and rank <= 80:
        return 1
    return 0