# Eagle Delivery: Project 1 starter

This is our project 1 that focuses on search and reinforcement learning. Edit this readme file with your own project introduction and run commands for your GitHub commits.

## Requirements

Use Python 3.9+.

## What already works

```bash
python3 run_project.py show
python3 run_project.py search --algorithm bfs --start S --goal W
python3 run_project.py search --algorithm bfs --map maps/emu_detour.txt --start S --goal W
python3 run_project.py random --start S --goal W --seed 0
python3 examples/interaction_demo.py
python3 -m unittest tests.test_environment -v
```

On `emu_campus.txt`, BFS from S to W should return path length **18** and **67**
expanded nodes, The path visualization uses `o`.

## Your implementation tasks

Edit only these four functions in `agents.py` for the required algorithms:

1. `manhattan(state, goal)`
2. `astar(campus, start, goal)`
3. `epsilon_greedy(q_values, state, actions, epsilon, rng)`
4. `q_learning_update(q_values, state, action, reward, next_state, actions, alpha, gamma, terminal)`


After TODOs 1-2:

```bash
python3 -m unittest tests.test_student.SearchTests -v
python3 run_project.py search --algorithm astar --start S --goal W
```

After TODOs 3-4:

```bash
python3 -m unittest tests.test_student.LearningTests -v
python3 -m unittest discover -v
python3 run_project.py train --start S --goal W --output results/baseline_SW
```



python3 -m unittest tests.test_student.SearchTests -v
python3 -m unittest tests.test_student.LearningTests -v

# Baseline Map Searches (emu_campus.txt)
python3 run_project.py search --algorithm bfs   --map maps/emu_campus.txt --start S --goal W
python3 run_project.py search --algorithm astar --map maps/emu_campus.txt --start S --goal W

python3 run_project.py search --algorithm bfs   --map maps/emu_campus.txt --start L --goal D
python3 run_project.py search --algorithm astar --map maps/emu_campus.txt --start L --goal D

python3 run_project.py search --algorithm bfs   --map maps/emu_campus.txt --start H --goal P
python3 run_project.py search --algorithm astar --map maps/emu_campus.txt --start H --goal P

# Detour Map Searches (emu_detour.txt)
python3 run_project.py search --algorithm bfs   --map maps/emu_detour.txt --start S --goal W
python3 run_project.py search --algorithm astar --map maps/emu_detour.txt --start S --goal W

# Custom Map Search (my_campus.txt)
python3 run_project.py search --algorithm astar --map maps/my_campus.txt --start S --goal W 

# Delivery Requirements (not custom)
python3 run_project.py train --map maps/emu_campus.txt --start S --goal W --output results/baseline_SW
python3 run_project.py train --map maps/emu_campus.txt --start L --goal D --output results/baseline_LD
python3 run_project.py train --map maps/emu_campus.txt --start H --goal P --output results/baseline_HP

# Custom Map Experiments (Varying Exploration Parameter Epsilon)
python3 run_project.py train --map maps/my_campus.txt --start S --goal W --epsilon 0.05 --output results/custom_e005
python3 run_project.py train --map maps/my_campus.txt --start S --goal W --epsilon 0.20 --output results/custom_e020
python3 run_project.py train --map maps/my_campus.txt --start S --goal W --epsilon 0.50 --output results/custom_e050

# Summarize the results
python3 summarize_results.py results/baseline_SW
python3 summarize_results.py results/baseline_LD
python3 summarize_results.py results/baseline_HP
python3 summarize_results.py results/custom_e005
python3 summarize_results.py results/custom_e020
python3 summarize_results.py results/custom_e050
