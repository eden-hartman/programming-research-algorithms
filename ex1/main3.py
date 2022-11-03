
import copy


def sort_rec(arr):
    # if (type(arr) is not dict) or (type(arr) is not list) or (type(arr) is not tuple):
    if type(arr) is dict:
        arr = {k: v for k, v in sorted(arr.items(), key=lambda item: str(item[0]))}
        print("in" + str(arr))
        for a in arr.keys():
            arr[a] = sort_rec(arr[a])
    elif type(arr) is list:
        arr = arr = {v for v in sorted(arr, key=lambda item: str(item))}
        for a in arr:
            a = sort_rec(a)
    # print("in2 " + str(arr))
    return arr


def print_sort(x):
    y = copy.deepcopy(x)
    y = sort_rec(y)
    print(y)


if __name__ == "__main__":
    # ar = {"a": 5, "c": 6, "b": [1, ['f', 'a', 2], 2, 4]}
    ar = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print(ar)
    print_sort(ar)
    print(ar)