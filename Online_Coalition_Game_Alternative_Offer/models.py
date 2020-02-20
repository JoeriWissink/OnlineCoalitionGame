from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import string

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Online_Coalition_Game_Alternative_Offer'
    players_per_group = 3
    num_rounds = 50

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

        for p in self.get_players():
            p.participant.vars['end_game'] = False

        for p in self.get_players():
            p.participant.vars['grouped'] = False

        for p in self.get_players():
            p.participant.vars['leftover'] = False

        for p in self.get_players():
            p.participant.vars['kicked'] = False

        for p in self.get_players():
            p.completion_code = 'DS' + ''.join(random.choices(string.digits, k=4))

        for g in self.get_groups():
            g.coalition_ratified = 'No_coalition'




class Group(BaseGroup):

    proposed_coalition_player_A = models.StringField(widget=widgets.RadioSelect, )
    proposed_coalition_player_B = models.StringField(widget=widgets.RadioSelect, )
    proposed_coalition_player_C = models.StringField(widget=widgets.RadioSelect, )

    allocation_A_to_A = models.IntegerField()
    allocation_A_to_B = models.IntegerField()
    allocation_A_to_C = models.IntegerField()

    allocation_B_to_A = models.IntegerField()
    allocation_B_to_B = models.IntegerField()
    allocation_B_to_C = models.IntegerField()

    allocation_C_to_A = models.IntegerField()
    allocation_C_to_B = models.IntegerField()
    allocation_C_to_C = models.IntegerField()

    selected_coalition_name_player_A = models.StringField()
    selected_coalition_name_player_B = models.StringField()
    selected_coalition_name_player_C = models.StringField()

    selected_coalition_allocation_A_player_A = models.IntegerField()
    selected_coalition_allocation_B_player_A = models.IntegerField()
    selected_coalition_allocation_C_player_A = models.IntegerField()

    selected_coalition_allocation_A_player_B = models.IntegerField()
    selected_coalition_allocation_B_player_B = models.IntegerField()
    selected_coalition_allocation_C_player_B = models.IntegerField()

    selected_coalition_allocation_A_player_C = models.IntegerField()
    selected_coalition_allocation_B_player_C = models.IntegerField()
    selected_coalition_allocation_C_player_C = models.IntegerField()

    tentative_selected_coalition_name_player_A = models.StringField()
    tentative_selected_coalition_name_player_B = models.StringField()
    tentative_selected_coalition_name_player_C = models.StringField()

    tentative_selected_coalition_allocation_A_player_A = models.IntegerField()
    tentative_selected_coalition_allocation_B_player_A = models.IntegerField()
    tentative_selected_coalition_allocation_C_player_A = models.IntegerField()

    tentative_selected_coalition_allocation_A_player_B = models.IntegerField()
    tentative_selected_coalition_allocation_B_player_B = models.IntegerField()
    tentative_selected_coalition_allocation_C_player_B = models.IntegerField()

    tentative_selected_coalition_allocation_A_player_C = models.IntegerField()
    tentative_selected_coalition_allocation_B_player_C = models.IntegerField()
    tentative_selected_coalition_allocation_C_player_C = models.IntegerField()

    tentative_coalition_formed = models.BooleanField()
    tentative_formed_coalition_name = models.StringField()

    not_in_tentative = models.StringField()

    tentative_payoff_A = models.IntegerField()
    tentative_payoff_B = models.IntegerField()
    tentative_payoff_C = models.IntegerField()

    counter_proposed_coalition_name = models.StringField()
    counter_allocation_to_player_A = models.IntegerField()
    counter_allocation_to_player_B = models.IntegerField()
    counter_allocation_to_player_C = models.IntegerField()

    counter_proposed_coalition_player_A = models.StringField(widget=widgets.RadioSelect, )
    counter_proposed_coalition_player_B = models.StringField(widget=widgets.RadioSelect, )
    counter_proposed_coalition_player_C = models.StringField(widget=widgets.RadioSelect, )

    counter_allocation_A_to_A = models.IntegerField()
    counter_allocation_A_to_B = models.IntegerField()
    counter_allocation_A_to_C = models.IntegerField()

    counter_allocation_B_to_A = models.IntegerField()
    counter_allocation_B_to_B = models.IntegerField()
    counter_allocation_B_to_C = models.IntegerField()

    counter_allocation_C_to_A = models.IntegerField()
    counter_allocation_C_to_B = models.IntegerField()
    counter_allocation_C_to_C = models.IntegerField()

    coalition_ratified = models.StringField()

    coalition_ratified_A = models.StringField()
    coalition_ratified_B = models.StringField()
    coalition_ratified_C = models.StringField()


    coalition_formed = models.BooleanField()
    formed_coalition_name = models.StringField()

    coalition_formed_name = models.StringField()
    payoff_A = models.IntegerField()
    payoff_B = models.IntegerField()
    payoff_C = models.IntegerField()

    new_tentative_formed_coalition_name = models.StringField()

    not_in_new_tentative = models.StringField()

    new_tentative_payoff_A = models.IntegerField()
    new_tentative_payoff_B = models.IntegerField()
    new_tentative_payoff_C = models.IntegerField()

    new_tentative_coalition_formed = models.BooleanField()

    round_begin = models.StringField()
    round_end = models.StringField()

