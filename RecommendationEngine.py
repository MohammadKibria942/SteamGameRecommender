import pandas as pd
import PySimpleGUI as sg


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

##Path for the steam data
path = "FinalData/steam_clean.csv"
descriptionPath = "Exports/steam_description_data.csv"

pd.set_option("display.max_columns", 100)

ds = pd.read_csv(path, encoding = "ISO-8859-1")
descriptionDs = pd.read_csv(descriptionPath, encoding = "ISO-8859-1")


##Transforms text to feature vectors which can be used as input
##TF-IDF means term frequency, IDF is inverse docuemnt frequency
##It defines how important a word is by how manmy times it appears in the docuemnt
##it also checks how many times the word appears in other documents

tf = TfidfVectorizer(analyzer = "word", ngram_range = (1, 1), min_df = 0.0, stop_words = "english")
tfidf_matrix = tf.fit_transform(ds["tags"])


##Measures the similarity between two vectors and the distance between them, measures similarity in text analysis
cosineSimilarities = linear_kernel(tfidf_matrix, tfidf_matrix)

##Create an empty list for the results of the filter
results = {}

##Sorts the similarities between the entered games and the games in the csv file
##Adds the appid of the game that is coing to be reccommended into the array
for idx in range(len(ds)):
    similarIndicies = cosineSimilarities[idx].argsort()[:-100:-1]
    similarItems = [(cosineSimilarities[idx][i], ds["appid"].iloc[i]) for i in similarIndicies]
    results[ds["appid"].iloc[idx]] = similarItems[1:]



def item(appid):
    ##gets the appid for the current game

    return ds.loc[ds["appid"] == appid, "name"].tolist()[0]


def description(appid):
    ##gets the dedscription for the current game

    return descriptionDs.loc[descriptionDs["steam_appid"] == appid, "short_description"].tolist()[0]

##Calls the gui program for the user input
import gui

##Creates empty lists
reviewList2 = []
priceList2 = []
gameList2 = []
tupList = []
recommendedList = []

def recommend(item_id, num):
    recs = results[item_id][:num]
    for rec in recs:
        gameList2.append(item(rec[1]))

        # Check the game being recommended to every game in the csv file to find the price and review rating
        # Once the price and review rating are found, they will be added to the list
        for i in range(len(gameList2)):
            for j in range(len(ds.name)):
                if gameList2[i] == ds.name[j]:
                    priceList2.append(ds.price[j])
                    reviewList2.append(ds.review_rating[j])
                    break

        # Convert the elements from priceList2 from tuple to string
        # Check the price length and add the price to the list
        tupList.clear()  # Clear the list before populating it
        for tup in priceList2:
            tup_str = str(tup)
            if len(tup_str) == 4:
                tup_str = "£" + tup_str[0] + "," + tup_str[2:]
            elif len(tup_str) == 3:
                tup_str = "£" + tup_str[0] + "," + tup_str[1:]
            elif len(tup_str) == 2:
                tup_str = "0." + tup_str
            elif len(tup_str) == 1:
                tup_str = "£0.0" + tup_str
            else:
                tup_str = "£" + tup_str + ".00"
            tupList.append(tup_str)

        # Check if lists have elements before accessing their indices
        if tupList and reviewList2:
            recommendedList.append("Recommended: " + item(rec[1]) + " | Price: " + tupList[0] + " | Rating: " + str(reviewList2[0]) + "/10\n\n" + description(rec[1]) + "\n\n" + "..................................................................................................\n")


        # Clear all of the arrays
        gameList2.clear()
        priceList2.clear()
        reviewList2.clear()

    


    ##Print out the results in order of:
    # Recommended games
    # Prices
    # Review ratings

    sg.popup_scrolled("Recommending " + str(num) + " products similar to " + item(item_id) + "...\n" + "..................................................................................................\n"
                      , *recommendedList, size = (75, 15), title = "Recommended Games", font = "10")

    ##Clears the recomended games form the list
    recommendedList.clear()

##Determines the number of games recommended per game inputted
##Calls the recommended function to publish the fames in the pop up window
for i in range(len(gui.appidList)):
    recommend(item_id = (gui.appidList[i]), num = 10)
    print()

