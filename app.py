from flask import Flask, render_template
import datetime
import json
# import requests

import calc
from add import add_game
from sort import sort_games

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")                 
def site():
    #IF WISHLIST DOESN'T EXIST, CREATE JSON FILE storage.json
    #ELSE, ADD ALL DATA IN storage.json
    #WHEN ADDING DATA, USE calc.py TO FIND SCORE FOR EACH GAME AND STORE THAT VALUE
    try:
        with open("storage.json", "r") as file:
            games_data = json.load(file)
    except FileNotFoundError:
        games_data = json


    #ADD GAME TO JSON FROM INPUT
    new_game = input("Please Enter the Name of the Game You Wish to Enter: ")
    interest = int(input("Please Enter your Level of Interest in the game you've just Entered from 1-10, slightly to highly interested:"))
    
    new_data = add_game(new_game, interest)
    games_data.update(new_data)

    with open("storage.json", "w") as file:
        json.dump(games_data, file, indent=4)


    #SORT WISHLIST WITH sort.py
    games_data = sort_games(games_data)



    return render_template("site.html", games=games_data)


@app.route("/page")                 
def page():
    date = datetime.date.today().strftime("%B %d, %Y")
    return render_template('page.html', date=date)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

