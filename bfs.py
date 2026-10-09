from collections import deque
import copy


def get_next_states(state):
  """Generates all legal next states using list copies."""
  next_states = []

  # Look at every source peg (0, 1, or 2)
  for i in range(3):
    if not state[i]:
      continue  # Nothing to move

    # Get the top disk (the last item in the array list)
    disk = state[i][-1]

    # Look at every destination peg
    for j in range(3):
      if i == j:
        continue

      # Valid move if destination peg is empty or its top disk is larger
      if not state[j] or state[j][-1] > disk:
        # Create a deep copy of the array list structure
        new_state = copy.deepcopy(state)

        # Array List Operations: Pop from source, append to destination
        moved_disk = new_state[i].pop()
        new_state[j].append(moved_disk)

        next_states.append((new_state, (i, j, moved_disk)))

  return next_states


def bfs_tower_of_hanoi(n):
  # Initial State: 3 disks on Peg 0, others empty. Represented as nested array lists.
  # Larger numbers represent larger disks.
  start_state = [list(range(n, 0, -1)), [], []]

  # Goal State: All disks moved to Peg 2
  goal_state = [[], [], list(range(n, 0, -1))]

  # Queue holds: (current_state_array, path_history_of_states)
  # Convert to tuple inside 'visited' because lists aren't hashable
  queue = deque([(start_state, [start_state])])
  visited = {tuple(tuple(peg) for peg in start_state)}

  peg_names = {0: 'A', 1: 'B', 2: 'C'}

  while queue:
    current_state, path = queue.popleft()

    if current_state == goal_state:
      return path

    for next_state, move in get_next_states(current_state):
      # Hash check using an immutable representation of the nested array lists
      state_signature = tuple(tuple(peg) for peg in next_state)

      if state_signature not in visited:
        visited.add(state_signature)
        queue.append((next_state, path + [next_state]))

  return []


if __name__ == '__main__':
  n_disks = 3
  solution_path = bfs_tower_of_hanoi(n_disks)

 


  for step, state in enumerate(solution_path):
    if step == 0:
      print(f'Step {step} (Start State):')
    elif step == len(solution_path) - 1:
      print(f'Step {step} (Goal State reached!):')
    else:
      print(f'Step {step}:')

    # Directly prints the raw list-of-lists arrays
    print(f'  {state}\n')

