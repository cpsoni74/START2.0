import pandas as pd

#add filters for ncAA and noncAA

def avg_enrichment():
	# Load the CSV file into a DataFrame, assuming the CSV file already has a MultiIndex
	input_file = '/Users/chintansoni/Desktop/NGS/TWIST analysis/-ncAA/Results/15N_TWIST Results.csv'
	# Save the updated DataFrame to a new CSV file with the MultiIndex
	output_file = '/Users/chintansoni/Desktop/NGS/TWIST analysis/-ncAA/Results/noncAA_multiindex.csv'
	#barcodes and corresponding average_enrichment for subsequent processing
	output_file2 = '/Users/chintansoni/Desktop/NGS/TWIST analysis/-ncAA/Results/noncAA_avg_en.csv'

	df = pd.read_csv(input_file, header=[0, 1])

	# Calculate the total raw counts for each condition
	total_in = df[('Raw counts', 'in')].sum()
	total_out1 = df[('Raw counts', 'out1')].sum()
	total_out2 = df[('Raw counts', 'out2')].sum()

	print('Total in, out1, out2:', total_in, total_out1, total_out2)

	print("Not dropping for noncAA out")
	#df = df[df[('Raw counts','out1')] > 0]
	#df = df[df[('Raw counts', 'out2')] > 0]
	#print("Dropping for ncAA =0")

	total_in = df[('Raw counts', 'in')].sum()
	total_out1 = df[('Raw counts', 'out1')].sum()
	total_out2 = df[('Raw counts', 'out2')].sum()

	#After dropping
	print('Total in, out1, out2 after dropping unreliable reads from out:', total_in, total_out1, total_out2)

	# Calculate the fraction of total for each barcode in each condition
	df[('Fraction of total', 'in')] = df[('Raw counts', 'in')] / total_in
	df[('Fraction of total', 'out1')] = df[('Raw counts', 'out1')] / total_out1
	df[('Fraction of total', 'out2')] = df[('Raw counts', 'out2')] / total_out2

	#Calculate enrichment

	df[('Fold enrichment', 'in')] = df['Fraction of total', 'in']/ df[('Fraction of total','in')]
	df[('Fold enrichment', 'out1')] = df['Fraction of total', 'out1']/ df[('Fraction of total','in')]
	df[('Fold enrichment', 'out2')] = df['Fraction of total', 'out2']/ df[('Fraction of total','in')]

	#Average enrichment
	df[('average_ncAA','_')] = (df[('Fold enrichment', 'out1')] + df[('Fold enrichment', 'out2')])/2
	df['Rawbccounts_in'] = df[('Raw counts','in')]
	
	df.to_csv(output_file, index = False)

	print(f"Fraction of total calculations have been completed and saved to {output_file}")
	selected_col = ['barcode', 'Rawbccounts_in','average_ncAA']
	final_en = df[selected_col]
	#final_en = final_en.drop(index = 1)

	final_en.to_csv(output_file2, index = False)

#Testing columns
"""import pandas as pd

# Load the CSV file into a DataFrame, assuming the CSV file already has a MultiIndex
input_file = '/Users/chintansoni/Desktop/NGS/Results/15N_TWIST Results.csv'
df = pd.read_csv(input_file, header=[0, 1])

# Print the columns to check the MultiIndex structure
print("Columns in DataFrame:")
print(df.columns)

# Check the first few rows of the DataFrame
print("\nFirst few rows of DataFrame:")
print(df.head())"""
avg_enrichment()

