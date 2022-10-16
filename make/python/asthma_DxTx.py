'''
Encoding: UTF-8
Title: asthma_Dx_Tx_3.py
Created: 2022-10-15 22:17:29
@author: samantix
'''


# ----------------------------------------------------------
# # * Asthma Assessment via GINA criteria
# ----------------------------------------------------------

# ! ----------------------------------------------------------


# * asthma_control_factors v4 (type-casting keyword changed to string 2/2 problematic O/P)

asthma_control_factors = {
    'A4': ['currently symptomatic (True/False)', "bool", None],
    'A5': ['daytime asthma Sx per week (integer)', "int", None],
    'A6': ['rescue inhaler uses per week (integer)', "int", None],
    'A7': ['asthmatic-awakening ≥1 per month (True/False)', "bool", None],
    'A8': ['asthma-limited physical activity (True/False)', "bool", None],
    'A9': ['≥1 annual exacerbation (True/False)', "bool", None],
    'A10': ['asthma triggers (True/False)', "bool", None],
    'A11': ['atopy (personal or FMH) (True/False)', "bool", None],
    'A12': ['characteristic musical wheezing on PE (True/False)', "bool", None],
    'A15': ['alternative Dx have been excluded (True/False)', "bool", None]
}

# * asthma_exacerbation_risk_factors v2

asthma_exacerbation_risk_factors = {
    "A17": ["tobacco smoke exposure (True/False)", "bool", None],
    "A18": ["sensitized allergen exposure (True/False)", "bool", None],
    "A19": ["previous asthma-induced intubation or ICU admission (True/False)", "bool", None],
    "A20": ["low FEV1 (especially <60% predicted) (True/False)", "bool", None],
    "A21": ["obesity (True/False)", "bool", None],
    "A22": ["food allergy (True/False)", "bool", None],
    "A23": ["chronic rhinosinusitis (True/False)", "bool", None],
    "A24": ["poor adherence/inhaler technique (True/False)", "bool", None]
}

# pack both sets of questions into a tuple; AND
#   map a single dict comprehension expression to both Q banks via lambda.
asthma_factors = asthma_control_factors, asthma_exacerbation_risk_factors

# ----------------------------------------------------------

# todo: format user input: strip white space, capitalize booleans, etc.


def assess_asthma(d):
    '''
    # * records asthma assessment
    # iterating through both dicts passed as tuple;
    # using 0th val indices as user prompts;
    # using 1st val indices to typcast 3rd val, via eval()
    '''
    return list(map(lambda n: {k: [v[0], v[1], eval(v[1])(input(f"{v[0]}: "))]
                               for k, v in n.items()}, d))
    # ----------------------------------------------------------


# ! ----------------------------------------------------------


# todo: review implementation

# asthma_exacerbation = {
#     "sx": [
#         "breathlessness",
#         "wheezing",
#         "cough",
#         "chest_tightness",
#         "worsened_exercise_intolerance"
#     ],
#     "severity": [
#         "provoked by exertion",
#         "present at rest",
#         "sx-related sleep disturbance"
#     ]
# }

# print(asthma_exacerbation)
# FEV1/FVC is normal if > 5th %ile (i.e., > z-score of -1.645)

# ! ----------------------------------------------------------

# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @


# * Display results of asthma assessment
print(assess_asthma(asthma_factors))
