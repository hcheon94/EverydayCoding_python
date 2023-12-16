#%%
def transform_value(func,dict):
    return {key : func(value)
            for key,value in dict.items()
        
    }
# %%
