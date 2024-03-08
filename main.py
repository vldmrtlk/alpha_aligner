import typer 
import numpy

version = "0.0.1"

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

user_input()
