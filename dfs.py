def print_state(step, peg_a, peg_b, peg_c, total_steps):
    label = " (Start State)" if step == 0 else (" (Goal State reached!)" if step == total_steps else "")
    print(f"Step {step}{label}:")
    print(f"  [{peg_a}, {peg_b}, {peg_c}]\n")

def tower_of_hanoi_dfs(n, source, target, auxiliary, pegs, tracking):
    if n == 0:
        return

    tower_of_hanoi_dfs(n - 1, source, auxiliary, target, pegs, tracking)

    disk = pegs[source].pop()
    pegs[target].append(disk)
    tracking["step"] += 1
    
    print_state(tracking["step"], pegs['A'], pegs['B'], pegs['C'], tracking["total"])

    tower_of_hanoi_dfs(n - 1, auxiliary, target, source, pegs, tracking)

if __name__ == "__main__":
    num_disks = 3
    total_moves = 2**num_disks - 1
    
    pegs = {
        'A': list(range(num_disks, 0, -1)),
        'B': [],
        'C': []
    }
    
    tracking = {"step": 0, "total": total_moves}
    

    print_state(tracking["step"], pegs['A'], pegs['B'], pegs['C'], tracking["total"])
    
    tower_of_hanoi_dfs(num_disks, 'A', 'C', 'B', pegs, tracking)

