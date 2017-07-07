# prawidlowe zastosowanie lambdy to uzycie jej jako argument jakiejs funkcji

from utils.smart_wait import wait_until

import random

def get_current_value():
    return random.randint(1, 100)

wait_until(condition=lambda: get_current_value() == 22)