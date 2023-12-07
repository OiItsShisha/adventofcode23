from pathlib import Path
def workin_fnc(line, lst) -> None:
    v1 = next((char for char in list(line) if char.isdigit()))
    v2 = next((char for char in reversed(list(line)) if char.isdigit()))
    lst.append(int(v1 + v2))
lst = []
[workin_fnc(line, lst) for line in open(Path("./d1data.txt"), encoding="utf8")]
print(sum(lst)); lst.clear()
str_digits = {
    "one": 1,
    "two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9,}
with open(Path("./d1data.txt"), encoding="utf8") as f:
    for line in f:
        temp_line = line
        for dig in str_digits:
            if dig in temp_line: temp_line = temp_line.replace(
                dig, f"{dig[0]}{str_digits[dig]}{dig[-1]}")
        workin_fnc(temp_line, lst)
print(sum(lst))