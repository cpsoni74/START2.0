import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logomaker

def make_base_matrix_columns(sequences):
    # Convert the set to a sorted list to ensure consistent column ordering
    columns = sorted(set(char for seq in sequences for char in seq))
    return columns

def populate_logo_matrix(sequences, quantifications, columns=None):
    if columns is None:
        columns = make_base_matrix_columns(sequences)

    seq_len = len(sequences[0])
    ret = pd.DataFrame(np.zeros(shape=(seq_len, len(columns))),
                       index=list(range(seq_len)),
                       columns=columns)

    for s, q in zip(sequences, quantifications):
        if not np.isnan(q):
            for i, b in enumerate(s):
                ret.at[i, b] += q

    return ret

def make_logo_plot(fname, dat, width, height, font_size):
    seq_len = len(dat)
    x_labels = list(range(seq_len))

    # Create the sequence logo using logomaker
    logo = logomaker.Logo(dat, color_scheme='hydrophobicity')
    logo.style_spines(visible=False)
    logo.style_xticks(visible=False)
    logo.ax.set_xticks(range(seq_len))
    logo.ax.set_xticklabels(x_labels)
    logo.ax.set_ylabel('Weighted Enrichment Factor')

    # Set the figure size
    plt.gcf().set_size_inches(width, height)

    # Save the figure to a file
    plt.savefig(fname, format='png', dpi=600)

# Load the data
input_file = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/at10min10/peptoid_avg_en_noncAA_PB_at10min10_at10min10_avgd_aaRS>1.csv'
output_quant = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/at10min10/peptoid_avg_en_noncAA_PB_at10min10_at10min10_avgd_aaRS>1_frac.csv'
weblogo = '/Users/chintansoni/Desktop/NGS/TWIST analysis/peptoid/ncAA>0, noncAA>=0/at10min10/peptoid_avg_en_noncAA_PB_at10min10_at10min10_avgd_aaRS>1_weblogo.png'

hits_df = pd.read_csv(input_file)
sequences = hits_df['aaRS']
quantifications = hits_df['aaRS_count']

# Print sequences and quantifications for debugging purposes
print(sequences)
print(quantifications)

# Process the data
col = make_base_matrix_columns(sequences)
df = populate_logo_matrix(sequences, quantifications, col)

# Print the resulting matrix for debugging purposes
print(df)

# Save the processed data to a CSV file
df.to_csv(output_quant)

# Create the sequence logo plot
make_logo_plot(weblogo, df, 20, 40, 5)
