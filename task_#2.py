import random


def get_numbers_ticket(min, max, quantity):

    lottery_numbers = set()
    condition = not( min < 1 or max > 1000 or quantity <= 0 or quantity > max - min or min > max) 
    if condition :
        try:
            while len(lottery_numbers) != quantity:
                lottery_numbers.add(random.randint(min, max))
        except ValueError :
            pass
                
    return lottery_numbers

    

    
    

print(get_numbers_ticket(5,9,3))