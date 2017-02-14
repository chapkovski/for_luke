from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Test(Page):
    form_model = models.Player
    form_fields = ['question']

    def is_displayed(self):
        return not self.participant.vars['correct']

    def before_next_page(self):
        if self.player.question ==2:
            self.participant.vars['correct'] = True
        else:
            self.participant.vars['correct'] = False



class Experiment(Page):
    def is_displayed(self):
        return (self.subsession.round_number == Constants.num_rounds and self.participant.vars['correct'])


class Results(Page):
    def is_displayed(self):
        return (self.subsession.round_number == Constants.num_rounds and self.participant.vars['correct'])


class GoodBye(Page):
    def is_displayed(self):
        return (self.subsession.round_number == Constants.num_rounds and not self.participant.vars['correct'])

page_sequence =[
    Test,
    Experiment,
    Results,
    GoodBye,
]
