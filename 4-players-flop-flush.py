#!/usr/bin/env python3

import random

class monte:
    pass

def main():

    flush4 = 0
    total = 0
    
    for i in range(0, 100000000):
        cards = list(range(0,51))
        hands = deal(cards)
        flop = dealFlop(cards)
        if is4flush(hands, flop):
            flush4+=1
	    print("4 flush found:")
            print(hands)
            print(flop)
        total+=1

    print("Results: Number of times 4 players flopped a flush 9-handed:")        
    print(flush4)
    print("Total hands dealt:")
    print(total)

def deal(cards):
    players=[]
    for i in range(9):
        players.append([cards.pop(random.randrange(0,len(cards))), cards.pop(random.randrange(0,len(cards)))])

    return players

def dealFlop(cards):
    flop = []
    for i in range(3):
        flop.append(cards.pop(random.randrange(0,len(cards))))
    return flop

def is4flush(hands, flop):
    misses=9
    if flop[0]//13 == flop[1]//13 == flop[2]//13:
        suit = flop[0]//13
        i=0
        while misses > 5 and i < 9:
            if hands[i][0]//13 == suit and hands[i][1]//13 == suit:
                misses-=1
            i=i+1
    if misses > 5: return False
    else: return True
    

if __name__ == "__main__":
    main()
