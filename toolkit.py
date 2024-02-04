from random import choice
from decimal import Decimal, getcontext
from structures import *
from collections import Counter
from itertools import chain

# DNA toolkit
def generate_DNA(length):
  """Random sequence generator for testing"""
  return ''.join(choice('ACGT') for _ in range(length))


def validate_seq(seq):
  tmp_seq = seq.upper()
  for nuc in tmp_seq:
    if nuc not in NUCLEO_BASES:
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
  """Returns the reverse complement.\nExample the 5' -> 3' would return 5' -> 3' with complementary bases"""
  return seq.translate(COMPLEMENTARY_TABLE)[::-1]
  # ''.join([structures.REVERSECOMPLEMENT[base] for base in seq])[::-1]


def gc_content(seq, n=6):
  """
  Returns the percentage content of CG in the supplied sequence \n
  n = decimal precision
  """

  return round((seq.count('C') + seq.count('G')) / len(seq) * 100, n)


def gc_content_subseq(seq, k=20):
  """
  Returns gc content of subsequences of an sequence \n
  k is used to select window width and defaults at 20
  """
  return [gc_content(seq[i:i + k]) for i in range(0, len(seq) - k + 1, k)]


def translate_seq(seq, init_pos=0):
  """Translates DNA to Amino Acid Sequence"""
  return ''.join([DNA_CODON[seq[pos: pos+3]] for pos in range(init_pos, len(seq) - 2, 3)]) # Check sequence 3 at a time to match to dict


def codon_freq(seq, codon):
  """
  Checks for a specific aminoacid then gives you the frequency of each specific codon that codes for that amino acid
  """
  tmpList = [seq[i:i + 3] for i in range(0, len(seq) - 2, 3) if DNA_CODON[seq[i:i + 3]] == codon]
  return { k: f'{(v / len(tmpList)) * 100}%' for k,v in Counter(tmpList).most_common() }


def gen_reading_frames(seq):
  """Generate six reading frames of a DNA sequence, including reverse complement"""
  frames = [translate_seq(seq, x) for x in range(0, 3)]
  for x in range(0, 3):
    frames.append(translate_seq(reverse_complement(seq), x))
  return frames


def proteins_from_aminoseq(seq):
  # Check the seq for starting codon M and register each subsequent codon until the stop codon *
  # Each protein should be saved to a list and then returned when all available proteins has been checked

  # MLGVRSHTIEYIRTKYHLADIDAVSEIGMIIRYFRPPRARKI
  current_prot = []
  proteins = []
  for aa in seq:
    if aa == "*":
      # If this symbols appears the chain has stopped and proteins are collected and memory containers are emptied
      if current_prot:
        for p in current_prot:
          proteins.append(p)
        current_prot = []
    else:
      if aa == "M":
        # Create a new entry for a new start codon
        current_prot.append("")
      for i in range(len(current_prot)):
        # Loop through each current protein and add the new codon to the chain
        current_prot[i] += aa
  return proteins


def proteins_from_orfs(seq, start=0, end=0, ordered=False):
  """
  Returns a list of proteins based on reading frames created from the supplied sequence
  """
  if end > start:
    rfs = gen_reading_frames(seq[start:end])
  else:
    rfs = gen_reading_frames(seq)
  
  res = list(chain.from_iterable([proteins_from_aminoseq(rfs[i]) for i in range(len(rfs))]))
  if ordered:
    return sorted(res, key=len, reverse=True)
  return res