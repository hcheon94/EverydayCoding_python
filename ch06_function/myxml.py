#%%
def myxml(tagname) :
    
    return f'<{tagname}></{tagname}>'
# %%
def myxml(tagname,content='') :
    
    return f'<{tagname}>{content}</{tagname}>'
# %%
def myxml(tagname,content='', **kwargs) :
    attrs = ''.join([f' {key}="{value}"' for key,value in kwargs.items()])
    
    return f'<{tagname}{attrs}>{content}</{tagname}>'
# %%
