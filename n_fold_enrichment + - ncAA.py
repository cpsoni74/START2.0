# at least n-fold diff between +Uaa and -Uaa

import pandas as pd
import csv

inputfile = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/peptoid_avg_en_noncAA_PB.csv'
atn_file = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/peptoid_avg_en_noncAA_PB_at10.csv'
atnminn_file = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/peptoid_avg_en_noncAA_PB_at10min10.csv'


df = pd.read_csv(inputfile)

filtered_df = df[df['average_noncAA'] <= (df['average_ncAA']/10)]

filtered_df.to_csv(atn_file, index = False)

df2 = filtered_df[filtered_df['average_ncAA'] >= 10]

df2.to_csv(atnminn_file, index = False)