class Player(BasePlayer):

    completion_code = models.StringField()

    score = models.IntegerField()
    position = models.StringField()
    resources = models.IntegerField()

    comprehension_money = models.PositiveIntegerField(
        widget=widgets.RadioSelect()
    )

    comprehension_money_fail = models.IntegerField()

    comprehension_exclusion = models.PositiveIntegerField(
        choices=[
            [0, 'This depends on which offer is accepted'],
            [1, 'This party does not receive any money'],
        ],
        widget=widgets.RadioSelect()
    )

    comprehension_exclusion_fail = models.IntegerField()

    comprehension_coalitions = models.PositiveIntegerField(
        widget=widgets.RadioSelect()
    )

    comprehension_coalitions_fail = models.IntegerField()

    proposed_coalition = models.CharField(max_length=3)
    selected_coalition = models.StringField()
    selected_coalition_name = models.CharField(max_length=3)
    selected_coalition_allocation_A = models.IntegerField()
    selected_coalition_allocation_B = models.IntegerField()
    selected_coalition_allocation_C = models.IntegerField()

    allocate_to_player_A = models.PositiveIntegerField(blank=True, null=True)
    allocate_to_player_B = models.PositiveIntegerField(blank=True, null=True)
    allocate_to_player_C = models.PositiveIntegerField(blank=True, null=True)

    tentative_selected_coalition = models.StringField()
    tentative_selected_coalition_name = models.StringField()
    tentative_selected_coalition_allocation_A = models.IntegerField()
    tentative_selected_coalition_allocation_B = models.IntegerField()
    tentative_selected_coalition_allocation_C = models.IntegerField()

    counter_proposed_coalition = models.StringField()
    counter_allocate_to_player_A = models.PositiveIntegerField(blank=True, null=True)
    counter_allocate_to_player_B = models.PositiveIntegerField(blank=True, null=True)
    counter_allocate_to_player_C = models.PositiveIntegerField(blank=True, null=True)

    tentative_payoff = models.IntegerField()

    ratify_coalition = models.StringField()

    money = models.IntegerField()


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
        grand_coalition = self.session.config['grand_coalition']

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
                'grand_coalition': grand_coalition,
                }

    def slider_field(label):
        return models.IntegerField(min=0,
        max=100,
        widget=widgets.Slider(),
        default = 0,
        label=label)

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

    slider22 = slider_field(False)
    slider23 = slider_field(False)
    slider24 = slider_field(False)
    slider25 = slider_field(False)
    slider26 = slider_field(False)
    slider27 = slider_field(False)
    slider28 = slider_field(False)
    slider29 = slider_field(False)
    slider30 = slider_field(False)
    slider31 = slider_field(False)
    slider32 = slider_field(False)
    slider33 = slider_field(False)
    slider34 = slider_field(False)
    slider35 = slider_field(False)
    slider36 = slider_field(False)
    slider37 = slider_field(False)
    slider38 = slider_field(False)
    slider39 = slider_field(False)
    slider40 = slider_field(False)
    slider41 = slider_field(False)
    slider42 = slider_field(False)

    slider43 = slider_field(False)
    slider44 = slider_field(False)
    slider45 = slider_field(False)
    slider46 = slider_field(False)
    slider47 = slider_field(False)
    slider48 = slider_field(False)
    slider49 = slider_field(False)
    slider50 = slider_field(False)
    slider51 = slider_field(False)
    slider52 = slider_field(False)
    slider53 = slider_field(False)
    slider54 = slider_field(False)
    slider55 = slider_field(False)
    slider56 = slider_field(False)
    slider57 = slider_field(False)
    slider58 = slider_field(False)
    slider59 = slider_field(False)
    slider60 = slider_field(False)
    slider61 = slider_field(False)
    slider62 = slider_field(False)
    slider63 = slider_field(False)

    def offer_summary(self):
        offers = (self.allocate_to_player_A, self.allocate_to_player_B, self.allocate_to_player_C)
        offers_int = map(int, offers)
        offers_str = map(str, offers_int)
        return "-".join(offers_str)


    def selected_list(self):
        return [p for p in self.group.get_players() if p.selected == self.id]

    def leftover_check(self):
        other_players = self.get_others_in_group()
        for p in other_players:
            if p.participant.vars['kicked'] == True:
                self.participant.vars['leftover'] = True
            if p.participant._current_page_name == 'Funnel' and self.group.coalition_formed == False:
                    self.participant.vars['leftover'] = True
            if p.participant._current_page_name == 'Demographics' and self.group.coalition_formed == False:
                self.participant.vars['leftover'] = True
            if p.participant._current_page_name == 'Debriefing' and self.group.coalition_formed == False:
                self.participant.vars['leftover'] = True
            if p.participant._current_page_name == 'Kicked' and self.group.coalition_formed == False:
                self.participant.vars['leftover'] = True
