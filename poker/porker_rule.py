from card.Trump import Card
from collections import Counter

class Poker:
    def hand_check(hands):
        print(hands, ' > ', end='')
        hands = Card.num_change_num(hands)
        num = []
        suit = set()

        for i in hands:
            num.append(int(i[1:]))
            suit.add(i[0])
        
        num.sort()
        num_2 = list(Counter(num).values())

        max_num = 0
        rank = 0
        # macth_count = 0  # 3,4カードの判定
        # pair_count = 0  # ペアの判定
        # suit_count = 0  # 
        flush = False
        straight = False
        royal = False  # A10JQKの時True

        # for i in range(4):
        #     if num[i] == num[i + 1]:
        #         macth_count += 1
        #     else:
        #         pair_count -= 1
        
        if num[0] == 1 and num[1] == 10 and num[2] == 11 and num[3] == 12 and num[4] == 13:
            straight = True
            royal = True
        elif num[0] == num[1] - 1 and num[1] == num[2] - 1 and num[2] == num[3] - 1 and num[3] == num[4] - 1:
            straight = True

        if len(suit) == 1:
            flush = True

        if royal and straight and flush:
            print('ROYAL STRAIGHT FLUSH')
            rank = 1
        elif straight and flush:
            print('STRAIGHT FLUSH')
            rank = 2
        elif len(num_2) == 2:
            if 4 in num_2:
                print('FOUR OF A KIND')
                rank = 3
            else:
                print('FULL HOUSE')
                rank = 4
        elif flush:
            print('FLUSH')
            rank = 5
        elif straight:
            print('STRAIGHT')
            rank = 6
        elif len(num_2) == 3:
            if 3 in num_2:
                 print('THREE CARD')
                 rank = 7
            else:
                print('TWO PAIR')
                rank = 8
        elif len(num_2) == 4:
            print('ONE PAIR')
            rank = 9
        else:
            print('NO PAIR')
            rank = 10

        return rank, max_num
    
    # def discard(hands, *num):
    #     hands_2 = hands.pop(num)
    #     return hands_2
    
    # def exchange(hands):
    #     return

