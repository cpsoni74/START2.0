#Generating protein library 

import csv
from codon_translate import translate
from twist_translate import twist_randomize
from twist_translate import twist_translate
import pandas as pd

def DNA_codon(MaPylDNA, positions, forward_adap, reverse_adap):

	twist_DNA = {}
	twist_lib = []
	twist_lib_final = []

	for x in positions: 
		pos = x - 1

		#first twist translate the position in DNA sequence	
		MaPylAA, codons = translate(MaPylDNA)

		#print (MaPylAA, MaPylAA[pos])
		codons[pos] = twist_translate(MaPylAA, pos)
		MaPylDNA = ''.join(codons)
	twist_lib = [MaPylDNA]
	print ("post twist_opt of sites: ", twist_lib)

	for x in positions:
		pos = x - 1
		for seq in twist_lib:
			MaPylAA, codons = translate(seq) 
			twist_DNA = twist_randomize(codons, pos)
			twist_lib = twist_lib + twist_DNA

	twist_lib_final_no_dups = []
	seen = set()
	for item in twist_lib:
		if item not in seen:
			twist_lib_final_no_dups.append(item)
			seen.add(item)

	print (len(twist_lib_final_no_dups))
	output_file = "twist_aaRS_lib_oligo 2.csv"
	with open(output_file, 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(['DNA Sequence'])
    
		for sequence in twist_lib_final_no_dups:
			final_sequence = forward_adap + sequence + reverse_adap
			csv_writer.writerow([final_sequence])

	#print (sequences)
	protein_seq = []
	for sequence in twist_lib_final_no_dups:
		#print (sequence)
		MaPylAA, codons = translate(sequence)
		#print (MaPylAA, codons)
		protein_seq.append(MaPylAA)
	
	df2 = pd.DataFrame(protein_seq)
	df2.to_csv('protein_sequence_twist_oligo2.csv')

MaPylDNA = 'CTGAACCTTGTGGATATGGGACCGCGTGGTGATGCGACAGAGGTTTTAAAAAATTACATTAGTGTTGTGATGAAAGCAGCGGGATTGCCCGATTATGATTTAGTCCAGGAAGAGAGTGACGTCTACAAAGAAACTATCGATGTTGAGATTAACGGGCAAGAAGTATGTAGCGCTGCTGTCGGACCCCATTATCTGGAT'
positions = [41, 42]
forward_adap = ''
reverse_adap = 'GC'
DNA_codon(MaPylDNA, positions, forward_adap, reverse_adap)




