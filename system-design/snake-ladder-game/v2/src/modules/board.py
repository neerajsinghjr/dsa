class Board:

    def __init__(self, rows=10, cols=10, snakes=4, ladder=5):
        self.rows = rows
        self.cols = cols
        self.snakes = snakes
        self.ladder = ladder

    def initialize_game(self):
        board = self.create_board()
        jumpers = self.add_jumpers()
        players = self.add_player()

    def create_board(self) -> object:
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)


    def add_jumpers(self) -> object:
        pass

    def add_player(self) -> object:
        pass

    def __repr__(self) -> str:
        return f"Board(Rows: {self.rows}, cols: {self.cols})"
