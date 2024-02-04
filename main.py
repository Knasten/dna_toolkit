from toolkit import *
from utilities import *

# Create a new test string
tmpSeq = generate_DNA(200)

# Validate said string
seq = validate_seq(tmpSeq)

# Get freq count
freq = base_frequency_count(seq)

# Transcription DNA -> RNA
RNA = transcribe(seq)

# Get the reverse complement for a DNA strand
complement = reverse_complement(seq)

# Get GC Content
cg_content = gc_content(seq)

# Subsection GC
subsection_gc = gc_content_subseq(seq, k=20)

# Seq -> Amino Acid Seq 
amino_seq = translate_seq(seq)

# Codon Freq
codon = 'L'
codon_frequency = codon_freq(seq, codon)

# # Read File
# amino_from_file = translate_seq(readFile('./testdata/rosalind_prot.txt'))


frames = gen_reading_frames(seq)


# Amino sequence -> protein chain
protein_chains = proteins_from_orfs(NM_000207_3, ordered=True)

# print(f"[1] - tmpSeq | {tmpSeq}")
# print(f"[2] - Validation | {seq}")
# print(f"[3] - Frequency | {freq}")
# print(f"[4] - Transcription | {RNA}")
# print(f"[5] - Reverse Complement | {complement}")
# print(f"[6] - CG-Content | {cg_content}%")
# print(f"[7] - Amino Acid Seq | {amino_seq}")
# print(f"[8] - GC-Subsection Content | {subsection_gc}")
# print(f"[9] - Codon Freq - {codon} | {codon_frequency}")
# print(frames)
print(f"[10] - Protein Chains From Frames - {protein_chains}")

