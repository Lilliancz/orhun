from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'orhun2'
    players_per_group = 3
    num_rounds = 1
    firmChoices = ["Firm A", "Firm B"]
    wtpChoices = [-50,-20,0,20,50]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    firm = models.StringField(choices=Constants.firmChoices,widget=widgets.RadioSelect)
    wtp = models.IntegerField(choices=Constants.wtpChoices,widget=widgets.RadioSelect,label="")
    qtype = models.StringField()
    scores = models.StringField()
    pass

class Player(BasePlayer):
    pass
