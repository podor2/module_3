import random


def get_numbers_ticket(min, max, quantity):

    lottery_numbers = set()

    if min < 1 or max > 1000 or quantity <= 0:
        return lottery_numbers

    while len(lottery_numbers) != quantity:
        lottery_numbers.add(random.randint(min, max))

    return sorted(lottery_numbers)
