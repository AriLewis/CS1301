"""
Program Name: dna_translation.py
Author: Aryona
"""

from helper import amino
 
def transcription(dna):
    mrna = ""
    for nucleotide in dna:
        if nucleotide == "A":
            mrna += "U"
        elif nucleotide == "T":
            mrna += "A"
        elif nucleotide == "C":
            mrna += "G"
        elif nucleotide == "G":
            mrna += "C"
    return mrna
 

def translation(mrna):
    triplets = []
    current = ""                      # fixed: no leading space
    for character in mrna:
        current += character
        if len(current) == 3:
            triplets.append(current)
            current = ""

    protein = []
    for triplet in triplets:
        if triplet in ("UAA", "UAG", "UGA"):   # stop codon ends translation
            break
        protein.append(amino[triplet])         # look up the amino acid
    return " ".join(protein)

 
def main():
    dna = "TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT"
 
    print("DNA Sequence")
    print(dna)
    print()
 
    mrna = transcription(dna)
    print("mRNA Sequence")
    print(mrna)
    print()
 
    protein = translation(mrna)
    print("Protein Sequence")
    print(protein)
 

main()