import argparse
import numpy

version = "0.1"

class BiologicalSequence:
    """biological sequences"""

    valid_types = ("dna", "rna", "protein")

    def __init__(self, sequence_type: str, path: str):
        self.path = path
        self.sequence_type = sequence_type
        if self.sequence_type not in self.valid_types:
            print("nuh uh")

def extractSequenceFromFasta(path: str) -> str:
    with open(path, 'r') as fasta_file:
        sequence = fasta_file.readlines()[1:] # todo: what if file doesn't have >, or starts with empty line?
    return ''.join(sequence).strip()
    
def constructSequence(type, path):
    instance = BiologicalSequence(type, path)
    return instance
    
def smithWaterman(seq1, seq2):
    pass

def align(seq1: BiologicalSequence, seq2: BiologicalSequence):
    seqA = extractSequenceFromFasta(seq1.path)
    seqB = extractSequenceFromFasta(seq2.path)
    pass

def main():
    parser = argparse.ArgumentParser(description=f'pairwise alignment of biological sequences, version {version}')
    parser.add_argument('seq1', metavar='seq1', type=str, help="path to FASTA sequence file 1")
    parser.add_argument('seq2', metavar='seq2', type=str, help="path to FASTA sequence file 2") # loop won't work with next if statement
    parser.add_argument('--output', type=str, default='alignment.fasta', help='path to output file (default: alignment.fasta)') 
    parser.add_argument('--type', type=str, default='protein', choices=["protein", "dna", "rna"], help="type of sequence (default: protein)")
    parser.add_argument('--algorithm', type=str, default="SW", choices=["SW", "NW"], help="alignment algorithm (default: SW)")
    parser.add_argument('--dotplot', metavar="-d", type=bool, default=False, help="output dotplot file (default: False)")
    args = parser.parse_args()

if __name__ == "__main__":
    main()    
