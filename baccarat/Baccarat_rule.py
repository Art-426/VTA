class Point:
    # point_check関数　現在の得点（下一桁）を出す
    def point_check(hands):
        sum_point = 0
        for i in hands:
            point = i[-1]
            if point == 'A':
                sum_point += 1
            elif point == 'J' or point == 'Q' or point =='K':
                sum_point += 0
            else:
                sum_point += int(point)
        sum_point = str(sum_point)
        point = int(sum_point[-1])

        return point
    
    def devidend(chip, odds):
        chip *= odds
        return int(chip)


class Natural:
    # natural_check関数　ナチュラルか判定する
    def natural_check(check_point):
        natural_flag = False
        if check_point == 8 or check_point == 9:
            natural_flag = True
        if natural_flag:
            if check_point == 8:
                print('natural_8!')
            elif check_point == 9:
                print('natural_9!')
        else:
            print()
        return natural_flag

# 3枚目の判定
class DrawCheck:
    def banker_draw(b_p, p_p, p_draw):
        if not p_draw:
            if (p_p == 6 or p_p == 7) and b_p <= 5:
                b_draw = True  
        else:
            if b_p <= 2:
               b_draw = True  
            if b_p == 3 and (p_p <= 9 and not p_p == 8):
                b_draw = True
            if b_p == 4 and 2 <= p_p <= 7:
               b_draw = True
            if b_p == 5 and 4 <= p_p <= 7:
               b_draw = True
            if b_p == 6 and 6 <= p_p <= 7:
                b_draw = True
        return b_draw

    def player_draw(p_p):
        if p_p <= 5:
            p_draw = True
        return p_draw

