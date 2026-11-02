'''
Aryona Lewis
Helper
Building a dictionary of the nucleotide triplates
'''

amino = {
    "UUU": "Phe", "UUC": "Phe", "UUA":"Leu", "UUG": "Leu",
    "UUC": "Ser","UCC": "Ser", "UCA": "Ser", "UCG": "Ser","UAA": "Stop", "UAG": "STOP", "UGA": "Stop",
    "UAU": "Tyr", "UAC": "Tyr", "UGU": "Cys", "UCG":"Cyr", "UGG":"Trp",

    "CUU":"Leu", "CUC": "Leu", "CUA":"Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA":"Pro", "CCG": "Pro",
    "CAU":"His", "CAC": "His", "CAA": "Gin", "CAG": "Gin",
    "CGU": "Arg", "CGC":"Arg","CGA": "Arg", "CGG": "Arg",

    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",

    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}