#%%

from freedonia import calculate_tax

import testModule as tm
tax_at_12noon = calculate_tax(100,'Harpo',12)
tax_at_9pm = calculate_tax(100,'Harpo',21)

print(f'You owe a total of : {tax_at_12noon}')
print(f'You owe a total of : {tax_at_9pm}')
print(tm.a)
# %%
import testModule as tm
print(tm.c)
# %%
