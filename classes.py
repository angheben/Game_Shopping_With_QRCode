class Game:
    def __init__(self, name, time_played, players, price):
        self.name = name
        self.time_played = time_played
        self.players = players
        self.price = price

    def __str__(self):
        return f"The game {self.name}, was played {self.time_played} hours by his users, there are {self.players} " \
               f"players and it costs around US$ {self.price}!"
