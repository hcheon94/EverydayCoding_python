#%%
list = [[1,2],[3,4]]
def flatten(mylist) :
    return [one_element 
     for one_sublist in mylist
     for one_element in one_sublist]
# %%
print(flatten(list))
# %%
def flatten_odd_ints (mylist) :
    
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist 
            if (one_element%1==0 and type(one_element)==int )]
# %%
