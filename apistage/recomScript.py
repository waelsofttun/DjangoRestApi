from pathlib import Path
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.conf import settings
import os.path
# loading the data from the csv file to apandas dataframe



def recomndationSystem(offer_name):

    print(offer_name)
    offer_data = pd.read_csv('C:/Users/21620/OneDrive/Bureau/Projects/RestApi/restapistage/apistage/BANGALORE.csv')


    i=0
    for index, row in offer_data.iterrows():

        row['_id']=i
        i=i+1
# selecting the relevant features for recommendation
    selected_features = ['profile','company','Location','Stipend','Duration','Offer','Skills and Perks']
    for feature in selected_features:

        offer_data[feature] = offer_data[feature].fillna('')
    combined_features = offer_data['profile']+' '+offer_data['company']+' '+offer_data['Location']+' '+offer_data['Stipend']+' '+offer_data['Duration']+' '+offer_data['Offer']+' '+offer_data['Skills and Perks']
# converting the text data to feature vectors
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
# getting the similarity scores using cosine similarity

    similarity = cosine_similarity(feature_vectors)
# getting the profile name from the user

    
    list_of_all_profiles = offer_data['profile'].tolist()
    find_close_match = difflib.get_close_matches(offer_name, list_of_all_profiles)
    try :
        close_match = find_close_match[0]
    except :
        return {}
    index_of_the_offer = offer_data[offer_data.profile == close_match]['_id'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_offer]))
    sorted_similar_offer = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
    responsedata={}
    i = 1
    for offer in sorted_similar_offer:

        index = offer[0]
        offer_from_index = offer_data[offer_data.index==index]['profile'].values[0]
        if (i<10):
            responsedata[i]=offer_from_index
            i+=1
    return  responsedata    
        