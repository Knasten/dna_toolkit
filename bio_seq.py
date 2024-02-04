from bio_structs import NUCLEO_BASES, DNA_CODONS, RNA_CODONS
from collections import Counter
from random import choice
from itertools import chain

class bio_seq:
  """DNA sequence class. Default value: ATCG, DNA, No Label"""

  def __init__(self, seq="ATCG", seq_type="DNA", label="No Label"):
    """Initialization and validation of sequence"""
    self.seq = seq
    self.seq_type = seq_type
    self.label = label
    self.is_valid = self.__validate()
    assert self.is_valid, f'Provided DNA sequence seems to be incorrect: {self.seq}'

  def __validate(self):
    """Makes sure the string is a valid DNA string"""
    return set(NUCLEO_BASES[self.seq_type]).issuperset(self.seq)
  
  def get_info(self):
    return f"[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Label]: {self.label}\n[Length]: {len(self.seq)}"
  
  def get_seq_type(self):
    return self.seq_type
  
  def gen_random_sequence(self, length=50, seq_type="DNA"):
    seq = ''.join(choice(NUCLEO_BASES[seq_type]) for _ in range(length))
    self.__init__(seq, seq_type, "Randomly generated sequence")

  def base_frequency_count(self):
    """Sequence -> Dict with counter for each base """
    return dict(Counter(self.seq))
  
  def transcription(self):
    """DNA -> RNA, replaces Thymine with Uracil"""
    if self.seq_type != 'DNA':
      return 'Invalid sequence not DNA'
    return self.seq.replace("T", "U")
  
  def reverse_complement(self):
    """
    Swaps adenine with thymine and guanine with cytosine\n
    Reverses the final string
    """
    mapping = str.maketrans("ACTG", "TGAC") if self.seq_type == "DNA" else str.maketrans("ACUG", "UGAC")
    return self.seq.translate(mapping)[::-1]
  
  def gc_content(self, n=6):
    """
    GC Content in DNA\RNA sequence \n
    n will specify decimal precision
    """
    return round((self.seq.count('C') + self.seq.count('G')) / len(self.seq) * 100, n)
  
  def gc_content_subseq(self, k=20):
    """
    GC Content in a DNA/RNA sub sequence of k length. k defaults at 20
    """
    return [round((self.seq[i:i + k].count('C') + self.seq[i:i + k].count('G')) / k * 100, 6) for i in range(0, len(self.seq) - k + 1, k)]
  
  def translate_seq(self, init_pos=0):
    """Translates DNA to Amino Acid Sequence"""
    if self.seq_type == 'DNA':
      return ''.join([DNA_CODONS[self.seq[pos: pos+3]] for pos in range(init_pos, len(self.seq) - 2, 3)])
    elif self.seq_type == 'RNA':
      return ''.join([RNA_CODONS[self.seq[pos: pos+3]] for pos in range(init_pos, len(self.seq) - 2, 3)])
    
  def codon_freq(self, aa):
    """
    Check for a special Amino Acid(AA) and return freq for each codon encoding for that specific AA
    """
    if self.seq_type == 'DNA':
      tmpList = [self.seq[i:i + 3] for i in range(0, len(self.seq) - 2, 3) if DNA_CODONS[self.seq[i:i + 3]] == aa]
    elif self.seq_type == 'RNA':
      tmpList = [self.seq[i:i + 3] for i in range(0, len(self.seq) - 2, 3) if RNA_CODONS[self.seq[i:i + 3]] == aa]
      
    return { k: f'{(v / len(tmpList)) * 100}%' for k,v in Counter(tmpList).most_common() }
  
  def gen_reading_frames(self):
    """Generate six reading frames of a DNA sequence, including reverse complement"""
    frames = [self.translate_seq(x) for x in range(0, 3)]
    tmp_seq = bio_seq(self.reverse_complement(), self.seq_type)
    for x in range(0, 3):
      frames.append(tmp_seq.translate_seq(x))
    del tmp_seq
    return frames
  
  def proteins_from_rf(self, aa_seq):
    current_prot = []
    proteins = []
    for aa in aa_seq:
      if aa == "*":
        if current_prot:
          for p in current_prot:
            proteins.append(p)
          current_prot = []
      else:
        if aa == "M":
          current_prot.append("")
        for i in range(len(current_prot)):
          current_prot[i] += aa
    return proteins
  
  def proteins_from_orfs(self, start=0, end=0, ordered=False):
    """
    Returns a list of proteins based on reading frames created from the supplied sequence
    """
    if end > start:
      tmpSeq = bio_seq(self.seq[start:end], self.seq_type)
      rfs = tmpSeq.gen_reading_frames()
    else:
      rfs = self.gen_reading_frames()
    
    res = list(chain.from_iterable([self.proteins_from_rf(rfs[i]) for i in range(len(rfs))]))
    if ordered:
      return sorted(res, key=len, reverse=True)
    return res