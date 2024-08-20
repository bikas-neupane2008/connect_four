from une_ai.assignments import ConnectFourBaseEnvironment
from une_ai.models import GridMap

class ConnectFourEnvironment(ConnectFourBaseEnvironment):

    def __init__(self):
        super().__init__()

    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def get_legal_actions(game_state):
        # it must return the legal actions for the current game state
        legal_actions = []
        grid_map = game_state['game-board']

        for col in range(7):
            if not ConnectFourBaseEnvironment.is_column_full(grid_map, col):
                legal_actions.append(f'release-{col}')

        return legal_actions
    
    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def is_terminal(game_state):
        # it must return True if there is a winner or there are no more legal actions, False otherwise
        if ConnectFourBaseEnvironment.get_winner(game_state) is not None:
            return True

        legal_actions = ConnectFourEnvironment.get_legal_actions(game_state)
        return len(legal_actions) == 0
    
    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def payoff(game_state, player_colour):
        # it must return a payoff for the considered player ('Y' or 'R') in a given game_state
        winner = ConnectFourBaseEnvironment.get_winner(game_state)
        if winner == player_colour:
            return 1
        elif winner is not None:
            return -1
        else:
            return 0
        
    # TODO
    # static method
    # Note: in a static method you do not have access to self
    def simulate_move(game_state, move, player_colour):
        # it must return new state
        new_state = ConnectFourBaseEnvironment.transition_result(game_state, move)

        if 'power-up-Y' not in new_state:
            new_state['power-up-Y'] = game_state.get('power-up-Y', None)
        if 'power-up-R' not in new_state:
            new_state['power-up-R'] = game_state.get('power-up-R', None)

        return new_state
