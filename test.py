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
player.hand.add_card(Dominion.Laboratory())
player.hand.add_card(Dominion.Market())
player.hand.add_card(Dominion.Smithy())
player.hand.add_card(Dominion.Village())

player.action_phase(None)
player.play_money()
