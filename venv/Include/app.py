from flask import Flask, render_template
#import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def site():
    rows = 2
    return render_template('site.html', numRows=rows)
if __name__ == "__main__":
    app.run(debug=True)

'''
@app.route("/")
def page():
    date = datetime.date.today().strftime("%B %d, %Y")
    return render_template('page.html', date=date)



#Define p, a, re, and ra
def calc_score(p, a, re, ra):
    score = calc_price(p) + calc_review(a, re) + calc_rank(ra)
    print(score)

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

def calc_review(all_time, recent):
    avg = (all_time + recent) / 2
    if avg <= 100 and avg >= 95:
        return 5
    elif avg < 95 and avg >= 90:
        return 4
    elif avg < 90 and avg >= 85:
        return 3
    elif avg < 85 and avg >= 80:
        return 2
    elif avg < 80 and avg >= 70:
        return 1
    return 0

def calc_rank(ranking, rank_total):
    rank = (ranking // rank_total) * 100
    if rank > 0 and rank <= 10:
        return 5
    elif rank > 10 and rank <= 25:
        return 4
    elif rank > 25 and rank <= 40:
        return 3
    elif rank > 40 and rank <= 65:
        return 2
    elif rank > 65 and rank <= 80:
        return 1
    return 0'

'''