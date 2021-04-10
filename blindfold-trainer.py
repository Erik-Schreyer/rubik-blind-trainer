#!/python3

import os
import sys
import matplotlib.pyplot as plt
from pandas_ods_reader import read_ods

def getDataFrame(database):
    if database == "default":
        dataframeSource = os.path.abspath(os.path.join(os.path.dirname(__file__), "BlindMemo.ods"))
    else :
        dataframeSource = os.path.isfile(database)
    df = read_ods(dataframeSource, 1)
    dfEdges = df[df['Type'] == 'Edge']
    dfCorners = df[df['Type'] == 'Corner']
    #print(dfEdges)
    #print(dfCorners)
    return dfCorners, dfEdges

def train(dataframe) :

    dfSample = dataframe.sample(n=4)
    #print(dfSample)
    imgArray = []
    for index, row in dfSample.iterrows():
        print(row['Type'], row['StickerIdent']+'.jpg')
        imagePath = os.path.abspath(os.path.join(os.path.dirname(__file__), row['Type'],row['StickerIdent']+'.jpg'))
        img = plt.imread(imagePath, format='jpeg')
        imgArray.append(img)
        plt.imshow(img)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.show()

    f, axarr = plt.subplots(2,2)
    axarr[0,0].imshow(imgArray[0])
    axarr[0,0].axes.xaxis.set_visible(False)
    axarr[0,0].axes.yaxis.set_visible(False)
    axarr[0,0].set_title(dfSample['Name'].iloc[0])

    axarr[0,1].imshow(imgArray[1])
    axarr[0,1].axes.xaxis.set_visible(False)
    axarr[0,1].axes.yaxis.set_visible(False)
    axarr[0,1].set_title(dfSample['Verb'].iloc[1])

    axarr[1,0].imshow(imgArray[2])
    axarr[1,0].axes.xaxis.set_visible(False)
    axarr[1,0].axes.yaxis.set_visible(False)
    axarr[1,0].set_title(dfSample['Adjective'].iloc[2])

    axarr[1,1].imshow(imgArray[3])
    axarr[1,1].axes.xaxis.set_visible(False)
    axarr[1,1].axes.yaxis.set_visible(False)
    axarr[1,1].set_title(dfSample['Object'].iloc[3])

    plt.show()
    return

if __name__=="__main__":
    database = input("Please enter the full/path/to/ods or \"default\" to use the provided file:\n")
    dfCorners,dfEdges = getDataFrame(database)
    while True :
        trainingType = input("Do you want to train corners (Enter \"c\"), edges (Enter \"e\"), or exit (Enter \"x\")?\n")
        cont = 'y'
        if trainingType == "c" :
            while cont=='y' :
                train(dfCorners)
                cont = input("Do you want to continue (y/n)?\n")
        elif trainingType == "e" :
            while cont=='y' :
                train(dfEdges)
                cont = input("Do you want to continue (y/n)?\n")
        elif trainingType == "x" :
            break
        else :
            print("Not a valid option.")
