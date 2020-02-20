from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Overview(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class GeneralInstructions(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class InstructionsSeats(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class InstructionsPhases(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class Testinstructions(Page):

    def is_displayed(self):
        return self.session.config['earned']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.session.config['earned'] == True and self.participant.vars['kicked'] == False:
            return True

class PracticeFields(Page):
    form_model = 'player'
    form_fields = ['practice']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def practice_error_message(self, value):
        if value != 150:
            return 'This is incorrect. To make an offer of 150 million you need to insert 150 in the text box. Please try again.'

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class Testslider(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.session.config['earned'] == True and self.participant.vars['kicked'] == False:
            return True

    def get_form_fields(self):
        return ['tslider{}'.format(i) for i in range(1, 22)]

    form_model = 'player'

    def before_next_page(self):
        self.player.tscore = 0

        tsliders = [self.player.tslider1, self.player.tslider2, self.player.tslider3, self.player.tslider4,
                   self.player.tslider5, self.player.tslider6, self.player.tslider7, self.player.tslider8,
                   self.player.tslider9, self.player.tslider10, self.player.tslider11, self.player.tslider12,
                   self.player.tslider13, self.player.tslider14, self.player.tslider15, self.player.tslider16,
                   self.player.tslider17, self.player.tslider18, self.player.tslider19, self.player.tslider20,
                   self.player.tslider21]

        for tslider in tsliders:
            if tslider == 50:
                self.player.tscore += 1

    def get_timeout_seconds(self):
        return self.session.config['slider_time']

class Testresults(Page):

    def vars_for_template(self):
        vars = self.player.vars_for_template()
        vars.update({'tscore': self.player.tscore})
        return vars

    def is_displayed(self):
        if self.session.config['earned'] == True and self.participant.vars['kicked'] == False:
            return True

class Groupassignment(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['kicked'] == False:
            return True

class Kicked(Page):

    def is_displayed(self):
        if self.participant.vars['kicked'] == True:
            return True
        else:
            return False

    def vars_for_template(self):
        return self.player.vars_for_template()

page_sequence = [
    Overview,
    GeneralInstructions,
    InstructionsSeats,
    InstructionsPhases,
    PracticeFields,
    Testinstructions,
    Testslider,
    Testresults,
    Groupassignment,
    Kicked,
]
