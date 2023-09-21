class Jump:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        jumper = "LADDER" if self.start < self.end else "SNAKE"
        return f"{jumper}(From: {self.start}, To: {self.end})"
