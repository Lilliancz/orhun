from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group == 1:
            if self.group.qtype == "firm":
                yield (pages.ChooseFirm, {'firm':random.choice(Constants.firmChoices)})
            if self.group.qtype == "wtp":
                yield (pages.WTP, {'wtp': random.choice(Constants.wtpChoices)})
        #yield (pages.Results)
