def split_fastq_by_umi(input_file, umi1, umi2, output_file1, output_file2):
    with open(input_file, 'r') as infile, \
         open(output_file1, 'w') as outfile1, \
         open(output_file2, 'w') as outfile2:
        
        while True:
            # Read the four lines corresponding to a single read
            header = infile.readline().strip()
            if not header:
                break  # End of file
            sequence = infile.readline().strip()
            plus_line = infile.readline().strip()
            quality = infile.readline().strip()
            
            # Check the UMI at the beginning of the sequence
            if sequence.startswith(umi1):
                outfile1.write(f"{header}\n{sequence}\n{plus_line}\n{quality}\n")
            elif sequence.startswith(umi2):
                outfile2.write(f"{header}\n{sequence}\n{plus_line}\n{quality}\n")

# Define your input and output files and UMIs
input_fastq = '/Users/chintansoni/Desktop/NGS/Fastq/mod_947339-4_S25_L001_R1_001.fastq'
umi_ox1 = 'AAAAAA'
umi_ox2 = 'TTTTTT'
output_fastq_ox1 = '/Users/chintansoni/Desktop/NGS/Fastq/out_mod_947339-4_S25_L001_R1_001.fastq'
output_fastq_ox2 = '/Users/chintansoni/Desktop/NGS/Fastq/in_947339-4_S25_L001_R1_001.fastq'

# Call the function to split the FASTQ file
split_fastq_by_umi(input_fastq, umi_ox1, umi_ox2, output_fastq_ox1, output_fastq_ox2)
