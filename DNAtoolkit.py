from structures import *

#Check the validity of the string to make sure it is a DNA string
def validateSeq(dna):
    #"""this creates a temporary DNA sequence in upper case"""
    tempdna = dna.upper()

    for nuc in tempdna:
        if nuc not in nucleotides:
            return "Invalid Genomic Sequence"
    return tempdna




#Count frequency of nucleotides
def countfreq(seq):
    tmpfreqDict = {"A": 0, "G": 0, "C": 0, "T": 0}
    for nuc in seq:
        tmpfreqDict[nuc] += 1
    return tmpfreqDict






#Transcription of DNA -> RNA
def transcription(seq):
    return seq.replace("T", "U")

#Reverse Trnascription of RNA -> DNA
def reversetranscription(seq):
    return seq.replace("U", "T")

#complementing DNA Sequences

def reverse_complement(seq):
    return''.join([DNA_reversecomplement[nucleotides] for nucleotides in seq])[::-1]

"""calculating GC content"""
def gc_content(seq):
    return round((seq.count('C')+ seq.count('G')/ len(seq)* 100))
