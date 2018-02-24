#Assignment based on http://www.nasdaq.com/quotes/
#Feel free to use any libraries. 
#Make sure that the output format is perfect as mentioned in the problem.
#Also check the second row of the download dataset.
#If it follows a different format, avoid it or remove it.

#Vail Dorchester

import argparse
import pandas as pd
import numpy as np

def normalization ( fileName , normalizationType , attribute):
    '''
    Input Parameters:
        fileName: The comma seperated file that must be considered for the normalization
        attribute: The attribute for which you are performing the normalization
        normalizationType: The type of normalization you are performing
    Output:
        For each line in the input file, print the original "attribute" value and "normalized" value seperated by <TAB> 
    '''
    #TODO: Write code given the Input / Output Paramters.
    path = './'+str(fileName)#set the path
    df = pd.read_csv(path)
    #if they want min max normalization
    if(normalizationType == 'min_max'):#min max
        #get the min max and make a list
        ma = df[attribute].max()#get max
        mi = df[attribute].min()#get min
        normalized_col = []#list
        #calculate norm for each value
        for val in df[attribute]:#go down rows of that attribute
            n = ((val-mi)/(ma-mi))*(1-0)+(0)#norm value
            normalized_col.append(n)#adding to list
            print("{0:.3f}\t{1:.3f}".format(val, n))#print it
        #add these to the dataframe for later use?    
        df['normalized_'+str(attribute)] = normalized_col#append the norms to the df
    #if they want z_score normalization    
    elif(normalizationType=='z_score'):#z score
        #calculate standard dev, mean, and make a norm col
        std = df[attribute].std()#get standard
        mean = df[attribute].mean()#mean
        normalized_col = []#list
        #calc each norm value
        for val in df[attribute]:#
            n = (val-mean)/std#calc that value
            normalized_col.append(n)#add it to the list
            print("{0:.3f}\t{1:.3f}".format(val, n))#print it
        #add it to the dataframe for later use?    
        df['normalized_'+str(attribute)] = normalized_col#add it to the dataframe
    #if one of these normalization methods wasn't selected then print this    
    else:
        print("Not a valid normalization method.")

def correlation ( attribute1 , fileName1 , attribute2, fileName2 ):
    '''
    Input Parameters:
        attribute1: The attribute you want to consider from file1
        attribute2: The attribute you want to consider from file2
        fileName1: The comma seperated file1
        fileName2: The comma seperated file2
        
    Output:
        Print the correlation coefficient 
    '''
    #TODO: Write code given the Input / Output Paramters.
    path1 = './'+str(fileName1)#set the paths
    path2 = './'+str(fileName2)#set the paths
    df1 = pd.read_csv(path1)#load the dfs
    df2 = pd.read_csv(path2)#load the dfs

    #now get standard deviations and means for calculations
    std1 = df1[attribute1].std()
    std2 = df2[attribute2].std()
    mean1 = df1[attribute1].mean()
    mean2 = df2[attribute2].mean()
    #calculating correlation coefficient r
    r = np.sum([df1[attribute1]*df2[attribute2]])
    r = r - df1[attribute1].count()*(mean1*mean2)
    r = r/(df1[attribute1].count()*std1*std2)
    print(r)
    #didn't use the stuff below, but i'm keeping it because it is helpful for me
    #combine the attributes we want to compare into one frame i guess
    #combined_frames = pd.concat([df1[attribute1], df2[attribute2]], axis=1, keys=[attribute1, attribute2])
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f1', type=str,
                            help="Location of filename1. Use only f1 when working with only one file.",
                            required=True)
    parser.add_argument("-f2", type=str, 
                            help="Location of filename2. To be used only when there are two files to be compared.",
                            required=False)
    parser.add_argument("-n", type=str, 
                            help="Type of Normalization. Select either min_max or z_score",
                            choices=['min_max','z_score'],
                            required=False)
    parser.add_argument("-a1", type=str, 
                            help="Type of Attribute for filename1. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    parser.add_argument("-a2", type=str, 
                            help="Type of Attribute for filename2. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    
    args = parser.parse_args()
    
    if ( args.n and args.a1 ):
        normalization( args.f1 , args.n , args.a1 )
    elif ( args.f2 and args.a1 and args.a2):
        correlation ( args.a1 , args.f1 , args.a2 , args.f2 )
    else:
        print("Kindly provide input of the following form:\nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -n <normalizationType> \nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -f2 <filename2> -a2 <attribute>")
