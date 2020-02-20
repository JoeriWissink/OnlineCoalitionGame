# OnlineCoalitionGame
An oTree application for three-player coalition formation research

# **Description**

The Online Coalition Game (OCG) has been developed for conducting (online) three-player simple weighted majority games. This documentation contains a guide on how to install the program, use it for research, and describes the adjustable parameters and key output variables. For a basic guide on how to install and use oTree (Chen, Schonger, & Wickens, 2016)—the platform on which the game runs—extensive oTree documentation can be found here: https://otree.readthedocs.io/en/latest/

# **Installation**

1. Installing oTree and starting a new project (see oTree documentation: https://otree.readthedocs.io/en/latest/).

2.Copy the folders Online_Coalition_Game, Online_Coalition_Game_Alternative_Offer, Online_Coalition_Game_Introduction, and Online_Coalition_Game_ _Alternative_Offer_Introduction to your project folder.

3. Copy and paste the following session configurations into your own settings.py file.


```SESSION_CONFIGS = [
        {
            'name': 'Online_Coalition_Game_One_Step',
            'display_name': "Online Coalition Game One-Step Protocol",
            'num_demo_participants': 3,
            'app_sequence': ['Online_Coalition_Game_Introduction', 'Online_Coalition_Game'],
            'resources_player_A': 4,
            'resources_player_B': 3,
            'resources_player_C': 2,
            'decision_point': 5,
            'grand_coalition': False,
            'total_payoff': 100,
            'payoff_conversion': 0.05,
            'incentives': True,
            'base_fee': 1.00,
            'select_none': False,
            'timeout_time': 60 * 5,
            'earned': False,
            'slider_time': 30,
            'comprehension_check': True,
        },
        {
            'name': 'Online_Coalition_Game_Alternative_Offer',
            'display_name': "Online Coalition Game Dynamic Protocol",
            'num_demo_participants': 3,
            'app_sequence': ['Online_Coalition_Game_Alternative_Offer_Introduction', 'Online_Coalition_Game_Alternative_Offer'],
            'resources_player_A': 4,
            'resources_player_B': 3,
            'resources_player_C': 2,
            'decision_point': 5,
            'grand_coalition': False,
            'total_payoff': 100,
            'payoff_conversion': 0.05,
            'incentives': True,
            'base_fee': 1.00,
            'select_none': False,
            'timeout_time': 60 * 5,
            'earned': False,
            'slider_time': 30,
            'comprehension_check': True,
        },

    ]


To make sure participants can skip to the end of the study if they cannot be matched into a group within a specified amount of time, install the otree_mturk_utils (available on the OCG GitHub page and https://github.com/chapkovski/custom-waiting-page-for-mturk) as well as in the OCG GitHub page. NB: The current version of otree_mturk_utils is not compatible with oTree 2.3 and higher. Although this is not problematic—all features of the OCG are functional on older versions of oTree—otree_mturk_utils is likely to be updated to work with the newest version of oTree.
