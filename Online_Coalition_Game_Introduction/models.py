from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Online_Coalition_Game_Introduction'
    players_per_group = None
    num_rounds = 1

    positions = ['A', 'B', 'C']

class Subsession(BaseSubsession):

    resources_AB = models.IntegerField()
    resources_AC = models.IntegerField()
    resources_BC = models.IntegerField()
    resources_ABC = models.IntegerField()

    def creating_session(self):
        self.resources_AB = self.session.config['resources_player_A'] + self.session.config['resources_player_B']
        self.resources_AC = self.session.config['resources_player_A'] + self.session.config['resources_player_C']
        self.resources_BC = self.session.config['resources_player_B'] + self.session.config['resources_player_C']
        self.resources_ABC = self.session.config['resources_player_A'] + self.session.config['resources_player_B'] + \
                             self.session.config['resources_player_C']


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consent = models.BooleanField()
    tscore = models.IntegerField()
    score = models.IntegerField()
    position = models.StringField()
    resources = models.IntegerField()

    practice = models.IntegerField()


    def vars_for_template(self):

        resources_player_A = self.session.config['resources_player_A']
        resources_player_B = self.session.config['resources_player_B']
        resources_player_C = self.session.config['resources_player_C']
        decision_point = self.session.config['decision_point']

        total_payoff = self.session.config['total_payoff']
        base_fee = self.session.config['base_fee']
        payoff_conversion = self.session.config['payoff_conversion']
        max_bonus = total_payoff * payoff_conversion
        timeout_time = self.session.config['timeout_time']
        timeout_time_minutes = timeout_time / 60
        comprehension_check = self.session.config['comprehension_check']
        incentives = self.session.config['incentives']
        earned = self.session.config['earned']
        slider_time = self.session.config['slider_time']

        possible_coalitions_A = []
        possible_coalitions_B = []
        possible_coalitions_C = []
        possible_coalitions_all = []

        select_none = self.session.config['select_none']

        if self.subsession.resources_AB >= self.session.config['decision_point']:
            possible_coalitions_A.append('AB')
            possible_coalitions_B.append('AB')
            possible_coalitions_all.append('AB')
        if self.subsession.resources_AC >= self.session.config['decision_point']:
            possible_coalitions_A.append('AC')
            possible_coalitions_C.append('AC')
            possible_coalitions_all.append('AC')
        if self.subsession.resources_BC >= self.session.config['decision_point']:
            possible_coalitions_B.append('BC')
            possible_coalitions_C.append('BC')
            possible_coalitions_all.append('BC')
        if self.subsession.resources_ABC >= self.session.config['decision_point'] and self.session.config[
            'grand_coalition']:
            possible_coalitions_A.append('ABC')
            possible_coalitions_B.append('ABC')
            possible_coalitions_C.append('ABC')
            possible_coalitions_all.append('ABC')

        return {'possible_coalitions_A': possible_coalitions_A,
                'possible_coalitions_B': possible_coalitions_B,
                'possible_coalitions_C': possible_coalitions_C,
                'possible_coalitions_all': possible_coalitions_all,
                'resources_player_A': resources_player_A,
                'resources_player_B': resources_player_B,
                'resources_player_C': resources_player_C,
                'total_payoff': total_payoff,
                'base_fee': base_fee,
                'payoff_conversion': payoff_conversion,
                'select_none':select_none,
                'decision_point':decision_point,
                'max_bonus': max_bonus,
                'timeout_time': timeout_time,
                'timeout_time_minutes': timeout_time_minutes,
                'comprehension_check': comprehension_check,
                'incentives': incentives,
                'earned': earned,
                'slider_time': slider_time,
                }

    def slider_field(label):
        return models.IntegerField(min=0,
        max=100,
        widget=widgets.Slider(),
        default = 0,
        label=label,)

    tslider1 = slider_field(False)
    tslider2 = slider_field(False)
    tslider3 = slider_field(False)
    tslider4 = slider_field(False)
    tslider5 = slider_field(False)
    tslider6 = slider_field(False)
    tslider7 = slider_field(False)
    tslider8 = slider_field(False)
    tslider9 = slider_field(False)
    tslider10 = slider_field(False)
    tslider11 = slider_field(False)
    tslider12 = slider_field(False)
    tslider13 = slider_field(False)
    tslider14 = slider_field(False)
    tslider15 = slider_field(False)
    tslider16 = slider_field(False)
    tslider17 = slider_field(False)
    tslider18 = slider_field(False)
    tslider19 = slider_field(False)
    tslider20 = slider_field(False)
    tslider21 = slider_field(False)

    slider1 = slider_field(False)
    slider2 = slider_field(False)
    slider3 = slider_field(False)
    slider4 = slider_field(False)
    slider5 = slider_field(False)
    slider6 = slider_field(False)
    slider7 = slider_field(False)
    slider8 = slider_field(False)
    slider9 = slider_field(False)
    slider10 = slider_field(False)
    slider11 = slider_field(False)
    slider12 = slider_field(False)
    slider13 = slider_field(False)
    slider14 = slider_field(False)
    slider15 = slider_field(False)
    slider16 = slider_field(False)
    slider17 = slider_field(False)
    slider18 = slider_field(False)
    slider19 = slider_field(False)
    slider20 = slider_field(False)
    slider21 = slider_field(False)