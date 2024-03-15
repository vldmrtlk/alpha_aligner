# requires: numpy, argparse

import argparse

from algorithms import needlemanWunsch

version = "0.2"

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
    
def constructBiologicalSequence(type, path):
    instance = BiologicalSequence(type, path)
    return instance
    
def align(sequenceA: BiologicalSequence, sequenceB: BiologicalSequence, penalty = -8):
    seqA = extractSequenceFromFasta(sequenceA.path).lower()
    seqB = extractSequenceFromFasta(sequenceB.path).lower()

    alignments = needlemanWunsch(seqA,seqB,gap_penalty=penalty)
    for pair in alignments:
        print(f"{pair[0]}\n{pair[1]}\n")
    
def main():
    parser = argparse.ArgumentParser(description=f'pairwise alignment of biological sequences, version {version}')
    parser.add_argument('seqA', metavar='seqA', type=str, help="path to FASTA sequence file 1")
    parser.add_argument('seqB', metavar='seqB', type=str, help="path to FASTA sequence file 2") # loop won't work with next if statement
    parser.add_argument('--output', type=str, default='alignment.fasta', help='path to output file (default: alignment.fasta)') 
    parser.add_argument('--type', type=str, default='protein', choices=["protein", "dna", "rna"], help="type of sequence (default: protein)")
    parser.add_argument('--penalty', type=int, default=-8, help="penalty for creating gap (defautl: -8)")
    parser.add_argument('--algorithm', type=str, default="SW", choices=["SW", "NW"], help="alignment algorithm (default: SW)")
    parser.add_argument('--dotplot', metavar="-d", type=bool, default=False, help="output dotplot file (default: False)")
    args = parser.parse_args()

    print(f"aligning {args.seqA} with {args.seqB} using {args.algorithm}\n")

    sequenceA = constructBiologicalSequence(args.type, args.seqA)
    sequenceB = constructBiologicalSequence(args.type, args.seqB)
    penalty = args.penalty
    align(sequenceA, sequenceB, penalty)

if __name__ == "__main__":
    main()    
