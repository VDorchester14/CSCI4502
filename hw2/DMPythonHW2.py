#Assignment based on http://www.nasdaq.com/quotes/
#Feel free to use any libraries. 
#Make sure that the output format is perfect as mentioned in the problem.
#Also check the second row of the download dataset.
#If it follows a different format, avoid it or remove it.

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
    
    if(normalizationType == 'min_max'):#min max
        ma = df[attribute].max()#get max
        mi = df[attribute].min()#get min
        normalized_col = []#list
        for val in df[attribute]:#go down rows of that attribute
            n = ((val-mi)/(ma-mi))*(1-0)+(0)#norm value
            normalized_col.append(n)#adding to list
            print("{0:.3f}\t{1:.3f}".format(val, n))#print it
        df['normalized_'+str(attribute)] = normalized_col#append the norms to the df
    elif(normalizationType=='z_score'):#z score
        std = df[attribute].std()#get standard
        mean = df[attribute].std()#mean
        normalized_col = []#list 
        for val in df[attribute]:#
            n = (val-mean)/std#calc that value
            normalized_col.append(n)#add it to the list
            print("{0:.3f}\t{1:.3f}".format(val, n))#print it
        df['normalized_'+str(attribute)] = normalized_col#add it to the dataframe
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
