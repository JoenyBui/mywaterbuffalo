UNASSIGNED = 0
FILL_IN_THE_BLANK = 1
TRUE_OF_FALSE = 2
MULTIPLE_CHOICE = 3
PROBLEM_SET = 4
SHORT_ANSWER = 5
MULTIPLE_ANSWER = 6
WORD_PROBLEM = 7

QUESTION_CHOICES = (
    (UNASSIGNED, 'Unassigned'),
    (FILL_IN_THE_BLANK, 'Fill in the Blank'),
    (TRUE_OF_FALSE, 'True or False'),
    (MULTIPLE_CHOICE, 'Multiple Choice'),
    (PROBLEM_SET, 'Problem Set'),
    (SHORT_ANSWER, 'Short Answer'),
    (MULTIPLE_ANSWER, 'Multiple Answer'),
    (WORD_PROBLEM, 'Word Problem')
)

QUESTION_DICT = {}
for id, value in QUESTION_CHOICES:
    QUESTION_DICT[id] = value
