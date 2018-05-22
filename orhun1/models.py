from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'orhun1'
    players_per_group = None
    num_rounds = 4
    payoff_multiplier = .1

class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating session')
        for p in self.get_players():
            #set random values for each person per round, set only once per round
            p.n1 = random.randint(1,50)
            p.n2 = random.randint(1,50)
            p.answer = p.n1+p.n2
            #print('player' + str(p.id_in_group))
            #print(p.n1)
            #print(p.n2)
            #print(p.answer)
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #ALL THE VARS WE WILL BE USING
    input = models.IntegerField()
    answer = models.IntegerField()
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    diff = models.IntegerField()



