from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
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
        'timeout_time': 5 * 60,
        'earned': False,
        'slider_time': 30,
        'comprehension_check': True,
        'leave_matching': True,
        'leave_timer': 1 * 60,
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
        'timeout_time': 5 * 60,
        'earned': False,
        'slider_time': 30,
        'comprehension_check': True,
        'leave_matching': True,
        'leave_timer': 1 * 60,
    },

]

ROOMS = [
    dict(
        name='Lab1',
        display_name='Lab 1',
        participant_label_file='Lab1.txt',
        use_secure_urls=True
        ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = ''

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

EXTENSION_APPS  = []