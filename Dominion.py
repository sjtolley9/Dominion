import random

class CardPileIterator():
    def __init__(self, card_pile):
        self._card_pile = card_pile
        self._index = 0
    def __next__(self):
        if self._index < len(self._card_pile.cards):
            result = self._card_pile.cards[self._index]
            self._index += 1
            return result
        raise StopIteration

class CardPile():
    def __init__(self, name="Revealed Cards", cards=None):
        self.name = name
        self.cards = cards
        if cards == None:
            self.cards = []
    def get_top_cards(self, N):
        top_cards = self.cards[-N:]
        if len(top_cards) > 0:
            top_cards = CardPile(cards=top_cards)
        else:
            return None
        self.cards = self.cards[:-N]
        return top_cards
    def add_card(self, card):
        self.cards.append(card)
    def add_cards(self, crds):
        if isinstance(crds, CardPile):
            self.cards.extend(crds.cards)
            crds.cards = []
        else:
            self.cards = self.cards + crds
    def add_cards_below(self, cards):
        if isinstance(cards, CardPile):
            self.cards = cards.cards + self.cards
            cards.cards = []
        else:
            self.cards = cards + self.cards

    def __iter__(self):
        return CardPileIterator(self)
    def shuffle(self):
        random.shuffle(self.cards)
    def __invert__(self):
        self.shuffle()
    def __len__(self):
        return len(self.cards)
    def has(self, name):
        for i in self.cards:
            if i.name == name:
                return True
        return False
    def has_cat(self, cat):
        for i in self.cards:
            if cat in i.categories:
                return True
        return False
    def remove(self, name):
        index = 0
        rem_index = -1
        for i in self.cards:
            if i.name == name:
                rem_index = index
                break
            index += 1
        if rem_index != -1:
            return self.cards.pop(rem_index)
        return None
    def __str__(self):
        return ",".join([x.name for x in self.cards])

class Card():
    def __init__(self, name, categories, cost=0, value=0, victory_points=0):
        self.name = name
        self.categories = categories
        self.cost = cost
        self.value = value
        self.victory_points = victory_points
    def action(self, player, game):
        pass
    def treasure_action(self, player, game):
        pass
    def gain_event(self, player, card):
        pass

class Victory(Card):
    def __init__(self, name, cost, vp):
        Card.__init__(self, name, "victory", cost, victory_points=vp)

class Estate(Victory):
    def __init__(self):
        Victory.__init__(self, "Estate", 2, 1)

class Duchy(Victory):
    def __init__(self):
        Victory.__init__(self, "Duchy", 5, 3)

class Province(Victory):
    def __init__(self):
        Victory.__init__(self, "Province", 8, 6)

class Colony(Victory):
    def __init__(self):
        Victory.__init__(self, "Colony", 11, 10)

class Coin(Card):
    def __init__(self, name, cost, val):
        Card.__init__(self, name, "coin", cost, val)

class Copper(Coin):
    def __init__(self):
        Coin.__init__(self, "Copper", 0, 1)

class Silver(Coin):
    def __init__(self):
        Coin.__init__(self, "Silver", 3, 2)

class Gold(Coin):
    def __init__(self):
        Coin.__init__(self, "Gold", 6, 3)

class Platinum(Coin):
    def __init__(self):
        Coin.__init__(self, "Platinum", 9, 5)


class Utils():
    def make_deck(name):
        cards = [Copper()]*7 + [Estate()]*3
        return CardPile(name, cards)

class Supply():
    def __init__(self):
        pass

class Player():
    def __init__(self, name, supply, trash):
        self.name = name
        self.deck = Utils.make_deck(f"{name}'s Deck")
        self.hand = CardPile(f"{name}'s Hand")
        self.discard= CardPile(f"{name}'s Discard")
        self.aside= CardPile("Aside")
        self.in_play = CardPile(f"{name}'s In Play")
        self.actions = 1
        self.money = 0
        self.buys = 1
        self.supply = supply
        self.trash = trash

        ~self.deck
        
        self.hand.add_cards(self.deck.get_top_cards(5))
    def gain_card(self, destination=None, card=None, N=1, up_to=4, exact_cost=False, category=None):
        pass
    def replenish_deck(self):
        ~self.discard
        self.deck.add_cards_below(self.discard)
    def draw_card(self, N=1):
        if len(self.deck) < N:
            self.replenish_deck()
        self.hand.add_cards(self.deck.get_top_cards(N))
    def pick_cards_from(self, pile, N=1):
        assert isinstance(pile, CardPile)
        print(pile)
        cards = []
        while N > 0 and len(pile) > 0:
            card = input("Choose a card to discard : ")
            if pile.has(card):
                cards.append(pile.remove(card))
                N -= 1
        return CardPile(cards=cards)
    def pick_unknown_cards_from(self, pile, cat="coin"):
        cards = CardPile("Money to",[])
        while len(pile) > 0:
            card = input("Choose money card (Press Enter to Finish): ")
            if card == "":
                break
            if pile.has(card):
                c = pile.remove(card)
                if cat==None or cat in c.categories:
                    cards.add_card(c)
                else:
                    print("Card was not of the correct type")
                    pile.add_card(c)
            else:
                print(f"Could not select {card} from {pile.name}.")
        return cards

    def draw_to_N(self, N):
        while len(self.hand) < N and len(self.deck) > 0:
            self.draw_card()
    def discard_hand(self):
        self.discard.add_cards(self.hand)
    def trash_card(self, N=1, category=None, required=False):
        pass
    def trash_from(self, pile, N=1, required=False):
        pass
    def topdeck_from(self, pile, N=1, required=False):
        pass
    def reveal_cards(self, N=1, source=None, category=None, until_cat=None):
        pass
    def reveal_from_deck(self, N=1):
        if len(self.deck):
            pass
    def get_actions(self):
        return self.actions
    def get_buys(self):
        return self.buys
    def play_money(self):
        while self.hand.has_cat("coin"):
            card = input("Choose a Treasure to play: ")
            if card == "":
                print("Finished Playing Treasure")
                break
            if not self.hand.has(card):
                print(f"Hand does not contain {card}")
                continue
            c = self.hand.remove(card)
            if not "coin" in c.categories:
                self.hand.add_card(c)
                continue
            print(f"{c.name} worth {c.value}")
    def gain_victory_point(self, N=1):
        pass
    def count_victory_points(self):
        pass
