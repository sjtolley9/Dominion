import Dominion
from Dominion import Platinum, Gold, Silver, Copper, Estate, Duchy, Province, Colony
def print_pile(cards):
    print(f"Cards in {cards.name}")
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
#player.hand.add_card(Dominion.ThroneRoom())
player.hand.add_card(Dominion.Chapel())
player.hand.add_card(Dominion.Vassal())

player.deck.add_card(Dominion.Sentry())

game = Dominion.Game()
game.supply.print_supply()

player.action_phase(game)
player.treasure_phase()
player.end_turn()
player.end_turn()
player.end_turn()
player.end_turn()
player.end_turn()

#print_pile(player.discard)
#print_pile(player.deck)
#print_pile(player.hand)
