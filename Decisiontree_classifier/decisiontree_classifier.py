'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    entropy = 0
    
    if df.empty :
    	return entropy
    
    last_colm = df.columns[-1]
    tar = df[last_colm].unique()
    
    for i in tar:
    	a = df[last_colm].value_counts()[i]
    	b = len(df[last_colm])
    	p = a/b
    	q = 1-p
    	entropy = -(p* np.log2(p) + q* np.log2(q))
    
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):

    entropy_of_attribute=0
    
    if df.empty:
       return entropy_of_attribute
    
    try:
       last_colm=df.columns[-1]
       
       tar=df[last_colm].unique()
       
       attr_value=df[attribute].unique()
       
       for i in attr_value:
          entropy_of_feature=0
          pi_den=len(df[attribute][df[attribute]== i])
          
          for j in tar:
          
             pi_num=len(df[attribute][df[attribute]==i][df[last_colm]== j])
          
             pi=pi_num/pi_den
          
             if(pi==0):
                continue
             entropy_of_feature += -(pi*np.log2(pi))
          entropy_of_attribute += (((pi_den/len(df))*entropy_of_feature))  
         
    except KeyError:
           print("Attribute: ",attribute, "not in database")
           
        
    return entropy_of_attribute


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    information_gain=0
    
    try:
        
        info_gain = get_entropy_of_dataset(df) - get_avg_info_of_attribute(df,attribute)
    except KeyError:
         print("Attribute: ",attribute,"not in dataset")
    return info_gain




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    colm = ''
    info_gains = {}
    info_gain_max = float("-inf")
    for i in df.columns[:-1]:
        info_attr= get_information_gain(df, i)
        if info_attr > info_gain_max:
            colm = i
            info_gain_max = info_attr
        info_gains[i] = info_attr
    return (info_gains, colm)
