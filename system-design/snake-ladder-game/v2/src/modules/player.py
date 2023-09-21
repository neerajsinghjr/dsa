class Player:

    def __init__(self, pid, name, location):
        self.pid = pid
        self.name = name
        self.location = location

    def get_player_id(self):
        return self.pid

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def __repr__(self):
        return (f"Player("
                f"PID: {self.pid}, "
                f"name={self.name}, "
                f"location={self.location})")