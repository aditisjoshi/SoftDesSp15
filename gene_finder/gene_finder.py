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
    False
    >>> get_complement(7)
    False
    """
    # TODO: implement this
    if (nucleotide == 'A'):
        return 'T'
    elif (nucleotide == 'T'):
        return 'A'
    elif (nucleotide == 'C'):
        return 'G'
    elif (nucleotide == 'G'):
        return 'C'
    else:
        return False
    pass

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
    """
    # TODO: implement this
    dnaReverse = dna[::-1]
    reverseComplement = ''
    for x in range(0, len(dnaReverse)):
        reverseComplement += get_complement(dnaReverse[x])
    return reverseComplement
    pass

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
    # TODO: implement this
    # stop codons: 'TAG', 'TAA', 'TGA'
    for x in range(1, len(dna)):
        if(x % 3 == 0):
            if (dna[x] == 'T' and dna[x+1] == 'A' and dna[x+2] == 'G'):
                return dna[:x]
            elif (dna[x] == 'T' and dna[x+1] == 'A' and dna[x+2] == 'A'):
                return dna[:x]
            elif (dna[x] == 'T' and dna[x+1] == 'G' and dna[x+2] == 'A'):
                return dna[:x]
    return dna
    pass

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
    # TODO: implement this
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
    """
    # TODO: implement this
    allorfs = []
    allorfs += (find_all_ORFs_oneframe(dna))
    allorfs += (find_all_ORFs_oneframe(dna[1:]))
    allorfs += (find_all_ORFs_oneframe(dna[2:]))
    return allorfs
    pass

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    allorfs = []
    reverse_dna = get_reverse_complement(dna)
    allorfs += find_all_ORFs(dna)
    allorfs += find_all_ORFs(reverse_dna)
    return allorfs
    pass


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

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
    """
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()