import random

suits = ['♣', '♢', '♡', '♠']
suits = '♣ ♢ ♡ ♠'.split()
suits = list('♣♢♡♠')

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [f'{s}{r}' for r in ranks for s in suits]
print(len(cards))

random.shuffle(cards)

hand = [cards.pop() for _ in range(5)]

print(' '.join(sorted(hand)))

print(len(cards))
















##import random
##
### suits = 'clubs diamonds hearts spades'.split()
### suits = ('\u2660', '\u2661', '\u2662', '\u2663')
##suits = ('♣', '♢', '♡', '♠')
##
##ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
### ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
##
##cards = ['%s of %s' % (r, s) for r in ranks for s in suits]
### cards = [f'{r} of {s}' for r in ranks for s in suits]
### cards = [s + r for r in ranks for s in suits]
### cards = [f'{s}{r}' for r in ranks for s in suits]
##
### cards = []
### for r in ranks:
###     for s in suits:
###         cards.append('%s of %s' % (r, s))
##
##print(cards)
##
##random.shuffle(cards)
##
##hand = [cards.pop() for _ in range(5)]
##
##print(hand)
