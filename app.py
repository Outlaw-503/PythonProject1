import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d=st.container()
with d:
    data=pd.read_csv("googleplaystore.csv")
    data.drop_duplicates(inplace=True)
    l=[]
    l1=[]
    data["Reviews"]=pd.to_numeric(data["Reviews"],errors='coerce')
    def c(x):
        if("M" in x):
            return float(x[:-1])*1024
        elif("K" in x):
            return float(x[:-1])
    data["Size"]=data["Size"].apply(c)
    data.Installs.dropna(inplace=True
    def a(x):
        if('+' in x):
            return float(x[:-1].replace(",",''))
        
    data["Installs"]=data["Installs"].apply(a)
    def c(x):
        if("and up" in str(x)):
            return str(x[:-6])
        else:
            pass
    data["Android Ver"]=data["Android Ver"].apply(c)
    data["Current Ver"]=data["Current Ver"].apply(c)
    import seaborn as sns
    plt.scatter(data["Size"],data["Reviews"])
    st.write(plt.show())
    
