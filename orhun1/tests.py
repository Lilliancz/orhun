from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):
        guess = random.randint(1,99)
        print('guess' + str(guess))
        yield (pages.PerformanceTask, {'input':guess})
        yield (pages.Results)
