import random
import time
import math
from connect_four_environment import ConnectFourEnvironment as gm


def selection_policy(node, target_player):
    successors = node.get_successors()
    best_uct_score = 0
    best_node = None
    for s in successors:
        if s.n() > 0:
            uct = (s.wins(target_player) / s.n()) + math.sqrt(2) * math.sqrt(math.log(s.get_parent_node().n()) / s.n())
            if best_node is None or uct > best_uct_score:
                best_uct_score = uct
                best_node = s
        else:
            return s

    return best_node


def random_playout(initial_node):
    current_playout_state = initial_node.get_state()
    while not gm.is_terminal(current_playout_state):
        possible_moves = gm.get_legal_actions(current_playout_state)
        action = random.choice(possible_moves)
        current_playout_state = gm.simulate_move(current_playout_state, action, gm.turn(current_playout_state))

    return gm.get_winner(current_playout_state)


def mcts(root_node, target_player, max_time=1):
    start_time = time.time()

    while (time.time() - start_time) < max_time:
        current_node = root_node
        while not gm.is_terminal(current_node.get_state()) and not current_node.is_leaf_node():
            current_node = selection_policy(current_node, target_player)

        selected_node = current_node
        legal_moves = gm.get_legal_actions(selected_node.get_state())
        for a in legal_moves:
            if not selected_node.was_action_expanded(a):
                successor_state = gm.simulate_move(selected_node.get_state(), a, gm.turn(selected_node.get_state()))
                selected_node.add_successor(successor_state, a)

        winner = random_playout(selected_node)
        if winner is None:
            winner = target_player

        selected_node.backpropagate(winner)

    best_node = None
    max_wins = 0
    for successor in root_node.get_successors():
        if best_node is None or successor.wins(target_player) / successor.n() > max_wins:
            best_node = successor
            max_wins = successor.wins(target_player) / successor.n()

    return best_node.get_action()
