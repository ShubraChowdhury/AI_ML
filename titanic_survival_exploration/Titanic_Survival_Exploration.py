# -*- coding: utf-8 -*-
"""
Created on Tue May 03 13:25:48 2016

@author: DevAdmin
"""

import numpy as np
import pandas as pd

# RMS Titanic data visualization code 
from titanic_visualizations import survival_stats
from IPython.display import display


# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
display(full_data.head())

outcome = full_data['Survived']

print(outcome)

"""axis=1 denotes that we are referring to a column, not a row """
data = full_data.drop('Survived', axis =1)

display(data.head())

""" Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
The axis labels are collectively referred to as the index.
 pd.Series(data, index=index) 

np.ones(5) generates an array of 1 
 """

def accuracy_score(truth, pred):
    
    if(len(truth)== len(pred)):
        
        return " Accuracy = {:.1f}%.".format((truth == pred).mean()*100)
    else:
        return " Wrong comparison "
        



#print(pd.Series(np.ones(5)))

#print('\n Outcome:-', outcome[:5], '\n Prediction:-', predictions)

predictions = pd.Series(np.ones(5, dtype = int))
print('Prediction for 1 :-',accuracy_score(outcome[:5],predictions))


""" Prediction for Failure """
failurepredictions = pd.Series(np.zeros(5, dtype = int))
print('Prediction for 0 :-', accuracy_score(outcome[:5],failurepredictions))


def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    
    for _, passenger in data.iterrows():
        
        # Predict the survival of 'passenger'
        predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_0(data)
#print (predictions)
#def predictions_1(data):
#    """ Model with no features. Always predicts a passenger did not survive. """
#
#    pass_predictions = []
#    
#    for _, passenger in data.iterrows():
#        
#        # Predict the survival of 'passenger'
#        pass_predictions.append(1)
#    
#    # Return our predictions
#    return pd.Series(pass_predictions)
#
## Make the predictions
#pass_predictions = predictions_1(data)
#
#
#
#print ('Failure Prediction:-',accuracy_score(outcome, predictions))
#print ('Success Prediction:-',accuracy_score(outcome, pass_predictions))


survival_stats(data, outcome, 'Sex')



def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    #from titanic_visualizations import filter_data
    #print(filter_data(data,"Sex == 'female'"))
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        #pass
        
    
     predictions.append(1)
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)



def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    #from titanic_visualizations import filter_data
    #print(filter_data(data,"Sex == 'female'"))
    #data =filter_data(data,"Sex == 'female'")

    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        #pass
     if (passenger['Sex'] == "female"):
         predictions.append(1)
     #print(passenger['Sex'])   
     else:
         predictions.append(0)
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)

print accuracy_score(outcome, predictions)

survival_stats(data, outcome, 'Age', ["Sex == 'male'"])



#survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])

def predictions_2(data):
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        #pass
        if ((passenger['Sex']=="female") ):
            predictions.append(1)
        elif ((passenger['Sex']=='male') and (passenger['Age'] <= 10 )):
            predictions.append(1)
        else:
            predictions.append(0)
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_2(data)

print accuracy_score(outcome, predictions)

survival_stats(data, outcome, 'Pclass', ["Sex == 'female'", "Age < 18"])

def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        #pass
        if ((passenger['Sex'] == "female") and (passenger['Fare'] <> 18) and (passenger['SibSp'] !=8) and (passenger['Cabin'] !="C22 C26") ):
          predictions.append(1)
        elif ((passenger['Sex'] == "male") and (passenger['Age'] <= 10) ):
          predictions.append(1)
        else:
            predictions.append(0)
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data)

print accuracy_score(outcome, predictions)
