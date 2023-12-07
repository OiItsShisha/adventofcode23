from pathlib import Path
color_dict, total = {"red": 12, "green": 13, "blue": 14}, 0
with open(Path("./d2data.txt")) as f: game_data = f.readlines()
for line in game_data:
    colon_split, game_id, break_flag = line.split(":"), line.split(":")[0], False
    for pull in colon_split[1].split(";"):
        color_cnt = pull.strip().split(",")
        for color in color_cnt:
            for key in color_dict:
                if key in color:
                    temp_color = color.replace(key, "").strip()
                    if int(temp_color) > color_dict[key]: break_flag = True
    if not break_flag:total += int(game_id.replace("Game ", ""))
print(f'Puzzle One Total: {total}')
total = 0
for line in game_data:
    red, blue, green, pulls = 0, 0, 0, line.split(":")[1].split(";")
    for pull in pulls:
        color_cnt = pull.strip().split(",")
        for color in color_cnt:
            if "red" in color:
                t_col = int(color.replace(" red", ""))
                if t_col > red: red = t_col
            elif "blue" in color:
                t_col = int(color.replace(" blue", ""))
                if t_col > blue: blue = t_col
            else:
                t_col = int(color.replace(" green", "")); 
                if t_col > green: green = t_col
    total += red * blue * green
print(f'Puzzle Two total {total}')