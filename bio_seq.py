from bio_structs import *
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
    return set(NUCLEO_BASES).issuperset(self.seq)
  
  def get_info(self):
    return f"[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Label]: {self.label}\n[Length]: {len(self.seq)}"
  
  def get_seq_type(self):
    return self.seq_type
  
  def gen_random_sequence(self, length=50, seq_type="DNA"):
    seq = ''.join(choice(NUCLEO_BASES) for _ in range(length))
    self.__init__(seq, seq_type, "Randomly generated sequence")