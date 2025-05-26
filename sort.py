class Sort:
    def sort_games(games):
        #SORT BY LARGEST SCORE AT TOP, IF TIE THEN BY INTEREST, IF TIE THEN BY PRICE, IF TIE, THEN BY NAME
        for i in range(len(games) - 1, 0, -1):
            switch = False
            for j in range(i):
                if compare_games(games[j], games[j+1]):
                    games[j], games[j + 1] = games[j + 1], games[j]
                    switch = True
            if not switch:
                break

        return games        

def compare_games(game_1, game_2):
    if game_1["score"] > game_2["score"]:
        return True
    elif game_1["score"] < game_2["score"]:
        return False
    
    if game_1["interest"] > game_2["interest"]:
        return True
    elif game_1["interest"] < game_2["interest"]:
        return False
    
    if game_1["price"] > game_2["price"]:
        return True
    elif game_1["price"] < game_2["price"]:
        return False
    
    if game_1["title"][0] < game_2["title"][0]:
        return True
    else:
        return False