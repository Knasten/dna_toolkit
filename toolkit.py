from random import choice
from decimal import Decimal, getcontext
import structures

# DNA toolkit
def generate_DNA(length):
  """Random sequence generator for testing"""
  return ''.join(choice('ACGT') for _ in range(50))


def validate_seq(seq):
  tmp_seq = seq.upper()
  for nuc in tmp_seq:
    if nuc not in structures.NUCLEOBASES:
      return False
  return tmp_seq


def base_frequency_count(seq):
  """Sequence -> Dict with counter for each base """
  freq = {"A": 0, "C": 0, "G": 0, "T": 0}
  for nuc in seq:
    freq[nuc] += 1
  return freq


def transcribe(seq):
  """DNA -> RNA, replaces Thymine with Uracil"""
  return seq.replace("T", "U")


def reverse_complement(seq):
  """Returns the reverse complement. Example the 5' -> 3' would return 5' -> 3' with complementary bases"""
  return seq.translate(str.maketrans("ACTG", "TGAC"))[::-1]
  # ''.join([structures.REVERSECOMPLEMENT[base] for base in seq])[::-1]


def gc_content(seq, n=6):
  """
  Returns the percentage content of CG in the supplied sequence
  n = decimal precision
  """
  getcontext().prec = n + 2 # Add 2 to precision to counteract the multiplication from decimal to percentage form

  return (Decimal(seq.count('C') + seq.count('G')) / Decimal(len(seq)) * 100)


def translateRNA(seq, k=0):
  aminos = []
  while k + 3 <= len(seq):
    aminos.append(structures.CODON[seq[k:k + 3]])
    k += 3
  return "".join(aminos)