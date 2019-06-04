#0.

import os
import re
import nltk
import string
import pandas as pd
from read_write_create import *


global cwd, path, data_path

cwd = os.getcwd()
path = cwd
data_path = cwd + "/data"

stopwords = read_list_from_file(path, "stopwords.txt")

print("create-position-info-sCake")
for every_file in (os.listdir(data_path)):
    
    print(every_file)
    text = read_text_from_file(data_path,every_file)
    
    ## pre-processing text
    
    text = text.strip()
    text = text.lower()
    
    numbers_ex = re.compile("[0-9]+(-[0-9]+)?")
    text = re.sub(numbers_ex, '', text)
    
    #hyphen_ex = re.compile("[-]")
    #text = re.sub(hyphen_ex, ' ', text)
    
    #text = text.translate(None, string.punctuation)
    punctuation_ex = re.compile("[^a-z ]")
    text = re.sub(punctuation_ex, '', text)
    
    roman_num_ex = re.compile("\\b[i|v|x|l|c|d|m]{1,3}\\b")
    text = re.sub(roman_num_ex, '', text)
    
    words = nltk.word_tokenize(text)
    words = [i for i in words if i not in stopwords]
    
    selected_words = list(set(words))
    
    ## end of pre-processing
    
    N = len(words) +1
    posi = list()
    t = list()
    tf = list()
    
    for w in selected_words:
        
        posw = [i for i, word in enumerate(words) if w == word]
        w_freq = len(posw)+1
        
        posw.append(N)
        
        t.append(w)
        tf.append(w_freq)
        
        posi.append(posw)
  
    #print(posi)
    
    data = dict()
    data["words"] = t
    data["tf"] = tf
    data["positions"] = posi
    
    df = pd.DataFrame(data=data)
    print(df)
    
    df.to_pickle(cwd+"/graphs/"+every_file[:-4]+".pkl")
    
    
    
    
    
    
    
    
    
    
    
