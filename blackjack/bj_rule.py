from card.Trump import DeckAction as d

class Check:
    # BJ　持ち点計算
    def point_check(hands):
        sum_point = 0
        for i in hands:
            point = i[-1]
            if point == 'J' or point == 'Q' or point =='K' or point == '0':
                sum_point += 10
            elif point == 'A':
                if sum_point > 10:
                    sum_point += 1
                else:
                    sum_point += 11
            else:
                sum_point += int(point)
            
            if sum_point > 21 and 'A' in hands:
                sum_point -= 10

        return sum_point

    # burst_check
    def burst_check(point):
        if point > 21:
            print('BURST')
            return True
        else:
            return False

class Bj:
    def doubledown(hands, deck, chips, bet_chip):
        print('DOUBLE DOWN')
        chips -= bet_chip
        bet_chip *= 2
        hands.append(d.draw(deck))
        print(hands[-1])

        player_p = Check.point_check(hands)
        print(hands, '>', player_p)
            
        p_burst = Check.burst_check(player_p)

        return hands, deck, chips, bet_chip, player_p, p_burst