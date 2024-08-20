# Assignment 2 - Student's Report

Please make sure that the report is no longer than 500 words.

## Author: Bikash Neupane (220245756)

## Complexity of the Problem 

The Connect Four game presents significant complexity due to the large branching factor, as each move potentially leads to a different game state. With a 7x6 board and multiple power-ups, the complexity increases exponentially, particularly when considering advanced game rules such as "pop-ups" and "power-ups." During implementation, I tested the performance of various AI agents. For example, the Minimax algorithm with Alpha-Beta pruning required significant computation time for deeper searches, especially as the number of legal moves expanded in the middle of the game. The Monte Carlo Tree Search (MCTS) algorithm also demonstrated performance challenges as it simulated multiple possible futures, increasing memory usage and computation time. The tradeoff between accuracy and speed was essential in determining the final AI techniques used.

## AI Techniques Considered

Several AI techniques were considered for the Connect Four game. These included Random Behavior, Minimax, Minimax with Alpha-Beta Pruning, Monte Carlo Tree Search (MCTS), and an Optimized Minimax using Transposition Tables. Random Behavior was excluded early due to its lack of strategic depth.

Minimax with Alpha-Beta pruning showed improved performance by reducing the search space, making it suitable for deeper searches with acceptable computation time. However, for even better performance, I implemented Optimized Minimax with Transposition Tables, which significantly reduced redundant calculations by storing previously computed states. This approach offered a good tradeoff between performance and speed, allowing deeper lookaheads while maintaining reasonable response times.

MCTS was also tested, as it allows exploration of potential moves through random playouts. MCTS performed well in dynamic scenarios, but its reliance on numerous simulations made it less efficient compared to the Optimized Minimax, especially in the late game where deep strategic moves are critical.

Ultimately, I selected the Optimized Minimax with Transposition Tables for the yellow player and MCTS for the red player. This combination balanced performance and computational speed, leveraging the strengths of both techniques​(connect_four_app)​(minimax_functions)​(agent_programs).

## Reflections

One of the primary challenges I faced was managing the balance between depth of search and computation time. Initial implementations of the basic Minimax algorithm were too slow for practical use in real-time gameplay, prompting me to explore Alpha-Beta pruning and later, Transposition Tables for optimization.

Another significant challenge was implementing and debugging the MCTS algorithm. Ensuring that the selection, expansion, simulation, and backpropagation phases were correctly integrated into the game environment was complex. Additionally, fine-tuning the time limits for the MCTS simulations to ensure fairness without sacrificing performance required considerable testing​(mcts_functions).

Finally, integrating advanced game mechanics like "power-ups" and "pop-ups" added to the complexity, as I had to modify both the environment and agent behaviors to handle these new rules effectively. Through careful planning and iterative testing, I was able to overcome these challenges and create a competitive AI system for Connect Four​(connect_four_environment)​(connect_four_player).