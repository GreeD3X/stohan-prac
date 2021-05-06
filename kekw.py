import os
import sys
sys.path.insert(0, os.path.abspath('robust-fpm-cmc-msu-edu-2021-master'))
from robustfpm.finance import make_option

option1 = make_option(option_type='putonmax', strike=90)
print('Option 1: {}'.format(option1))
print('Option 1 payoff at x = 80, 90, and 100, t = 3: {}'.format(option1.payoff([[80], [90], [100]], 3)))