"""
	Playground :
	Playground is board which is also of custom size.

	It includes rest of the game objects as well
"""

class Playground:

	def __init__(self, players, dice, snakes, ladders, boardsize, player_position):
		self.players = players
		self.dice = dice 
		self.snakes = snakes
		self.ladders = ladders
		self.boardsize = boardsize
		# Mapped by Dict with Player Id {id : position};
		self.player_position = player_position


	def game_start(self):
		# GAME START;;
		while(len(self.players) > 1):
			player = self.players.popleft()
			player_id = player.id
			player_name = player.name
			print(f"{player_name}'s Turn  to roll the dice...")
			flag = input(f"{player_name}, Roll Dice")
			cur_position = self.player_position.get(player_id)
			dice_roll = self.dice.roll_dice()
			next_position = cur_position + dice_roll
			if next_position >= self.boardsize:
				print(f"Hurray, {player_name} Won the Game!!!")
			else:
				# Case1: Snake Bitten
				for snake in self.snakes:
					if snake.start == next_position:
						print(f"{player_name} is bitten by snake")
						print(f"Dragged From {next_position} -> {snake.end}")
						next_position = snake.end
				
				# Case2: Ladder Climb
				for ladder in self.ladders:
					if ladder.end == next_position:
						print(f"{player_name} is climbed up ladder")
						print(f"Climbed up From {next_position} -> {ladder.start}")
						next_position = ladder.start
				
				print(f"Next Position : {next_position}")
				self.player_position[player_id] = next_position
			
				self.players.append(player)
