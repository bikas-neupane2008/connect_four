import traceback
import random
import time

from une_ai.assignments import ConnectFourGame
from connect_four_environment import ConnectFourEnvironment
from une_ai.models import GraphNode, MCTSGraphNode
from minimax_functions import minimax, minimax_alpha_beta, optimised_minimax
from mcts_functions import mcts

# Initialize the transposition table
tt = ConnectFourTTable()

# A simple agent program choosing actions randomly
def random_behaviour(percepts, actuators):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()

    if not ConnectFourEnvironment.is_terminal(game_state):
        legal_moves = ConnectFourEnvironment.get_legal_actions(game_state)
        try:
            tic = time.time()  # Start timing
            action = random.choice(legal_moves)
            toc = time.time()  # End timing
            print("[Random (player {0})] Elapsed (sec): {1:.6f}".format(game_state['player-turn'], toc-tic))
        except IndexError as e:
            print("You may have forgotten to implement the ConnectFourEnvironment methods, or you implemented them incorrectly:")
            traceback.print_exc()
            return []

        return [action]
    else:
        return []
    
# An agent program to allow a human player to play Connect Four
# see the assignment's requirements for a list of valid keys
# to interact with the game
def human_agent(percepts, actuators):
    action = ConnectFourGame.wait_for_user_input()
    return [action]

# TODO
# complete the agent program to implement an intelligent behaviour for
# the agent player
def intelligent_behaviour(percepts, actuators, max_depth=4):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()

    if not ConnectFourEnvironment.is_terminal(game_state):
        state_node = GraphNode(game_state, None, None, 0)
        tic = time.time()
        _, best_move = minimax(state_node, game_state['player-turn'], max_depth)
        toc = time.time()
        print("[Minimax (player {0})] Elapsed (sec): {1:.6f}".format(game_state['player-turn'], toc-tic))
        if best_move is not None:
            return [best_move]
    
    return []

def intelligent_behaviour_alpha_beta(percepts, actuators, max_depth=4):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()

    if not ConnectFourEnvironment.is_terminal(game_state):
        state_node = GraphNode(game_state, None, None, 0)
        tic = time.time()
        _, best_move = minimax_alpha_beta(state_node, game_state['player-turn'], float("-Inf"), float("+Inf"), max_depth)
        toc = time.time()
        print("[Minimax Alpha-Beta (player {0})] Elapsed (sec): {1:.6f}".format(game_state['player-turn'], toc-tic))
        if best_move is not None:
            return [best_move]
    
    return []

def monte_carlo_behaviour(percepts, actuators, max_time=1):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()

    if not ConnectFourEnvironment.is_terminal(game_state):
        tic = time.time()
        root_node = MCTSGraphNode(game_state, None, None)
        best_move = mcts(root_node, game_state['player-turn'], max_time)
        toc = time.time()
        print("[MCTS (player {0})] Elapsed (sec): {1:.6f}".format(game_state['player-turn'], toc-tic))
        if best_move is not None:
            return [best_move]
    
    return []

def optimised_minimax_behaviour(percepts, actuators, max_depth=4):
    try:
        game_state = {
            'game-board': percepts['game-board-sensor'],
            'power-up-Y': percepts['powerups-sensor']['Y'],
            'power-up-R': percepts['powerups-sensor']['R'],
            'player-turn': percepts['turn-taking-indicator']
        }
    except KeyError as e:
        game_state = {}
        print("You may have forgotten to add the necessary sensors:")
        traceback.print_exc()

    if not ConnectFourEnvironment.is_terminal(game_state):
        state_node = GraphNode(game_state, None, None, 0)
        tic = time.time()
        _, best_move = optimised_minimax(state_node, game_state['player-turn'], tt, max_depth)
        toc = time.time()
        print("[Optimized Minimax (player {0})] Elapsed (sec): {1:.6f}".format(game_state['player-turn'], toc-tic))
        if best_move is not None:
            return [best_move]
    
    return []