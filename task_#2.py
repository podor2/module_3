import random


def get_numbers_ticket(min, max, quantity):

    lottery_numbers = set()
    condition = not (1 < min < max < 1000 and quantity <= max - min)
    if condition :
        try:
            while len(lottery_numbers) != quantity:
                lottery_numbers.add(random.randint(min, max))
        except ValueError :
            pass
                
    return sorted(list(lottery_numbers))

    

