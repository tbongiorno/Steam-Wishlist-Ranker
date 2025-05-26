#import requests
import json

class Add:
    def add_game(ng, i):
        #Search RAWG API for game data from title (ng parameter)
        #Search isthereanydeal API for price details
        #Add the game with all necessary parameters to data

        #Get details of the game
        # ENDPOINT_RAWG = f"https://api.rawg.io/api/games/{i}"
        # API_KEY_RAWG = "" #NEED TO SET UP
        # CONFIG_RAWG = {
        #     "id": f"{i}"
        # }
        # response_rawg = requests.get(url=ENDPOINT_RAWG, json= ,auth=)
        # data = response_rawg.json()


        #Prices
        # ENDPOINT_DEAL = "https://api.isthereanydeal.com/games/prices/v3"
        # API_KEY_DEAL = "" #NEED TO SET UP
        # REQUEST_BODY_SCHEMA = [f"{i}"]
        # CONFIG_DEAL = {
        #       "country": "US",
        #       "deals": False,
        #       "vouchers": False,
        #       "capacity": 3,
        #       "shops": "steam,gog,epic",
        # }
        # response_deal = requests.post(url=ENDPOINT_DEAL, json= ,auth= )

        # game = {
        #     "name": ng,
        #     "image": data["background_image"],
        #     "price": "",
        #     "on_sale": "",
        #     "reviews": "",
        #     "interest": "",
        # }

        # return game
        return 0