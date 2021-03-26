import csv
import re
import pandas as pd
import numpy as np

def return_method(string):

    method = string[ 0 : 3 ]
    
    if method == "GET":
        return 0
    elif method == "POS":
        return 1
    else:
        return 2

def count_keywords(string):

    keywords = 0
    
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("AND"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("ALL"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("AS"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("INJ"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("ECT"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("OR"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("PG"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("CAT"), string.upper()))
    keywords += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("CHAR"), string.upper()))

    keywords += string.upper().count('DOCUMENT')
    keywords += string.upper().count('COOKIE')
    keywords += string.upper().count('DROP')
    keywords += string.upper().count('UNION')
    keywords += string.upper().count('ORDER BY')
    keywords += string.upper().count('FROM')
    keywords += string.upper().count('WAPITI')
    keywords += string.upper().count('SELECT')
    keywords += string.upper().count('SLEEP')
    keywords += string.upper().count('NULL')
    keywords += string.upper().count('INJECT')
    keywords += string.upper().count('SCRIPT')
    keywords += string.upper().count('ALERT')
    keywords += string.upper().count('INFORMATION_SCHEMA')
    keywords += string.upper().count('WHERE')
    keywords += string.upper().count('CASE')
    keywords += string.upper().count('WHEN')
    keywords += string.upper().count('HAVING')
    keywords += string.upper().count('PASSWORD')
    keywords += string.upper().count('ROOT')
    keywords += string.upper().count('XP_CMDSHELL')
    keywords += string.upper().count('XP_REGREAD')
    keywords += string.upper().count('WAIT')
    keywords += string.upper().count('DELAY')
    keywords += string.upper().count('SQL')
    keywords += string.upper().count('BENCHMARK')
    keywords += string.upper().count('LIKE')
    keywords += string.upper().count('TIME')
    keywords += string.upper().count('ADMIN')
    keywords += string.upper().count('EXEC')
    keywords += string.upper().count('TRUE')
    keywords += string.upper().count('FALSE')
    keywords += string.upper().count('FETCH')
    keywords += string.upper().count('PING')
    keywords += string.upper().count('PRINT')
    keywords += string.upper().count('TABLE')

    return keywords
    
# Python program to count the number of
# Special Characters in a string. 
# codespeedy.com

def count_special_character(string): 
  
    # Declaring variable for special characters 
    special_char= 0
   
    for i in range(0, len(string)):  
    # len(string) function to count the 
    # number of characters in given string.
      
        ch = string[i]
  
        #.isalpha() function checks whether character 
        #is alphabet or not.

        if (string[i].isalpha()):  
            continue
        
        #.isdigit() function checks whether character 
        #is a number or not.
        elif (string[i].isdigit()):
            continue
            
        else: 
            special_char += 1
            
            
    return special_char
  

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def parseFile(file):
    fin = open(file)

    lines=fin.readlines()

    res=[]
    tot=[]

    for i in range(len(lines)):
        line = lines[i].strip()

        if line.startswith("GET"):

            for k in range (0,11):
                res.append(lines[k+i])
                    
            res = listToString(res)
            res = res.replace(" ","")
            res = res.rstrip()
            #res = re.sub(r"[\t\s]*", "", res)

            tot.append(res)
            res = []

        elif line.startswith("POST"):
                
            for k in range (0,15):
                res.append(lines[k+i])  
                      
            res = listToString(res)
            res = res.replace(" ","")
            res = res.rstrip()
            #res = re.sub(r"[\t\s]*", "", res)

            tot.append(res)
            res = []
            
        elif line.startswith("PUT"):
            
            for k in range (0,15):
                res.append(lines[k+i])
                         
            res = listToString(res)
            res = res.replace(" ","")
            res = res.rstrip()
            #res = re.sub(r"[\t\s]*", "", res)

            tot.append(res)
            res = []
            
    return tot

def calcFeatures(list_of_strings,malicious):
    single_feature = []
    total_feature = []
    
    for i in list_of_strings:
        #method 
        single_feature.append(return_method(i))

        #number of special characters
        single_feature.append( count_special_character(i)/len(i)   )

        #number of letters 
        single_feature.append(   sum(c.isalpha() for c in i)/len(i)      )

        #number of digits
        single_feature.append(   sum(c.isdigit() for c in i)/len(i)      )
         
        #number of keywords
        single_feature.append(count_keywords(i)/len(i))

        #len of first line
        first, _, _ = i.partition('\n')
        single_feature.append( len(first)/len(i)   )

        #threat
        if malicious == 0:
            single_feature.append(0)
        elif malicious == 1:
            single_feature.append(1)

        total_feature.append(single_feature)
        single_feature = []

    return total_feature

def combineFeatures(f1,f2,f3,labels):
    all_features = f1 + f2 + f3
    all_features.insert(0,labels)
    return all_features

def writeToCSV(all_features):
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(all_features)
        
n1 = parseFile("normalTrafficTraining.txt")
n2 = parseFile("anomalousTrafficTest.txt")
n3 = parseFile("normalTrafficTest.txt")

f1 = calcFeatures(n1,0)
f2 = calcFeatures(n2,1)
f3 = calcFeatures(n3,0)

labels = ["method","number of special characters","number of letters","number of digits","number of keywords","len of first line","threat"]
all_features = combineFeatures(f1,f2,f3,labels)

writeToCSV(all_features)

df = pd.read_csv("output.csv")
df.head()
