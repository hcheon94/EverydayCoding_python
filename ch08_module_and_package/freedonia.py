#%%
RATES = {
    'Chico' : 0.5,
    'Groucho' : 0.7,
    'Harpo' : 0.5,
    'Zeppo' : 0.4
    
}
def time_percentage(hour):
    return hour/24

def calculate_tax(amount,state,hour):
    return amount +(amount*RATES[state]*time_percentage(hour))

print(calculate_tax(500,'Harpo',12))
# %%
#Demical을 활용한 형태
from decimal import Decimal

rates = {
    'Chico' : Decimal('0.5'),
    'Groucho' : Decimal('0.7'),
    'Harpo' : Decimal('0.5'),
    'Zeppo' : Decimal('0.4')
}

def time_percentage(hour):
    return hour/Decimal('24.0')

def calculate_tax(amount,state,hour) :
    return float(amount + (amount*rates[state]*time_percentage(hour)))
# %%
class HourTooLowError(Exception) : pass
class HourTooHighError(Exception) : pass

RATES = {
    'Chico' : 0.5,
    'Groucho' : 0.7,
    'Harpo' : 0.5,
    'Zeppo' : 0.4
    
}
def time_percentage(hour):
    return hour/24

def calculate_tax(amount,state,hour):
    if hour <0 :
        raise HourTooLowError(f'Hour of {hour} is < 0')
    if hour >=24 :
        raise HourTooLowError(f'Hour of {hour} is >= 24')
    
    return float(amount + (amount*rates[state]*time_percentage(hour)))