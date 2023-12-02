from pathlib import Path

data = Path("./d2data.txt")


def puzzle_one() -> None:
    """The code solution for Advent of Code 2023 Day 2 Puzzle 1

    Args:
        None

    Returns:
        None
    """
    color_dict = {"red": 12, "green": 13, "blue": 14}
    total = 0
    with open(data) as f:
        game_data = f.readlines()

    for line in game_data:
        colon_split = line.split(":")
        game_id = colon_split[0]
        break_flag = False
        for pull in colon_split[1].split(";"):
            color_cnt = pull.strip().split(",")
            for color in color_cnt:
                for key in color_dict:
                    if key in color:
                        temp_color = color.replace(key, "").strip()
                        if int(temp_color) > color_dict[key]:
                            break_flag = True
        if not break_flag:
            total += int(game_id.replace("Game ", ""))
    print(total)


def puzzle_two() -> None:
    """The code solution for Advent of Code 2023 Day 2 Puzzle 2

    Args:
        None

    Returns:
        None
    """
    with open(data) as f:
        game_data = f.readlines()
    total = 0
    for line in game_data:
        red, blue, green = 0, 0, 0
        pulls = line.split(":")[1].split(";")
        for pull in pulls:
            color_cnt = pull.strip().split(",")
            for color in color_cnt:
                if "red" in color:
                    t_col = int(color.replace(" red", ""))
                    if t_col > red:
                        red = t_col
                elif "blue" in color:
                    t_col = int(color.replace(" blue", ""))
                    if t_col > blue:
                        blue = t_col
                else:
                    t_col = int(color.replace(" green", ""))
                    if t_col > green:
                        green = t_col
        total += red * blue * green
    print(total)


def main() -> None:
    """The main method

    Args:
        None

    Returns:
        None
    """
    puzzle_one()
    puzzle_two()


if __name__ == "__main__":
    main()
