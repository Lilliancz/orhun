from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        print('after_all_players_arrive assign group type')
        if (self.group.id_in_subsession % 2) == 0:
            self.group.qtype = "wtp"
        else:
            self.group.qtype = "firm"


class ChooseFirm(Page):
    form_model = 'group'
    form_fields = ['firm']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return self.group.qtype == "firm"

class WTP(Page):
    form_model = 'group'
    form_fields = ['wtp']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return self.group.qtype == "wtp"


class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        self.group.scores = [p.participant.vars['score1'] for p in self.group.get_players()]
        # scores = [p.score1 for p in self.group.get_players() if p.participant.vars['mygroup']==self.participant.vars['mygroup']]
        print("scores")
        print(self.group.scores)


class Results(Page):


    def vars_for_template(self):
        previous_players = self.player.in_previous_rounds()
        numbers = [p.number for p in previous_players]
        return {
            'numbers':numbers
        }

    def before_next_page(self):
        self.participant.vars['mygroup'] = self.group.id_in_subsession
        print("saving mygroup somewhere?")
        print(self.participant.vars['mygroup'])


page_sequence = [
    MyWaitPage,
    ChooseFirm,
    WTP,
    Results
]
