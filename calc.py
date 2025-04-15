from flask import Flask, render_template, url_for
#import requests
#import random
import datetime
    
def save_wishlist(wishlist):
    wishlist_data = []
    for game in wishlist:
        #enumerate(wishlist, start=1)
        #game_id = game['id']
        #game_details = get_game_details(game_id)
        #if game_details:
        game_data = {
            'name': game['name'],
           'price': game['price'],
            'all_time_reviews': game['all_time_reviews'],
            'recent_reviews': game['recent_reviews'],
            'image': game['image'],
            'interest': game['interest']
        }
        wishlist_data.append(game_data)
    
    return wishlist_data


'''
def get_game_details(game_id):
    
    url = f'https://store.steampowered.com/api/appdetails?appids={game_id}'
    response = requests.get(url)
    data = response.json()

    if str(game_id) in data and data[str(game_id)]['success']:
        game_data = data[str(game_id)]['data']
        game_details = {
            'name': game_data['name'],
            'image': game_data['header_image'],
            'all_time_reviews': game_data['reviews']['all_time'],
            'recent_reviews': game_data['reviews']['recent'],
            'price': game_data.get('price_overview', {}).get('final_formatted', 'N/A')
        }
        return game_details
    else:
        return None
 

def get_steam_wishlist(user_id, api_key):
    url = f'https://api.steampowered.com/ISteamUser/RequestUserStats/v1/?steamid={user_id}&key={api_key}'

    response = requests.get(url)
    data = response.json()

    if 'wishlist' in data:
        return data['wishlist']
    else:
        print("Could not retrieve wishlist data.")
        return []
'''

def sort_games(games):
    for game in games:
        game["score"] = calc_price(game["price"]) + calc_review(game["all_time_reviews"], game["recent_reviews"]) + calc_interest(game["interest"], len(games))
        
    n = len(games)
    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if games[j]["score"] < games[j - 1]["score"]:
                games[j], games[j + 1] = games[j + 1], games[j]
                sorted = False
        if sorted:
            break
    return games
    

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

calc = Flask(__name__)
calc.config['DEBUG'] = True


@calc.route("/page")                 
def page():
    date = datetime.date.today().strftime("%B %d, %Y")
    return render_template('page.html', date=date)

if __name__ == "__main__":
    calc.run(host="0.0.0.0", port=5000)

@calc.route("/")                 
def site():
    game_1 = {
        "name": "Hades 2",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1145350/header.jpg?t=1741889622",
        "interest": 1,
        "price": 30.00,
        "all_time_reviews": 94,
        "recent_reviews": 95
    }
    game_2 = {
        "name": "Signalis",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1262350/header.jpg?t=1704064951",
        "interest": 8,
        "price": 20.00,
        "all_time_reviews": 96,
        "recent_reviews": 96
    }
    game_3 = {
        "name": "Star of Providence",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/603960/header.jpg?t=1740062273",
        "interest": 18,
        "price": 15.00,
        "all_time_reviews": 96,
        "recent_reviews": 93
    }
    game_4 = {
        "name": "Cult of the Lamb",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1313140/header.jpg?t=1741724183",
        "interest": 27,
        "price": 12.50,
        "all_time_reviews": 95,
        "recent_reviews": 96
    }
    game_5 = {
        "name": "Devil May Cry V",
        "image": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/601150/header.jpg?t=1701395090",
        "interest": 35,
        "price": 7.50,
        "all_time_reviews": 96,
        "recent_reviews": 95
    }
    
    #api_key = "29F8D86BEF0EE4C4675EDA733F43337A"
    #user_id = "76561199515048875"
    #wishlist = get_steam_wishlist(user_id, api_key)
    
    wishlist = [game_1, game_2, game_3, game_4, game_5]

    if wishlist:
        games = save_wishlist(wishlist)
    else:
        print(f"No Wishlist Data Found")
    
    games = sort_games(wishlist)

    with calc.test_request_context():
        url = url_for('site')

    return render_template("site.html", games=games, url=url)
