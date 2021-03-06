import Dominion
from Dominion import Platinum, Gold, Silver, Copper, Estate, Duchy, Province, Colony
def print_pile(cards, name):
    print(f"Cards in {name}")
    for i in cards:
        print(i.name)


"""# CardPile Testing
a = Dominion.Utils.make_hand("Hand")
~a

print_pile(a, "A")

b = a.get_top_cards(6)

print_pile(a, "A")
print_pile(b, "B")

a.add_cards(b)
print_pile(a, "A")
"""

trash = Dominion.CardPile("TRASH")
supply = Dominion.Supply()

player = Dominion.Player("Sterling", supply, trash)

print(len(player.deck))
print_pile(player.hand, player.hand.name)

player.discard_hand()
player.draw_card(5)

player.discard_hand()
player.draw_card(5)

print_pile(player.hand, player.hand.name)
print_pile(trash, trash.name)
print_pile(player.deck, "DECK")

