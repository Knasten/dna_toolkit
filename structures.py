NUCLEO_BASES = ["A", "C", "G", "T"]

COMPLEMENTARY_TABLE = str.maketrans("ACTG", "TGAC")

# M is start codon and * is end codon
RNA_CODON = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGA': '*', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
    'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
    'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# M is start codon and * is end codon
DNA_CODON = {
  'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N',
  'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
  'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S',
  'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I',
  'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H',
  'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
  'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
  'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
  'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D',
  'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
  'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
  'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 
  'TAA': '*', 'TAC': 'Y', 'TAG': '*', 'TAT': 'Y',
  'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
  'TGA': '*', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C',
  'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'
 }

# NM_000207.3 Homo sapiens insulin (INS), transcript variant 1, mRNA
NM_000207_3 = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"