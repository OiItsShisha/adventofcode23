from pathlib import Path
with open(Path("./d4data.txt")) as f: data=f.readlines(); p1t, p2t, counter= 0, 0, {}
for line in data:
    card_num, card = line.split(":")[0], line.split(':')[1].split(' | ')
    if "   " in card_num: card_num = card_num.replace("   ", " ")
    else: card_num = card_num.replace("  ", " "); repeater=0
    if counter:
        for key, item in counter.items():
            for entry in item:
                if int(card_num.split(" ")[1]) == entry: repeater += 1
    card[0]= card[0].replace(' ',',').replace(',,', ',')[1::]
    card[1]=card[1].replace(' ', ',').replace(',,',',').strip()[1::] if card[1].startswith(
        " ") else card[1].replace(' ', ',').replace(',,',',').strip()
    if set([int(c) for c in eval(card[0])]).intersection(set([int(c) for c in eval(
        card[1])])): p1t += pow(2, len(set([int(c) for c in eval(card[0])]).intersection(
            set([int(c) for c in eval(card[1])])))-1)
    while repeater >= 0:
        if val := set(eval(card[0])).intersection(set(eval(card[1]))):
            if card_num not in counter:
                counter[card_num] = [(int(card_num.split(" ")[1])+1)+x for x in range(len(
                    val)) if x < len(data)]
            else:
                counter[card_num] += [(int(card_num.split(" ")[1])+1)+x for x in range(len(
                    val)) if x < len(data)]
        repeater -=1
for key, item in counter.items():
    p2t+=len(item)
p2t+=len(data); print(f'Puzzle One: {p1t}, Puzzle 2: {p2t}')