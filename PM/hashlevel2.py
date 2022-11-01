from hash import sha_512


def swap_positions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def hash2(hashed_str: str, rounds: int = 1):
    hashed_str_list = list(hashed_str)
    length = len(hashed_str_list)
    nums = range(length)
    for i in range(rounds):
        for char, j in zip(hashed_str_list, nums):
            hashed_str_list = swapPositions(hashed_str_list, ord(char) ** 2 % length, j)
        # l2hash = l22hash
        # l22hash = ""
        print(''.join(map(str, hashed_str_list)), end="\n")
        hashed_str = ''.join(map(str, hashed_str_list))
        hashed_str_list = list(hashed_str)


if __name__ == "__main__":
    inp = input("enter string: ")
    innt = int(input("enter rounds: "))

    hashed = sha_512(inp)
    print("hashed: ", hashed)
    hash2(hashed, rounds=innt)
