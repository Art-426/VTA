from card.Trump import Card as c, DeckAction as d, Game as g
from card.BET import Bet
from Baccarat_rule import Point as p, Natural as n, DrawCheck as dc

# # 勝率　使わない
# player_rate, banker_rate, tie_rate = 44.62, 45.86, 9.52

# odds 配当にかける数値
player_odds, banker_odds, tie_odds = 2, 1.95, 9

# # game start
print('***************')
print('Welcome to Baccarat!')
print('***************')
game_flag = True

# chip
chips = 100
devidend_chip = 0

# # loop始点
while game_flag:
    # トランプを作る
    cards = c.make_card()

    # 山をシャッフル 
    deck = d.shuffle(cards)

    # draw_flag
    draw_player, draw_banker,skip_flag = False, False, False

    # naturalのflag
    player_natural, banker_natural = False, False

    # bet対象
    p_bet, b_bet, tie_bet = False, False, False

    # 勝敗判定
    p_win, b_win, tie = False, False, False


    print('Choose which one to bet on "Player" or "Banker" or "Tie"')

    while True:
        bet = input('P or B or T >>> ')
        if bet == 'p' or bet == 'P':
            print('Player')
            p_bet = True
            break
        elif bet == 'b' or bet == 'B':
            print('Banker')
            b_bet = True
            break
        elif bet == 't' or bet == 'T':
            print('Tie')
            t_bet = True
            break
        else:
            continue

    print('賭け金を決めてください')

    bet_chip = Bet.bet_chip(chips)

    chips -= bet_chip
    print(f'賭け金{bet_chip}枚---残り{chips}枚')
    g.pless_enter()

    # カードを2枚配る
    player, banker = [], []

    for i in range(2):
        player.append(d.draw(deck))
        banker.append(d.draw(deck))
        
    # 最初のpoint_chek
    player_point, banker_point = p.point_check(player), p.point_check(banker)

    # 1ターン目の手札表示
    print('***************')
    print('Baccarat_start!')
    print()
    print('open_hands!')
    print()

    player_natural = n.natural_check(player_point)
    print('first_player_hands', player, player_point)

    banker_natural = n.natural_check(banker_point)
    print('first_banker_hands', banker, banker_point)
    g.pless_enter()

    if player_natural or banker_natural:
        skip_flag = True

    # player 3枚目を引くかどうかの判定
    if not skip_flag:
        print('player_draw_fase')
        print()

        # draw_player = dc.player_draw(player_point)
        if player_point <= 5:
            draw_player = True
            player.append(d.draw(deck))
            print('player is draw!', player[2])
            print()
            player_point = p.point_check(player)
        else:
            print('player is not draw...')
            print()

        # player 2ターン目の手札表示
        if not player_natural:
            n.natural_check(player_point)

        print('player_hands', player, player_point)
        g.pless_enter()

    # banker 3枚目を引くかどうかの判定
    if not skip_flag:
        print('banker_draw_fase')
        print()

        # draw_banker = dc.banker_draw(banker_point, player_point, draw_player)
        if not draw_player:
            if (player_point == 6 or player_point == 7) and banker_point <= 5:
                draw_banker = True
        else:
            if banker_point <= 2:
                draw_banker = True
            if banker_point == 3 and (player_point <= 9 and not player_point == 8):
                draw_banker = True
            if banker_point == 4 and 2 <= player_point <= 7:
                draw_banker = True
            if banker_point == 5 and 4 <= player_point <= 7:
                draw_banker = True
            if banker_point == 6 and 6 <= player_point <= 7:
                draw_banker = True

        if draw_banker:
            banker.append(d.draw(deck))
            print('banker is draw!', banker[2])
            print()
            banker_point = p.point_check(banker)
        else:
            print('banker is not draw...')
            print()

        # banker 2ターン目の手札表示
        if not banker_natural:
            n.natural_check(banker_point)
        print('banker_hands', banker, banker_point)
        g.pless_enter()

    # 勝利判定
    print('judge!!')
    print()
    print('final_player_hands', player, player_point)
    print('final_banker_hands', banker, banker_point)
    print()

    if player_point < banker_point:
        b_win = True
        if banker_natural:
            print('banker_natural_win!')
        else:
            print('banker_win!')
    elif player_point > banker_point:
        p_win = True
        if player_natural:
            print('player_natural_win!')
        else:
            print('player_win!')
    else:
        tie = True
        print('tie!')

    print()
    print('--------------------------')
    print()
    if (p_bet and p_win) or (b_bet and b_win) or (tie_bet and tie):
        print('You Win!')
        if p_win:
            get_chip = p.devidend(bet_chip, player_odds)
        elif b_win:
            get_chip = p.devidend(bet_chip, banker_odds)
        else:
            get_chip = p.devidend(bet_chip, player_odds)

        print(f'取得チップ:{get_chip}枚')
        chips += get_chip
    else:
        print('You Lose...')
    
    print(f'所持チップ:{chips}枚')
    
    # # deckからカードを抜いていることの確認
    # print(len(deck))           

    game_flag = g.next_game(chips)
             
    g.pless_enter()
    print('**************')