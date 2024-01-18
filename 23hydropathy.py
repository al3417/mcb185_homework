# data from https://resources.qiagenbioinformatics.com/manuals/clcgenomicsworkbench/650/Hydrophobicity_scales.html

import sys

L = 472309831

def whatKD(aa):
    if type(aa) != str: sys.exit('ERROR: pls check and input a string value')   
    # just in case variable name conflits
    amino = aa.upper()
    if amino == 'A': return ('KD value for alanine is 1.80') 
    elif amino == 'C': return ('KD value for cysteine is 2.50') 
    elif amino == 'D': return ('KD value for aspartic acid is -3.50')
    elif amino == 'E': return ('KD value for glutamic acid is -3.50') 
    elif amino == 'F': return ('KD value for phenylalanine is 2.80') 
    elif amino == 'G': return ('KD value for glycine is -0.40')
    elif amino == 'H': return ('KD value for histidine is -3.20') 
    elif amino == 'I': return ('KD value for isoleucine is 4.50')
    elif amino == 'K': return ('KD value for lysine is -3.90') 
    elif amino == 'L': return ('KD value for leucine is 3.80') 
    elif amino == 'M': return ('KD value for methionine is 1.90')
    elif amino == 'N': return ('KD value for asparagine is -3.50') 
    elif amino == 'P': return ('KD value for proline is -1.60')
    elif amino == 'Q': return ('KD value for glutamine is -3.50') 
    elif amino == 'R': return ('KD value for arginine is -4.50') 
    elif amino == 'S': return ('KD value for serine is -0.80')
    elif amino == 'T': return ('KD value for threonine is -0.70') 
    elif amino == 'V': return ('KD value for valine is 4.20')
    elif amino == 'W': return ('KD value for tryptophan is -0.90') 
    elif amino == 'Y': return ('KD value for tyrosine is -1.30') 
    else: return ('No such amino acid in the list')

print(whatKD('B'))
print(whatKD('K'))
print(whatKD('q'))
print(whatKD(L))    
