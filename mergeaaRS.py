#Merge by aaRS


import pandas as pd

# Define the file paths
file1_path = '/Users/chintansoni/Desktop/NGS/TWIST analysis/Sb2OH/ncAA>0/15NxTWIST_SB2OH_avg_en_noncAA_PB_at2min2_avgd.csv'
file2_path = '/Users/chintansoni/Desktop/inputlib_PB_cov_counts.csv'


outputfile = '/Users/chintansoni/Desktop/NGS/TWIST analysis/Sb2OH/ncAA>0/15NxTWIST_SB2OH_avg_en_noncAA_PB_at2min2_avgd_incounts.csv'
# Read both CSV files into DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Drop duplicates from df2 based on the 'barcode' column
df2 = df2.drop_duplicates(subset='aaRS')

# Find common barcodes between the two DataFrames
common_barcodes = set(df1['aaRS']).intersection(set(df2['aaRS']))

# Filter rows in df2 that have common barcodes
filtered_df2 = df2[df2['aaRS'].isin(common_barcodes)]

# Merge data from df1 and filtered_df2 based on the 'barcode' column
merged_df = df1.merge(filtered_df2, on='aaRS', how='inner')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(outputfile, index=False)

print("Merged data saved successfully.")
