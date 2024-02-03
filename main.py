from toolkit import *

# Create a new test string
tmpSeq = generate_DNA(50)

# Validate said string
seq = validate_seq(tmpSeq)

# Get freq count
freq = base_frequency_count(seq)

# Transcription DNA -> RNA
RNA = transcribe(seq)

# Get the reverse complement for a DNA strand
complement = reverse_complement(seq)

# Get CG Content
cg_content = gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT')

# RNA -> Amino
aminoacid = translateRNA(RNA)

print(f"[1] - tmpSeq | {tmpSeq}")
print(f"[2] - Validation | {seq}")
print(f"[3] - Frequency | {freq}")
print(f"[4] - Transcription | {RNA}")
print(f"[5] - Reverse Complement | {complement}")
print(f"[6] - CG-Content | {cg_content}%")
print(f"[7] - Amino Acids | {aminoacid}")
