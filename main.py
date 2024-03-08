import argparse
import numpy

version = "0.1"

class Sequence:
    """biological sequences"""

    seq_types = ("dna", "rna", "protein")

    def __init__(self, seq_type: str, path: str):
        self.path = path
        self.seq_type = seq_type
        if self.seq_type not in self.seq_types:
            print("nuh uh")

def user_input() -> Sequence:
    path = input("path to file")
    return Sequence("dna", path)

def main():
    parser = argparse.ArgumentParser(description=f'pairwise alignment of biological sequences, version {version}')

    for name in 'seq1', 'seq2':
        parser.add_argument('sequences',
                            metavar=name,  
                            action='append',
                            type=str,  
                            help="paths to FASTA sequence file")
        
    parser.add_argument('--output', type=str, default='alignment.fasta', help='path to output file (default: alignment.fasta)') 
    parser.add_argument('--algorithm', type=str, default="SW", choices=["SW", "NW"], help="alignment algorithm (default: SW)")
    parser.add_argument('--dotplot', metavar="-d", type=bool, default=False, help="output dotplot file (default: False)")

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()    
