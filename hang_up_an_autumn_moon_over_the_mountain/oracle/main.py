from .assets.texts import cards
from random import randint, shuffle
from .random_art.randomart import draw_cards, drunkenwalk

class Oracle():
    def __init__(self, sparrow_mode=False):
        self.sparrow_mode = sparrow_mode
        self.cards = self._set_cards(cards)


    # INT FUNCTIONS 
    def _set_sparrow_mode(self, cards):
        return [card for card in cards if card['mode'] == 'sparrow']


    def _set_cards(self, cards):
        if self.sparrow_mode:
            cards = self._set_sparrow_mode(cards)
        shuffle(cards)
        cards = cards[:3]
        
        for i, card in enumerate(cards):
            cards[i]['substring'] = self._create_digest(card['text'])
        
        return cards


    def _create_substring_range(self, haiku):
        start = randint(0, len(haiku)-2)
        stop = randint(start+1, len(haiku)-1)
        
        substring = list(range(start,stop))

        return substring


    def _create_digest(self, haiku):
        haiku = haiku.replace('\n', '').replace(' ','').lower()
        sub = self._create_substring_range(haiku)
        
        return haiku[sub[0]:sub[-1]]


    def _pick_oracle(self, sub, haiku):
        mid = len(haiku)/2
        if not mid.is_integer():
            if mid >= sub[-1]:
                return True
            elif mid <= sub[0]:
                return False
            else:
                if len(sub[0:int(mid)+1]) > len(sub[int(mid):]):
                    return True
                else: 
                    return False
        else:
            mid_floor, mid_ceil = mid - 1, mid
            if sub == [mid_floor, mid_ceil]:
                return False, True
            elif mid_floor >= sub[-1]:
                return True
            elif mid_ceil <= sub[0]:
                return False
            else: 
                if len(sub[0:int(mid_ceil)+1]) > len(sub[int(mid_floor):]):
                    return True
                else:
                    return False


    # EXT FUNCTIONS
    def draw_selection_cards(self):
        digests = [drunkenwalk(s['substring'].encode()) for s in self.cards]
        
        selection_cards = draw_cards(digests)
        
        return selection_cards


    def run_oracle(self, selection):
        card = self.cards[selection]
        haiku = card['text']
        sub = self._create_substring_range(haiku)

        oracle = self._pick_oracle(sub, haiku)
        oracle = card['oracle'][oracle] if type(oracle) == bool else card['oracle'][:]

        oracle_obj = {
            'oracle': oracle,
            'haiku': haiku
        }
        return oracle_obj
