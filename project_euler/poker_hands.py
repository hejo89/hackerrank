from collections import defaultdict
decks = []
with open("poker_hands.txt", "r") as h:
    for line in h: decks.append(line.strip().split())
test = ['AH', '2D', '4C', '3D', '5S', '2C', '3D', '4S', '5S', '6D']
def value_of_deck(deck):
    final = [[], []]
    for i, j in enumerate(deck): 
        if j[0] == "T": deck[i] = "10" + j[1:]   
        if j[0] == "J": deck[i] = "11" + j[1:]
        if j[0] == "Q": deck[i] = "12" + j[1:]
        if j[0] == "K": deck[i] = "13" + j[1:]
        if j[0] == "A": deck[i] = "14" + j[1:]
    for i, hand in enumerate([deck[:len(deck) / 2], deck[len(deck) / 2:]]):


        # royal flush
        tmp01 = sorted(map(int, [k[:-1] for k in hand]), reverse = True)
        tmp02 = set([k[-1] for k in hand])

        if tmp01 == [10, 11, 12, 13, 14] and len(tmp02) == 1: final[i].append(10); continue

        # straight flush

        if len(tmp02) == 1 and tmp01 == range(tmp01[0], tmp01[0] + 5):
            final[i].append(9)
            final[i] += tmp01
            continue

        # four of a kind

        d = defaultdict(int)
        for _ in hand:
            d[_[:-1]] += 1
        if 4 in d.values():
            final[i].append(8)
            final[i] += tmp01
            continue

        # full_house

        if len(d) == 2:
            for _ in d:
                if d[_] == 3: v = int(_)
            keys_1 = d.keys()
            if d[keys_1[0]] == 3 and d[keys_1[1]] == 2:
                final[i].append(7)
                final.append(v)
                continue
            if d[keys_1[0]] == 2 and d[keys_1[1]] == 3:
                final[i].append(7)
                final[i].append(v)
                continue
        
        # flush

        flush_set = set()
        for _ in hand:
            flush_set.add(_[-1])
        if len(flush_set) == 1:
            final[i].append(6)
            final[i] += tmp01
            continue
      
        # straight
        # special case for straight, a so called wheel
        if sorted(map(int, [k[:-1] for k in hand])) == [2, 3, 4, 5, 14]:
            final[i].append(5)
            continue
        # normal case
        arr = []
        for _ in hand:
            arr.append(_[:-1])


        r = sorted(map(int, arr))
        if r == range(r[0], r[0] + 5):
            final[i].append(5)
            final[i] += tmp01
            continue

        
        # three of a kind

        if len(d) == 3 and 3 in d.values():
            for _ in d:
                if d[_] == 3: v = int(_)
            final[i].append(4)
            final[i].append(v)
            final[i] += tmp01
            continue 

        # two pairs

        if sorted(d.values()) == [1, 2, 2]:
            v = []
            for _ in d:
                if d[_] == 2: v.append(int(_))
            final[i].append(3)
            final[i] += v + tmp01
            continue

        # one pair

        if len(d) == 4:
            for _ in d:
                if d[_] == 2: v = int(_)
            final[i].append(2)
            final[i].append(v)
            final[i] += tmp01
            continue

        # high card

        if len(d) == 5:
            final[i].append(1)
            final[i] += tmp01

    if final[0] < final[1]: return "Player 2"
    return "Player 1"
test = ["AD", "2S", "3D", "4S", "5D", "3S", "4S", "5S", "6D", "2D"]
print value_of_deck(test)
# für hackerrank...###################
#arr = []
#for _ in range(int(raw_input())):
#    arr.append(raw_input().split())
#for _ in arr:
#    print value_of_deck(_)
######################################
#s = 0
#for _ in decks:
#    if value_of_deck(_) == "Player 1": s += 1
#print s
