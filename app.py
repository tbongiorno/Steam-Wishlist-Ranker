'''
from flask import Flask, render_template
import requests
import datetime

STEAM_API_KEY = "29F8D86BEF0EE4C4675EDA733F43337A"
STEAM_USER_ID = "76561199515048875"

app = Flask(__name__)
app.config['DEBUG'] = True

def get_game_data(game_id):
    
    return


@app.route("/")
def site():
    rows=2
    return render_template('site.html', numRows=rows)
if __name__ == "__main__":
    app.run(debug=True)
'''