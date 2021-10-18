from card.Trump import Card as c, DeckAction as d, Game as g
from porker_rule import Poker as p


print('**************')
print('START')


cards = c.make_card_white()
# deck = d.shuffle(c.make_jokcer(1, cards)) #joker
deck = d.shuffle(cards)

p_hand = 0  #　役の強さ　小さいほど強い
d_hand = 0
p_max = 0  #　手札で最も強い数字
d_max = 0
player = []
dealer = []

for i in range(5):
    player.append(d.draw(deck))
    dealer.append(d.draw(deck))

# player.sort()
# dealer.


# print(player)
# for i in player:
#     print(i[0])
# player = ['♤A','♤4','♤5','♤J','♤10']
p_hand, p_max = p.hand_check(player)
d_hand, d_max = p.hand_check(dealer)

if d_hand < p_hand:
    print('PLAYER')
elif p_hand < d_hand:
    print('DEALER')
else:
    if d_max < p_max:
        print('PLAYER')
    else:
        print('DEALER')

# print(p.discard(player))