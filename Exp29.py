#!/usr/bin/env python3
"""
Simulate Keccak lane permutation (π) to see when capacity lanes
(indices 16..24) become nonzero starting from nonzero lanes 0..15.

Lanes are indexed as idx = x + 5*y for x,y in {0..4}.
π maps (x,y) -> (y, (2*x + 3*y) mod 5).
"""

from math import isqrt

def idx_to_xy(idx):
    x = idx % 5
    y = idx // 5
    return x, y

def xy_to_idx(x, y):
    return x + 5 * y

def pi_map(idx):
    x, y = idx_to_xy(idx)
    x_new = y
    y_new = (2 * x + 3 * y) % 5
    return xy_to_idx(x_new, y_new)

def simulate_activation(initial_nonzero, capacity_lanes):
    # activation_step[i] = step when lane i first became nonzero (None if not yet)
    activation_step = {i: None for i in range(25)}
    for i in initial_nonzero:
        activation_step[i] = 0

    current = set(initial_nonzero)
    visited = set(initial_nonzero)
    step = 0
    cap_activation = {}

    # keep going until every capacity lane has been seen nonzero at least once
    while not capacity_lanes.issubset(visited):
        step += 1
        # apply π: content from lane i moves to lane pi_map(i)
        current = {pi_map(i) for i in current}
        for lane in current:
            if activation_step[lane] is None:
                activation_step[lane] = step
        visited |= current
        for lane in capacity_lanes.intersection(current):
            if lane not in cap_activation:
                cap_activation[lane] = step

        # safety: if loop grows too long (shouldn't for 25-lane permutation), break
        if step > 100:
            raise RuntimeError("Exceeded 100 steps - something is wrong.")

    return activation_step, cap_activation, step

def permutation_cycles():
    seen = set()
    cycles = []
    for i in range(25):
        if i in seen:
            continue
        cyc = []
        cur = i
        while cur not in cyc:
            cyc.append(cur)
            cur = pi_map(cur)
        cycles.append(cyc)
        seen |= set(cyc)
    return cycles

def main():
    # initial condition: lanes 0..15 are nonzero at step 0
    initial_nonzero = set(range(16))
    capacity_lanes = set(range(16, 25))  # lanes 16..24

    activation_step, cap_activation, total_steps = simulate_activation(initial_nonzero, capacity_lanes)

    print(f"\nAll capacity lanes (indices 16..24) became nonzero by step {total_steps}.\n")
    print("Activation steps for capacity lanes (index: step):")
    for lane in sorted(capacity_lanes):
        print(f"  lane {lane}: step {activation_step[lane]}")

    print("\nFull activation table (lane: first_step_nonzero):")
    for i in range(25):
        print(f"  lane {i:2d}: {activation_step[i]}")

    print("\nπ permutation cycles (lane indices):")
    cycles = permutation_cycles()
    for cyc in cycles:
        print(cyc)

if __name__ == "__main__":
    main()

