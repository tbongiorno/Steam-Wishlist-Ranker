from flask import Flask, render_template
import requests
import datetime

STEAM_API_KEY = "my_api_key"
STEAM_USER_ID = "76561199515048875"

app = Flask(__name__)
app.config['DEBUG'] = True

def get_game_data(game_id):
    url=f"https://store.steampowered.com/api/appdetails?appids={game_id}"
    response = requests.get(url)
    game_data = response.json()

    if game_data.get(str(game_id), {}).get('success'):
        details = game_data[str(game_id)]['data']
        return{
            "name":details.get("name"),
            "image":details.get("header_image"),
            "price":details.get("price_overview", {}).get("final_formatted", "Not Availiable"),
            "all_time_reviews":details.get("reviews", {}).get("total", "No Reviews"),
            "recent_reviews":details.get("reviews", {}).get("recent", "No Recent Reviews"),
        }
    return None


@app.route("/")
def site():
    rows = 2
    game_ids = [12345, 67890, 13579]
    games = []
    for game_id in game_ids:
        game_data = get_game_data(game_id)
        if game_data:
            games.append(game_data)
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