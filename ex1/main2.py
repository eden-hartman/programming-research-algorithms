

def four_neighbors_function(node: any) -> list:
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def breadth_first_search(start=(0, 0), end=(2, 2), neighbors_function=four_neighbors_function):
    path = [start]
    history = {start: 0}
    done = False
    curr_ind = 0
    while not done:
        curr = path[curr_ind]
        neighbors = four_neighbors_function(curr)
        for neighbor in neighbors:
            if neighbor == end:
                path.append(neighbor)
                history[neighbor] = curr
                done = True
                break
            else:
                if neighbor not in path:
                    path.append(neighbor)
                    history[neighbor] = curr
        curr_ind += 1

    done = False
    curr = path[-1]
    short_path = [curr]
    while not done:
        curr = history[curr]
        if curr == 0:
            done = True
            break
        short_path.append(curr)

    print(short_path)


if __name__ == "__main__":
    breadth_first_search()