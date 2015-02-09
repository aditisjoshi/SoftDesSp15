# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: ADITI JOSHI 

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('B')
    
    >>> get_complement(7)
    
    """
    if (nucleotide == 'A'):
        return 'T'
    elif (nucleotide == 'T'):
        return 'A'
    elif (nucleotide == 'C'):
        return 'G'
    elif (nucleotide == 'G'):
        return 'C'
    else:
        ValueError('That is not a nucleotide')

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    >>> get_reverse_complement("C")
    'G'
    >>> get_reverse_complement("")
    ''
    """
    reverseComplement = ''
    for x in range(0, len(dna)):
        reverseComplement = get_complement(dna[x]) + reverseComplement
    return reverseComplement

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGCCCTAA")
    'ATGCCC'
    >>> rest_of_ORF("ATGAGAG")
    'ATGAGAG'
    """
    # stop codons: 'TAG', 'TAA', 'TGA'
    for x in range(0, len(dna), 3):
        if dna[x:x+3] in ['TAG','TAA','TGA']:
            return dna[:x]
    return dna

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC") 
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGATGCCCTAG")
    ['ATGATGCCC']
    >>> find_all_ORFs_oneframe("AGCATGTAG")
    ['ATG']
    >>> find_all_ORFs_oneframe("ATGTAGATG")
    ['ATG', 'ATG']
    """
    allorfs = []
    x = 0
    while x < len(dna)-2:
        if(dna[x] == 'A' and dna[x+1] == 'T' and dna[x+2] == 'G'):
            allorfs.append(rest_of_ORF(dna[x:]))
            x = x + len(rest_of_ORF(dna[x:]))
        else:
            x += 3
    return allorfs

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    >>> find_all_ORFs("")
    []
    """
    allorfs = []
    allorfs += (find_all_ORFs_oneframe(dna))
    allorfs += (find_all_ORFs_oneframe(dna[1:]))
    allorfs += (find_all_ORFs_oneframe(dna[2:]))
    return allorfs

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    >>> find_all_ORFs_both_strands("")
    []
    """
    allorfs = []
    reverse_dna = get_reverse_complement(dna)
    allorfs += find_all_ORFs(dna)
    allorfs += find_all_ORFs(reverse_dna)
    return allorfs

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("TCAGACCT")
    0
    """
    allorfs = find_all_ORFs_both_strands(dna)
    if len(allorfs) == 0:
        return 0
    return max(allorfs, key=len)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # orfslength = []
    max_length = 0
    for i in range(num_trials):
        dna_shuffle = shuffle_string(dna)
        length = len(longest_ORF(dna_shuffle))
        if max_length < length:
            max_length = length
    return max_length

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
        >>> coding_strand_to_AA("")
        ''
    """
    amino_acid_full = ''
    if len(dna) % 3 != 0:
        remainder = len(dna) % 3
        dna = dna[:-remainder]
    for i in range(0,len(dna),3):
        amino_acid = aa_table[dna[i:i+3]]
        amino_acid_full += amino_acid
    return amino_acid_full

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    allorfs = find_all_ORFs_both_strands(dna)
    allacids = []
    for orf in allorfs:
        if len(orf) > threshold:
            acid = coding_strand_to_AA(orf)
            allacids.append(acid)
    return allacids

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    from load import load_seq
    dna = load_seq("./data/X73525.fa")
    print gene_finder(dna)