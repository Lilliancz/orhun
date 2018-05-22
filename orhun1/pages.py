from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class PerformanceTask(Page):
    form_model = 'player'
    form_fields = ['input']

#calculate accuracy within the page before moving on
    def before_next_page(self):
        self.player.diff = abs(self.player.input - self.player.answer)
        self.player.payoff=self.player.diff*Constants.payoff_multiplier
        self.participant.vars['score1'] = sum([p.payoff for p in self.player.in_all_rounds()])
        print(self.participant.vars['score1'])

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass

page_sequence = [
    PerformanceTask,
    Results
]
