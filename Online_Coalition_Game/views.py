from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage
import random
import string

class Waitforgroup(CustomMturkWaitPage):
    title_text = "Matching you with participants"
    group_by_arrival_time = True

    startwp_timer = 5 * 60
    use_task = False


    def get_players_for_group(self, waiting_players):
        positions = iter(Constants.positions)
        active_players = [p for p in waiting_players if p.participant._current_page_name == 'Waitforgroup']
        if len(active_players) >= Constants.players_per_group:
            if not self.session.config['earned']:
                for p in active_players:
                    p.position = next(positions)
                    if p.position == 'A':
                        p.resources = self.session.config['resources_player_A']
                    elif p.position == 'B':
                        p.resources = self.session.config['resources_player_B']
                    elif p.position == 'C':
                        p.resources = self.session.config['resources_player_C']
            return active_players

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False




class Groupingconfirmation(CustomMturkPage):



    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1  and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']


    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.participant.vars['grouped'] = True
        self.player.leftover_check()

class Sliderinstructions(CustomMturkPage):



    def vars_for_template(self):
        return self.player.vars_for_template()


    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config['earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

    def vars_for_template(self):
        return self.player.vars_for_template()

class Slider(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config['earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['slider_time']

    form_model = 'player'

    def get_form_fields(self):
        return ['slider{}'.format(i) for i in range(1, 22)]

class EndRound1(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config['earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

class Slider2(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config[
                'earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars[
                'leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['slider_time']

    form_model = 'player'

    def get_form_fields(self):
        return ['slider{}'.format(i) for i in range(22, 43)]

class EndRound2(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config['earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

class Slider3(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config[
                'earned'] == True and self.participant.vars['kicked'] == False and self.participant.vars[
                'leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['slider_time']

    form_model = 'player'

    def get_form_fields(self):
        return ['slider{}'.format(i) for i in range(43, 64)]

    def before_next_page(self):
        self.player.score = 0
        self.player.leftover_check()

        sliders = [self.player.slider1, self.player.slider2, self.player.slider3, self.player.slider4, self.player.slider5, self.player.slider6, self.player.slider7, self.player.slider8, self.player.slider9, self.player.slider10, self.player.slider11, self.player.slider12, self.player.slider13, self.player.slider14, self.player.slider15, self.player.slider16, self.player.slider17, self.player.slider18, self.player.slider19, self.player.slider20, self.player.slider21, self.player.slider22, self.player.slider23, self.player.slider24, self.player.slider25, self.player.slider26, self.player.slider27, self.player.slider28, self.player.slider29, self.player.slider30, self.player.slider31, self.player.slider32, self.player.slider33, self.player.slider34, self.player.slider35, self.player.slider36, self.player.slider37, self.player.slider38, self.player.slider39, self.player.slider40, self.player.slider41, self.player.slider42, self.player.slider43, self.player.slider44, self.player.slider45, self.player.slider46, self.player.slider47, self.player.slider48, self.player.slider49, self.player.slider50, self.player.slider51, self.player.slider52, self.player.slider53, self.player.slider54, self.player.slider55, self.player.slider56, self.player.slider57, self.player.slider58, self.player.slider59, self.player.slider60, self.player.slider61, self.player.slider62, self.player.slider63]

        for slider in sliders:
            if slider == 50:
                self.player.score += 1

        self.participant.vars['score'] = self.player.score







class Waitforparticipants(WaitPage):

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.session.config['earned'] == True and self.participant.vars['grouped'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    title_text = "Waiting for other participants"
    body_text = "Waiting for the other two participants to complete the slider task. Please wait."

    def after_all_players_arrive(self):

        scores = []
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)

        for p in self.group.get_players():

            summary = (p.id_in_group, p.score)

            scores.append(summary)
        sorted_scores = sorted(scores, key=lambda tup: tup[1], reverse=True)

        A = sorted_scores[0]
        B = sorted_scores[1]
        C = sorted_scores[2]


        if A[0] == 1:
            p1.position = 'A'
            p1.resources = self.session.config['resources_player_A']
        elif A[0] == 2:
            p2.position = 'A'
            p2.resources = self.session.config['resources_player_A']
        elif A[0] == 3:
            p3.position = 'A'
            p3.resources = self.session.config['resources_player_A']

        if B[0] == 1:
            p1.position = 'B'
            p1.resources = self.session.config['resources_player_B']
        elif B[0] == 2:
            p2.position = 'B'
            p2.resources = self.session.config['resources_player_B']
        elif B[0] == 3:
            p3.position = 'B'
            p3.resources = self.session.config['resources_player_B']

        if C[0] == 1:
            p1.position = 'C'
            p1.resources = self.session.config['resources_player_C']
        elif C[0] == 2:
            p2.position = 'C'
            p2.resources = self.session.config['resources_player_C']
        elif C[0] == 3:
            p3.position = 'C'
            p3.resources = self.session.config['resources_player_C']


class PositionAssignment(CustomMturkPage):

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False and self.session.config['earned'] == True and self.round_number == 1:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

    def vars_for_template(self):
        return self.player.vars_for_template()

class AssignedPosition(CustomMturkPage):

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def vars_for_template(self):
        return self.player.vars_for_template()

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()


class InstructionsCoalitions(CustomMturkPage):
    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class ComprehensionCheck(CustomMturkPage):
    form_model = 'player'
    form_fields = ['comprehension_money']

    def is_displayed(self):
        if self.session.config['comprehension_check'] == True and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def vars_for_template(self):
        vars = self.player.vars_for_template()
        vars.update({
            'money_label': "How large is the budget that can be allocated?"})
        return vars

    def comprehension_money_choices(self):
        choices = [
            [0, 'Always ${} million'.format(self.session.config['total_payoff'])],
            [1, 'This depends on the size of the coalition'],
        ]
        return choices

    def comprehension_money_error_message(self, value):
        if value == 1:
            self.player.comprehension_money_fail = 1
            return "Your answer is incorrect. The budget is ${} million, regardless of the size of the coalition.".format(
                self.session.config['total_payoff'])

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()


class ComprehensionCheck2(CustomMturkPage):
    form_model = 'player'
    form_fields = ['comprehension_exclusion']

    def is_displayed(self):
        if self.session.config['comprehension_check'] == True and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def comprehension_exclusion_error_message(self, value):
        if value == 0:
            self.player.comprehension_exclusion_fail = 1
            return "Your answer is incorrect. The party that is not in the coalition will never receive any money."

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class ComprehensionCheck3(CustomMturkPage):
    form_model = 'player'
    form_fields = ['comprehension_coalitions']

    def is_displayed(self):
        if self.session.config['comprehension_check'] == True and self.round_number == 1 and self.participant.vars[
            'kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def comprehension_coalitions_choices(self):
        choices = []
        if not self.session.config['grand_coalition']:
            choices = [
                [0, 'AB and AC '],
                [1, 'AB and BC'],
                [2, 'AC and BC'],
                [3, 'AB, AC and BC'],
            ]

        elif self.session.config['grand_coalition']:
            choices = [
                [0, 'AB and AC '],
                [1, 'AB and BC'],
                [2, 'AC and BC'],
                [3, 'AB, AC and BC'],
                [4, 'AB, AC, BC and ABC'],
            ]

        return choices

    def comprehension_coalitions_error_message(self, value):
        if self.session.config['grand_coalition'] == False and value != 3:
            if value == 0:
                self.player.comprehension_coalitions_fail = 0
            if value == 1:
                self.player.comprehension_coalitions_fail = 1
            if value == 2:
                self.player.comprehension_coalitions_fail = 2
            return "Your answer is incorrect. The coalitions that can be formed are AB, AC and BC"
        if self.session.config['grand_coalition'] == True and value != 4:
            if value == 0:
                self.player.comprehension_coalitions_fail = 0
            if value == 1:
                self.player.comprehension_coalitions_fail = 1
            if value == 2:
                self.player.comprehension_coalitions_fail = 2
            if value == 3:
                self.player.comprehension_coalitions_fail = 3
            return "Your answer is incorrect. The coalitions that can be formed are AB, AC, BC and ABC"

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class ManipulationCheck2control(CustomMturkPage):

    def is_displayed(self):
        if self.round_number == 1 and self.participant.vars[
            'kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['manipulation_check2control']

class ManipulationCheck2controlBudget(CustomMturkPage):

    def is_displayed(self):
        if self.round_number == 1 and self.participant.vars[
            'kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    form_model = 'player'
    form_fields = ['manipulation_check2controlbudget']

class BargainingStarts(CustomMturkPage):

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class NewRound(CustomMturkPage):
    def vars_for_template(self):
        return self.player.vars_for_template()


    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.round_number > 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def before_next_page(self):
        for player in self.group.get_players():
            prev_player = player.in_round(1)
            player.position = prev_player.position
            player.resources = prev_player.resources
            player.completion_code = prev_player.completion_code
        self.player.leftover_check()
        if self.timeout_happened:
            self.participant.vars['kicked'] = True

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

class PhaseI(CustomMturkPage):
    def vars_for_template(self):
        return self.player.vars_for_template()

    form_model = 'player'
    form_fields = ['proposed_coalition', 'allocate_to_player_A', 'allocate_to_player_B', 'allocate_to_player_C']

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def before_next_page(self):
        for p in self.group.get_players():
            if p.proposed_coalition == 'BC':
                p.allocate_to_player_A = 0
            if p.proposed_coalition == 'AC':
                p.allocate_to_player_B = 0
            if p.proposed_coalition == 'AB':
                p.allocate_to_player_C = 0
            if p.position == 'A':
                self.group.proposed_coalition_player_A = p.proposed_coalition
                self.group.allocation_A_to_A = p.allocate_to_player_A
                self.group.allocation_A_to_B = p.allocate_to_player_B
                self.group.allocation_A_to_C = p.allocate_to_player_C
            elif p.position == 'B':
                self.group.proposed_coalition_player_B = p.proposed_coalition
                self.group.allocation_B_to_A = p.allocate_to_player_A
                self.group.allocation_B_to_B = p.allocate_to_player_B
                self.group.allocation_B_to_C = p.allocate_to_player_C
            elif p.position == 'C':
                self.group.proposed_coalition_player_C = p.proposed_coalition
                self.group.allocation_C_to_A = p.allocate_to_player_A
                self.group.allocation_C_to_B = p.allocate_to_player_B
                self.group.allocation_C_to_C = p.allocate_to_player_C

        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

class WaitForOffers(WaitPage):
    title_text = "Waiting for offers"
    body_text = "Waiting until all participants have made an offer. This could take a while."

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

class OffersMade(CustomMturkPage):

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class PhaseII(CustomMturkPage):
    form_model = 'player'
    form_fields = ['selected_coalition']

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def vars_for_template(self):
        vars = self.player.vars_for_template()
        offers = dict()
        for p in self.group.get_players():
            pc = p.proposed_coalition
            if pc and self.player.position in p.proposed_coalition:
                summary = (
                pc, p.offer_summary(), p.allocate_to_player_A, p.allocate_to_player_B, p.allocate_to_player_C,
                p.id_in_group,)
                summary_wo_id = summary[:-1]
                offers[summary_wo_id] = summary

        if self.session.config['select_none']:
            offers['tuple'] = ("Select this option if you do not wish to select one of the above offers. You will not be able to form a coalition this round.", "No", 99, 99, 99, 'None')
        vars.update({"offers": sorted(offers.values())})
        return vars

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class WaitForSelection(WaitPage):
    title_text = "Waiting for selection"
    body_text = "Waiting until all participants have chosen an offer. This may take a while."

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['grouped'] == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def after_all_players_arrive(self):

        players = self.group.get_players()

        for p in players:
            cs = p.selected_coalition
            if p.selected_coalition != 'None':
                p.selected_coalition_name = self.group.get_player_by_id(cs).proposed_coalition
                p.selected_coalition_allocation_A = self.group.get_player_by_id(cs).allocate_to_player_A
                p.selected_coalition_allocation_B = self.group.get_player_by_id(cs).allocate_to_player_B
                p.selected_coalition_allocation_C = self.group.get_player_by_id(cs).allocate_to_player_C

            elif p.selected_coalition == 'None':
                p.selected_coalition_name = 'None'
                p.selected_coalition_allocation_A = None
                p.selected_coalition_allocation_B = None
                p.selected_coalition_allocation_C = None

            if p.position == 'A':
                self.group.selected_coalition_name_player_A = p.selected_coalition_name
                self.group.selected_coalition_allocation_A_player_A = p.selected_coalition_allocation_A
                self.group.selected_coalition_allocation_B_player_A = p.selected_coalition_allocation_B
                self.group.selected_coalition_allocation_C_player_A = p.selected_coalition_allocation_C
            elif p.position == 'B':
                self.group.selected_coalition_name_player_B = p.selected_coalition_name
                self.group.selected_coalition_allocation_A_player_B = p.selected_coalition_allocation_A
                self.group.selected_coalition_allocation_B_player_B = p.selected_coalition_allocation_B
                self.group.selected_coalition_allocation_C_player_B = p.selected_coalition_allocation_C
            elif p.position == 'C':
                self.group.selected_coalition_name_player_C = p.selected_coalition_name
                self.group.selected_coalition_allocation_A_player_C = p.selected_coalition_allocation_A
                self.group.selected_coalition_allocation_B_player_C = p.selected_coalition_allocation_B
                self.group.selected_coalition_allocation_C_player_C = p.selected_coalition_allocation_C


        list_AB = []
        list_AC = []
        list_BC = []
        list_ABC = []
        list_none = []

        for p in players:
            if p.selected_coalition_name == "AB":
                list_AB.append(p.position)
            if p.selected_coalition_name == "AC":
                list_AC.append(p.position)
            if p.selected_coalition_name == "BC":
                list_BC.append(p.position)
            if p.selected_coalition_name == "ABC":
                list_ABC.append(p.position)
            if p.selected_coalition_name == None:
                list_none.append(p.position)


        if len(
                list_AB) == 2 and self.group.selected_coalition_allocation_A_player_A == self.group.selected_coalition_allocation_A_player_B:
            if self.group.selected_coalition_allocation_B_player_A == self.group.selected_coalition_allocation_B_player_B:
                print("AB is formed")
                self.group.coalition_formed = True
                self.group.formed_coalition_name = "AB"
                self.group.payoff_A = self.group.selected_coalition_allocation_A_player_A
                self.group.payoff_B = self.group.selected_coalition_allocation_B_player_B
                self.group.payoff_C = 0


        elif len(
                list_AC) == 2 and self.group.selected_coalition_allocation_A_player_A == self.group.selected_coalition_allocation_A_player_C:
            if self.group.selected_coalition_allocation_C_player_A == self.group.selected_coalition_allocation_C_player_C:
                print("AC is formed")
                self.group.coalition_formed = True
                self.group.formed_coalition_name = "AC"
                self.group.payoff_A = self.group.selected_coalition_allocation_A_player_A
                self.group.payoff_B = 0
                self.group.payoff_C = self.group.selected_coalition_allocation_C_player_C

        elif len(
                list_BC) == 2 and self.group.selected_coalition_allocation_B_player_B == self.group.selected_coalition_allocation_B_player_C:
            print("First part for B works")
            if self.group.selected_coalition_allocation_C_player_B == self.group.selected_coalition_allocation_C_player_C:
                print("BC is formed")
                self.group.coalition_formed = True
                self.group.formed_coalition_name = "BC"
                self.group.payoff_A = 0
                self.group.payoff_B = self.group.selected_coalition_allocation_B_player_B
                self.group.payoff_C = self.group.selected_coalition_allocation_C_player_C

        elif len(
                list_ABC) == 3 and self.group.selected_coalition_allocation_A_player_A == self.group.selected_coalition_allocation_A_player_B == self.group.selected_coalition_allocation_A_player_C:
            if self.group.selected_coalition_allocation_B_player_A == self.group.selected_coalition_allocation_B_player_B == self.group.selected_coalition_allocation_B_player_C:
                if self.group.selected_coalition_allocation_C_player_A == self.group.selected_coalition_allocation_C_player_B == self.group.selected_coalition_allocation_C_player_C:
                    self.group.coalition_formed = True
                    self.group.formed_coalition_name = "ABC"
                    self.group.payoff_A = self.group.selected_coalition_allocation_A_player_A
                    self.group.payoff_B = self.group.selected_coalition_allocation_B_player_B
                    self.group.payoff_C = self.group.selected_coalition_allocation_C_player_C

        else:
            self.group.coalition_formed = False
            self.group.payoff_A = 0
            self.group.payoff_B = 0
            self.group.payoff_C = 0

        for p in players:
            if p.position == "A":
                p.money = self.group.payoff_A
                p.payoff = self.group.payoff_A * self.session.config['payoff_conversion']
            if p.position == "B":
                p.money = self.group.payoff_B
                p.payoff = self.group.payoff_B * self.session.config['payoff_conversion']
            if p.position == "C":
                p.money = self.group.payoff_C
                p.payoff = self.group.payoff_C * self.session.config['payoff_conversion']


class OffersSelected(CustomMturkPage):
    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False and \
                        self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()

class PhaseIII_Success(CustomMturkPage):
    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.group.coalition_formed == 1 and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def vars_for_template(self):

        offers_dict = dict()

        vars = self.player.vars_for_template()

        prop_name_A = self.group.proposed_coalition_player_A
        prop_name_B = self.group.proposed_coalition_player_B
        prop_name_C = self.group.proposed_coalition_player_C

        prop_A_to_A = self.group.allocation_A_to_A
        prop_A_to_B = self.group.allocation_A_to_B
        prop_A_to_C = self.group.allocation_A_to_C

        prop_B_to_A = self.group.allocation_B_to_A
        prop_B_to_B = self.group.allocation_B_to_B
        prop_B_to_C = self.group.allocation_B_to_C

        prop_C_to_A = self.group.allocation_C_to_A
        prop_C_to_B = self.group.allocation_C_to_B
        prop_C_to_C = self.group.allocation_C_to_C

        sel_name_A = self.group.selected_coalition_name_player_A
        sel_name_B = self.group.selected_coalition_name_player_B
        sel_name_C = self.group.selected_coalition_name_player_C

        sel_A_to_A = self.group.selected_coalition_allocation_A_player_A
        sel_A_to_B = self.group.selected_coalition_allocation_B_player_A
        sel_A_to_C = self.group.selected_coalition_allocation_C_player_A

        sel_B_to_A = self.group.selected_coalition_allocation_A_player_B
        sel_B_to_B = self.group.selected_coalition_allocation_B_player_B
        sel_B_to_C = self.group.selected_coalition_allocation_C_player_B

        sel_C_to_A = self.group.selected_coalition_allocation_A_player_C
        sel_C_to_B = self.group.selected_coalition_allocation_B_player_C
        sel_C_to_C = self.group.selected_coalition_allocation_C_player_C

        proposed_by_A = 0
        proposed_by_B = 0
        proposed_by_C = 0

        selected_by_A = 0
        selected_by_B = 0
        selected_by_C = 0

        offer_A = [self.group.proposed_coalition_player_A, self.group.allocation_A_to_A, self.group.allocation_A_to_B,
                   self.group.allocation_A_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offer_B = [self.group.proposed_coalition_player_B, self.group.allocation_B_to_A, self.group.allocation_B_to_B,
                   self.group.allocation_B_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offer_C = [self.group.proposed_coalition_player_C, self.group.allocation_C_to_A, self.group.allocation_C_to_B,
                   self.group.allocation_C_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offers = (offer_A, offer_B, offer_C)

        for offer in offers:
            if offer[0] == prop_name_A and offer[1] == prop_A_to_A and offer[2] == prop_A_to_B and offer[
                3] == prop_A_to_C:
                offer[4] = 1
            if offer[0] == prop_name_B and offer[1] == prop_B_to_A and offer[2] == prop_B_to_B and offer[
                3] == prop_B_to_C:
                offer[5] = 1
            if offer[0] == prop_name_C and offer[1] == prop_C_to_A and offer[2] == prop_C_to_B and offer[
                3] == prop_C_to_C:
                offer[6] = 1
            if offer[0] == sel_name_A and offer[1] == sel_A_to_A and offer[2] == sel_A_to_B and offer[3] == sel_A_to_C:
                offer[7] = 1
            if offer[0] == sel_name_B and offer[1] == sel_B_to_A and offer[2] == sel_B_to_B and offer[3] == sel_B_to_C:
                offer[8] = 1
            if offer[0] == sel_name_C and offer[1] == sel_C_to_A and offer[2] == sel_C_to_B and offer[3] == sel_C_to_C:
                offer[9] = 1

            offer_dict = (offer[0], offer[1], offer[2], offer[3], offer[4], offer[5], offer[6],
                          offer[7], offer[8], offer[9],)
            offers_dict[offer_dict] = offer_dict
        vars.update({"offers_dictionary": sorted(offers_dict.values())})

        return vars

    def before_next_page(self):
        for p in self.group.get_players():
            if p.position == 'A':
                p.payoff = self.group.payoff_A * self.session.config['payoff_conversion']
            if p.position == 'B':
                p.payoff = self.group.payoff_B * self.session.config['payoff_conversion']
            if p.position == 'C':
                p.payoff = self.group.payoff_C * self.session.config['payoff_conversion']




class Payoff(CustomMturkPage):
    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.group.coalition_formed == True and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False





class PhaseIII_Failure(CustomMturkPage):
    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.group.coalition_formed == False and self.participant.vars['kicked'] == False and self.participant.vars['leftover'] == False:
            return True
        else:
            return False

    def vars_for_template(self):

        offers_dict = dict()

        vars = self.player.vars_for_template()

        prop_name_A = self.group.proposed_coalition_player_A
        prop_name_B = self.group.proposed_coalition_player_B
        prop_name_C = self.group.proposed_coalition_player_C

        prop_A_to_A = self.group.allocation_A_to_A
        prop_A_to_B = self.group.allocation_A_to_B
        prop_A_to_C = self.group.allocation_A_to_C

        prop_B_to_A = self.group.allocation_B_to_A
        prop_B_to_B = self.group.allocation_B_to_B
        prop_B_to_C = self.group.allocation_B_to_C

        prop_C_to_A = self.group.allocation_C_to_A
        prop_C_to_B = self.group.allocation_C_to_B
        prop_C_to_C = self.group.allocation_C_to_C

        sel_name_A = self.group.selected_coalition_name_player_A
        sel_name_B = self.group.selected_coalition_name_player_B
        sel_name_C = self.group.selected_coalition_name_player_C

        sel_A_to_A = self.group.selected_coalition_allocation_A_player_A
        sel_A_to_B = self.group.selected_coalition_allocation_B_player_A
        sel_A_to_C = self.group.selected_coalition_allocation_C_player_A

        sel_B_to_A = self.group.selected_coalition_allocation_A_player_B
        sel_B_to_B = self.group.selected_coalition_allocation_B_player_B
        sel_B_to_C = self.group.selected_coalition_allocation_C_player_B

        sel_C_to_A = self.group.selected_coalition_allocation_A_player_C
        sel_C_to_B = self.group.selected_coalition_allocation_B_player_C
        sel_C_to_C = self.group.selected_coalition_allocation_C_player_C

        proposed_by_A = 0
        proposed_by_B = 0
        proposed_by_C = 0

        selected_by_A = 0
        selected_by_B = 0
        selected_by_C = 0

        offer_A = [self.group.proposed_coalition_player_A, self.group.allocation_A_to_A, self.group.allocation_A_to_B,
                   self.group.allocation_A_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offer_B = [self.group.proposed_coalition_player_B, self.group.allocation_B_to_A, self.group.allocation_B_to_B,
                   self.group.allocation_B_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offer_C = [self.group.proposed_coalition_player_C, self.group.allocation_C_to_A, self.group.allocation_C_to_B,
                   self.group.allocation_C_to_C, proposed_by_A, proposed_by_B, proposed_by_C, selected_by_A,
                   selected_by_B, selected_by_C]
        offers = (offer_A, offer_B, offer_C)

        for offer in offers:
            if offer[0] == prop_name_A and offer[1] == prop_A_to_A and offer[2] == prop_A_to_B and offer[
                3] == prop_A_to_C:
                offer[4] = 1
            if offer[0] == prop_name_B and offer[1] == prop_B_to_A and offer[2] == prop_B_to_B and offer[
                3] == prop_B_to_C:
                offer[5] = 1
            if offer[0] == prop_name_C and offer[1] == prop_C_to_A and offer[2] == prop_C_to_B and offer[
                3] == prop_C_to_C:
                offer[6] = 1
            if offer[0] == sel_name_A and offer[1] == sel_A_to_A and offer[2] == sel_A_to_B and offer[3] == sel_A_to_C:
                offer[7] = 1
            if offer[0] == sel_name_B and offer[1] == sel_B_to_A and offer[2] == sel_B_to_B and offer[3] == sel_B_to_C:
                offer[8] = 1
            if offer[0] == sel_name_C and offer[1] == sel_C_to_A and offer[2] == sel_C_to_B and offer[3] == sel_C_to_C:
                offer[9] = 1

            offer_dict = (offer[0], offer[1], offer[2], offer[3], offer[4], offer[5], offer[6],
                          offer[7], offer[8], offer[9],)
            offers_dict[offer_dict] = offer_dict
        vars.update({"offers_dictionary": sorted(offers_dict.values())})

        return vars

    def get_timeout_seconds(self):
        return self.session.config['timeout_time']

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['kicked'] = True
        self.player.leftover_check()




class Leftover(Page):

    def is_displayed(self):
        if self.participant.vars['grouped'] == False and self.participant.vars['kicked'] == False and self.participant.vars['end_game'] == False and self.round_number == 1:
            return True
        elif self.participant.vars['leftover'] == True and self.participant.vars['kicked'] == False and self.participant.vars['end_game'] == False and self.round_number == 1:
            return True
        else:
            return False

    def vars_for_template(self):
        return self.player.vars_for_template()

    def before_next_page(self):
        self.participant.vars['leftover'] = True



class ID(Page):

    def is_displayed(self):
        if self.participant.vars['end_game'] == False and self.group.coalition_formed == True and self.participant.vars[
            'kicked'] == False:
            return True
        elif self.subsession.round_number == Constants.num_rounds and self.participant.vars['end_game'] == False and self.participant.vars['kicked'] == False:
            return True
        elif self.participant.vars['leftover'] == True and self.participant.vars['kicked'] == False and self.participant.vars['end_game'] == False:
            return True
        else:
            return False

    def before_next_page(self):
        self.participant.vars['end_game'] = True


class Kicked(Page):

    def is_displayed(self):
        if self.participant.vars['kicked'] == True:
            return True
        else:
            return False

    def vars_for_template(self):
        return self.player.vars_for_template()

page_sequence = [
    Waitforgroup,
    Groupingconfirmation,
    Sliderinstructions,
    Slider,
    EndRound1,
    Slider2,
    EndRound2,
    Slider3,
    Waitforparticipants,
    PositionAssignment,
    AssignedPosition,
    InstructionsCoalitions,
    ComprehensionCheck,
    ComprehensionCheck2,
    ComprehensionCheck3,
    BargainingStarts,
    NewRound,
    PhaseI,
    WaitForOffers,
    OffersMade,
    PhaseII,
    WaitForSelection,
    OffersSelected,
    PhaseIII_Success,
    Payoff,
    PhaseIII_Failure,
    Leftover,
    ID,
    Kicked
]
