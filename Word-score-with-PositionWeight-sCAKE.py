#3.

import os
import numpy as np
import pandas as pd
from read_write_create import *

global cwd, path, data_path

cwd = os.getcwd()
path = cwd
data_path = cwd + "/data"
word_score_path = cwd + "/SCScore/"

print("Word-score-with-PositionWeight-sCake")
for every_file in (os.listdir(data_path)):
    
    print(every_file)
    file_name = every_file[:-4]
    #text = read_text_from_file(data_path,every_file)
    
    df = pd.read_csv(word_score_path + file_name  +".csv.sortedranked.IF.txt")
    df = df.drop(['IFDenseRank','IFMinRank'], axis=1)
    df.columns = ['Word', 'SCScore']
    #print(df)
    
    df.to_csv(cwd+"/SCScore_W/"+ file_name +"_ranked_list.csv")
     
