from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)


def manhattan(state, goal):
    """TODO 1: Return Manhattan distance between two (row, column) tuples."""
    # Add the absolute row difference and the absolute column difference.
    diff_row= abs(state[0] - goal[0])
    diff_col= abs(state[1] - goal[1])
    return diff_row + diff_col


def astar(campus, start, goal):
    """TODO 2: Return SearchResult(path, expanded) for A* graph search."""
    # Use heapq as a priority queue and manhattan() as the heuristic.
    # Track best known g-costs and parent states in dictionaries.
    
    #keep track of costs and parents
    counts = count()
    #define frontier, g_costs, parents, and expanded
    frontier = []
    g_costs = {start: 0}
    parents = {start: None}
    expanded = 0

    #push the start state onto the frontier with its f-cost
    f_start = g_costs[start] + manhattan(start, goal)
    heapq.heappush(frontier, (f_start, next(counts), g_costs[start], start))

    #pop the state with the lowest f-cost from the frontier
    while frontier:
        f, insertion_number, g, state = heapq.heappop(frontier)
        
        if g != g_costs[state]:
            continue
        #if the popped state is the goal, reconstruct the path and return the result
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)

        expanded += 1

        #for each neighbor of the current state, calculate its g-cost and f-cost
        for action, successor in campus.neighbors(state):
            tentative_g = g + 1
            #if the successor has not been seen or the new g-cost is lower, update its g-cost and parent, and push it onto the frontier
            if successor not in g_costs or tentative_g < g_costs[successor]:
                g_costs[successor] = tentative_g
                parents[successor] = state
                f_cost = tentative_g + manhattan(successor, goal)
                heapq.heappush(frontier, (f_cost, next(counts), tentative_g, successor))
    #return a SearchResult with None path and the number of expanded states if the goal is not reachable
    return SearchResult(None, expanded)


def epsilon_greedy(q_values, state, actions, epsilon, rng):
    """TODO 3: Choose an action with epsilon-greedy exploration."""
    #
    if rng.random() < epsilon:
        return rng.choice(actions)

    #get q-values for the current state and all actions, 0.0 is used for unseen pairs.
    q_scores = [q_values.get((state, a), 0.0) for a in actions]
    #assign the maximum q-value
    max_q = max(q_scores)

    # collect all actions that have the highest q-value.
    best_actions = [a for a, q in zip(actions, q_scores) if q == max_q]

    # break ties randomly and return the chosen action.
    return rng.choice(best_actions)


def q_learning_update(q_values, state, action, reward, next_state, actions, alpha, gamma, terminal):
    """TODO 4: Update exactly one Q-table entry in place; return nothing."""
    current_q = q_values.get((state, action), 0.0)

    #if the next state is terminal, the target is just the reward, otherwise, it's the reward plus the discounted maximum Q-value of the next state.
    if terminal:
        target = float(reward)
    else:
        max_next_q = max(q_values.get((next_state, a), 0.0) for a in actions)
        target = reward + gamma * max_next_q

    #update the q-value for the current state-action pair using the learning rate alpha and the difference between the target and current q-value.
    q_values[(state, action)] = current_q + alpha * (target - current_q)
