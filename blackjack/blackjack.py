from card.Trump import Card as c, DeckAction as d, Game as g
from card.BET import Bet as b
from bj_rule import Check, Bj as bj

# ゲーム開始
print('***************')
print('Welcome to Black Jack!')
print('***************')
game_flag = True    
chips = 100
return_chip = 0
bet_chip = 0


while game_flag:
    p_burst, d_burst = False, False
    p_bj, d_bj = False, False
    doubledown = False

    bet_chip = b.bet_chip(chips)
    chips -= bet_chip
    # カードを作りシャッフル
    card = c.make_card_white()
    deck = d.shuffle(card)
    dealer = []
    player = []

    for i in range(2):
        dealer.append(d.draw(deck))
        player.append(d.draw(deck))

    print('OPEN_HANDS')
    player_p = Check.point_check(player)
    print('dealer_hands', dealer[0], ' * ')
    print('player_hands', player, '>', player_p)

    g.pless_enter()
    # player turn
    if player_p == 21:
        print('BLACK JACK!!')
        print(player, Check.point_check(player))

    else:
        print('DOUBLE DOWN')
        dd = input('Y or N >>> ')
        if dd == 'Y' or dd == 'y':
            doubledown = True
        while not p_burst:
            if doubledown:
                player, deck, chips, bet_chip, player_p, p_burst =  bj.doubledown(player, deck, chips, bet_chip)

            if player_p < 21 and not doubledown:
                draw_flag = d.draw_check()
            else:
                draw_flag = False
            
            if draw_flag:
                print('HIT')
                player.append(d.draw(deck))
                print(player[-1])
            elif doubledown:
                print()
            else:
                print('STAND')
                break

            player_p = Check.point_check(player)
            print(player, '>', player_p)
            
            p_burst = Check.burst_check(player_p)

            if doubledown:
                break

    g.pless_enter()
    # dealer　turn
    print('OPEN')
    dealer_p = Check.point_check(dealer)
    print(dealer, dealer_p)

    if dealer_p == 21:
        print('BLACK JACK!!')

    while True: 
        if dealer_p < 17:
            print('HIT')
            dealer.append(d.draw(deck))
            print(dealer[-1])
        else:
            print('STAND')
            break
        dealer_p = Check.point_check(dealer)
        print(dealer, dealer_p)
    if dealer_p > 21:
        print('BURST!!')
        d_burst = True

    g.pless_enter()

    print('player', player, player_p)
    print('dealer', dealer, dealer_p)

    if player_p < dealer_p <= 21 or (p_burst and not d_burst):
        print('dealer_win')
    elif dealer_p < player_p <= 21 or (d_burst and not p_burst):
        print('player_win')
        chips += bet_chip * 2
    else:
        print('draw')
    
    print(chips)

    game_flag = g.next_game(chips)
    g.pless_enter()
    print('**************')
