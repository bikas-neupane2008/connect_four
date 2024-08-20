import random
from une_ai.models import TTable


class ConnectFourTTable(TTable):

    def __init__(self, saving_directory='./transposition-tables/', instance_id=None, verbose=False):
        super().__init__(saving_directory, instance_id, verbose)

    def generate_zobrist_table(self):
        random_int = lambda: random.randint(0, pow(2, 64))

        markers = ['Y', 'R']  # Connect Four uses yellow ('Y') and red ('R') markers
        board_width = 7  # Connect Four board has 7 columns
        board_height = 6  # Connect Four board has 6 rows
        table = {}

        for i in range(board_width):
            for j in range(board_height):
                for k in markers:
                    table[f"{i}-{j}-{k}"] = random_int()

        table["player-turn-Y"] = random_int()
        table["player-turn-R"] = random_int()

        return table

    def compute_hash(self, state):
        zobrist_table = self.get_zobrist_table()

        player = state['player-turn']
        h = 0

        # XOR the hash with the player turn
        h ^= zobrist_table[f'player-turn-{player}']

        game_board = state['game-board']
        for i in range(game_board.get_width()):
            for j in range(game_board.get_height()):
                board_value = game_board.get_item_value(i, j)
                if board_value is not None:
                    # XOR the hash with the corresponding position and marker
                    h ^= zobrist_table[f"{i}-{j}-{board_value}"]

        return str(h)
