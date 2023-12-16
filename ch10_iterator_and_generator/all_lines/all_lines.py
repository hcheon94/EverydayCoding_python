#%%
import os 
def all_lines(path) :
    for filename in os.listdir(path) :
        full_filename = os.path.join(path,filename)
        try :
            for line in open(full_filename):
               yield line
        except :
            pass
# %%
all_line_test=all_lines('C:/Users/user/PycharmProject/verydayCoding/ch10_iterator_and_generator/all_lines')
# %%
print(all_line_test)
# %%
for one_line in all_line_test :
    print(one_line)
# %%
