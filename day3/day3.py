def create_map(filename):
    map = []

    with open(filename) as f:
        for entry in f.readlines():
            map.append((entry.strip()))

    return map

def tree_found(map, hill_x, hill_y):
    # each string in list is 31 char long
    true_x = hill_x % 31
    return map[hill_y][true_x] == '#'


def move_down_slope(right_increment: int, down_increment: int, map: list):
    right_coord = 0
    down_coord = 0
    tree_count = 0

    while down_coord < len(map):
        if tree_found(map, right_coord, down_coord):
            tree_count += 1
        right_coord += right_increment
        down_coord += down_increment

    return tree_count


if __name__ == '__main__':
    map = create_map('input.txt')

    # part 1
    pt_one_tree_count = move_down_slope(3, 1, map)
    print(f'the answer to part one is: {pt_one_tree_count}')

    # part 2
    pt_two_tree_count = 1
    for (a, b) in ((1,1),(3,1),(5,1),(7,1),(1,2)):
        pt_two_tree_count *= move_down_slope(a, b, map)
    print(f'the answer to part two is: {pt_two_tree_count}')