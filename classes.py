class Game:
    def __init__(self, name, time_played, players, average_time, price):
        self.name = name
        self.time_played = time_played
        self.players = players
        self.average_time = average_time
        self.price = price

    def __str__(self):
        return f"The game {self.name}, was played "