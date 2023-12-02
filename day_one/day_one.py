from pathlib import Path


def workin_fnc(line, lst) -> None:
    """Working function to use in both puzzle calls"""
    v1, v2 = "", ""
    t_line = list(line)
    for char in t_line:
        if char.isdigit():
            v1 = char
            break
    t_line.reverse()
    for char in t_line:
        if char.isdigit():
            v2 = char
            break
    lst.append(int(v1 + v2))


def puzzle_one() -> None:
    """Function for Day One Puzzle 1 AdventofCode 2023

    Args:
        None

    Returns:
        None
    """
    lst = []
    with open(Path("./d1p1.txt"), encoding="utf8") as f:
        for line in f:
            workin_fnc(line, lst)
    answer = sum(lst)
    print(answer)


def puzzle_two() -> None:
    """Function for Day One Puzzle 2 AdventofCode 2023

    Args:
        None

    Returns:
        None
    """
    str_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    lst = []
    with open(Path("./d1p1.txt"), encoding="utf8") as f:
        for line in f:
            temp_line = line
            for dig in str_digits.keys():
                if dig in temp_line:
                    temp_line = temp_line.replace(
                        dig, f"{dig[0]}{str_digits[dig]}{dig[-1]}"
                    )
            workin_fnc(temp_line, lst)
        answer = sum(lst)
        print(answer)


def main() -> None:
    """Main method

    Args:
        None

    Returns:
        None
    """
    puzzle_one()
    puzzle_two()


if __name__ == "__main__":
    main()
