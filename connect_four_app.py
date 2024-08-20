from une_ai.assignments import ConnectFourGame
from connect_four_environment import ConnectFourEnvironment
from connect_four_player import ConnectFourPlayer
from agent_programs import random_behaviour, human_agent, intelligent_behaviour, intelligent_behaviour_alpha_beta, monte_carlo_behaviour, optimised_minimax_behaviour
from connect_four_ttable import ConnectFourTTable

if __name__ == '__main__':
    # Change these two lines to instantiate players with proper
    # agent programs, as per your tests
    yellow_player = ConnectFourPlayer('Y', optimised_minimax_behaviour)
    red_player = ConnectFourPlayer('R', monte_carlo_behaviour)

    # DO NOT EDIT THESE LINES OF CODE!!!
    game_environment = ConnectFourEnvironment()
    game_environment.add_player(yellow_player)
    game_environment.add_player(red_player)

    game = ConnectFourGame(yellow_player, red_player, game_environment)