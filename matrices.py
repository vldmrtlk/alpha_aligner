
one_letter_to_name = {'a': 'alanine', 'c': 'cysteine', 'd': 'aspartic acid', 'e': 'glutamic acid',
                      'f': 'phenylalanine', 'g': 'glycine', 'h': 'histidine', 'i': 'isoleucine', 
                      'k': 'lysine', 'l': 'leucine', 'm': 'methionine', 'n': 'asparagine', 'p': 'proline',
                      'q': 'glutamine', 'r': 'arginine', 's': 'serine', 't': 'threonine', 'v': 'valine', 
                      'w': 'tryptophan', 'y': 'tyrosine'}

blosum62 = {('a', 'a'): 4, ('a', 'r'): -1, ('a', 'n'): -2, ('a', 'd'): -2, ('a', 'c'): 0, ('a', 'q'): -1,
            ('a', 'e'): -1, ('a', 'g'): 0, ('a', 'h'): -2, ('a', 'i'): -1, ('a', 'l'): -1, ('a', 'k'): -1,
            ('a', 'm'): -1, ('a', 'f'): -2, ('a', 'p'): -1, ('a', 's'): 1, ('a', 't'): 0, ('a', 'w'): -3,
            ('a', 'y'): -2, ('a', 'v'): 0, ('a', 'b'): -2, ('a', 'z'): -1, ('a', 'x'): 0, ('a', '*'): -4,
            ('r', 'a'): -1, ('r', 'r'): 5, ('r', 'n'): 0, ('r', 'd'): -2, ('r', 'c'): -3, ('r', 'q'): 1,
            ('r', 'e'): 0, ('r', 'g'): -2, ('r', 'h'): 0, ('r', 'i'): -3, ('r', 'l'): -2, ('r', 'k'): 2,
            ('r', 'm'): -1, ('r', 'f'): -3, ('r', 'p'): -2, ('r', 's'): -1, ('r', 't'): -1, ('r', 'w'): -3,
            ('r', 'y'): -2, ('r', 'v'): -3, ('r', 'b'): -1, ('r', 'z'): 0, ('r', 'x'): -1, ('r', '*'): -4, 
            ('n', 'a'): -2, ('n', 'r'): 0, ('n', 'n'): 6, ('n', 'd'): 1, ('n', 'c'): -3, ('n', 'q'): 0, 
            ('n', 'e'): 0, ('n', 'g'): 0, ('n', 'h'): 1, ('n', 'i'): -3, ('n', 'l'): -3, ('n', 'k'): 0, 
            ('n', 'm'): -2, ('n', 'f'): -3, ('n', 'p'): -2, ('n', 's'): 1, ('n', 't'): 0, ('n', 'w'): -4, 
            ('n', 'y'): -2, ('n', 'v'): -3, ('n', 'b'): 3, ('n', 'z'): 0, ('n', 'x'): -1, ('n', '*'): -4, 
            ('d', 'a'): -2, ('d', 'r'): -2, ('d', 'n'): 1, ('d', 'd'): 6, ('d', 'c'): -3, ('d', 'q'): 0, 
            ('d', 'e'): 2, ('d', 'g'): -1, ('d', 'h'): -1, ('d', 'i'): -3, ('d', 'l'): -4, ('d', 'k'): -1, 
            ('d', 'm'): -3, ('d', 'f'): -3, ('d', 'p'): -1, ('d', 's'): 0, ('d', 't'): -1, ('d', 'w'): -4, 
            ('d', 'y'): -3, ('d', 'v'): -3, ('d', 'b'): 4, ('d', 'z'): 1, ('d', 'x'): -1, ('d', '*'): -4, 
            ('c', 'a'): 0, ('c', 'r'): -3, ('c', 'n'): -3, ('c', 'd'): -3, ('c', 'c'): 9, ('c', 'q'): -3, 
            ('c', 'e'): -4, ('c', 'g'): -3, ('c', 'h'): -3, ('c', 'i'): -1, ('c', 'l'): -1, ('c', 'k'): -3, 
            ('c', 'm'): -1, ('c', 'f'): -2, ('c', 'p'): -3, ('c', 's'): -1, ('c', 't'): -1, ('c', 'w'): -2, 
            ('c', 'y'): -2, ('c', 'v'): -1, ('c', 'b'): -3, ('c', 'z'): -3, ('c', 'x'): -2, ('c', '*'): -4, 
            ('q', 'a'): -1, ('q', 'r'): 1, ('q', 'n'): 0, ('q', 'd'): 0, ('q', 'c'): -3, ('q', 'q'): 5, 
            ('q', 'e'): 2, ('q', 'g'): -2, ('q', 'h'): 0, ('q', 'i'): -3, ('q', 'l'): -2, ('q', 'k'): 1, 
            ('q', 'm'): 0, ('q', 'f'): -3, ('q', 'p'): -1, ('q', 's'): 0, ('q', 't'): -1, ('q', 'w'): -2, 
            ('q', 'y'): -1, ('q', 'v'): -2, ('q', 'b'): 0, ('q', 'z'): 3, ('q', 'x'): -1, ('q', '*'): -4, 
            ('e', 'a'): -1, ('e', 'r'): 0, ('e', 'n'): 0, ('e', 'd'): 2, ('e', 'c'): -4, ('e', 'q'): 2, 
            ('e', 'e'): 5, ('e', 'g'): -2, ('e', 'h'): 0, ('e', 'i'): -3, ('e', 'l'): -3, ('e', 'k'): 1, 
            ('e', 'm'): -2, ('e', 'f'): -3, ('e', 'p'): -1, ('e', 's'): 0, ('e', 't'): -1, ('e', 'w'): -3, 
            ('e', 'y'): -2, ('e', 'v'): -2, ('e', 'b'): 1, ('e', 'z'): 4, ('e', 'x'): -1, ('e', '*'): -4, 
            ('g', 'a'): 0, ('g', 'r'): -2, ('g', 'n'): 0, ('g', 'd'): -1, ('g', 'c'): -3, ('g', 'q'): -2, 
            ('g', 'e'): -2, ('g', 'g'): 6, ('g', 'h'): -2, ('g', 'i'): -4, ('g', 'l'): -4, ('g', 'k'): -2,
            ('g', 'm'): -3, ('g', 'f'): -3, ('g', 'p'): -2, ('g', 's'): 0, ('g', 't'): -2, ('g', 'w'): -2,
            ('g', 'y'): -3, ('g', 'v'): -3, ('g', 'b'): -1, ('g', 'z'): -2, ('g', 'x'): -1, ('g', '*'): -4, 
            ('h', 'a'): -2, ('h', 'r'): 0, ('h', 'n'): 1, ('h', 'd'): -1, ('h', 'c'): -3, ('h', 'q'): 0, 
            ('h', 'e'): 0, ('h', 'g'): -2, ('h', 'h'): 8, ('h', 'i'): -3, ('h', 'l'): -3, ('h', 'k'): -1, 
            ('h', 'm'): -2, ('h', 'f'): -1, ('h', 'p'): -2, ('h', 's'): -1, ('h', 't'): -2, ('h', 'w'): -2, 
            ('h', 'y'): 2, ('h', 'v'): -3, ('h', 'b'): 0, ('h', 'z'): 0, ('h', 'x'): -1, ('h', '*'): -4, 
            ('i', 'a'): -1, ('i', 'r'): -3, ('i', 'n'): -3, ('i', 'd'): -3, ('i', 'c'): -1, ('i', 'q'): -3, 
            ('i', 'e'): -3, ('i', 'g'): -4, ('i', 'h'): -3, ('i', 'i'): 4, ('i', 'l'): 2, ('i', 'k'): -3, 
            ('i', 'm'): 1, ('i', 'f'): 0, ('i', 'p'): -3, ('i', 's'): -2, ('i', 't'): -1, ('i', 'w'): -3, 
            ('i', 'y'): -1, ('i', 'v'): 3, ('i', 'b'): -3, ('i', 'z'): -3, ('i', 'x'): -1, ('i', '*'): -4, 
            ('l', 'a'): -1, ('l', 'r'): -2, ('l', 'n'): -3, ('l', 'd'): -4, ('l', 'c'): -1, ('l', 'q'): -2, 
            ('l', 'e'): -3, ('l', 'g'): -4, ('l', 'h'): -3, ('l', 'i'): 2, ('l', 'l'): 4, ('l', 'k'): -2, 
            ('l', 'm'): 2, ('l', 'f'): 0, ('l', 'p'): -3, ('l', 's'): -2, ('l', 't'): -1, ('l', 'w'): -2, 
            ('l', 'y'): -1, ('l', 'v'): 1, ('l', 'b'): -4, ('l', 'z'): -3, ('l', 'x'): -1, ('l', '*'): -4, 
            ('k', 'a'): -1, ('k', 'r'): 2, ('k', 'n'): 0, ('k', 'd'): -1, ('k', 'c'): -3, ('k', 'q'): 1, 
            ('k', 'e'): 1, ('k', 'g'): -2, ('k', 'h'): -1, ('k', 'i'): -3, ('k', 'l'): -2, ('k', 'k'): 5, 
            ('k', 'm'): -1, ('k', 'f'): -3, ('k', 'p'): -1, ('k', 's'): 0, ('k', 't'): -1, ('k', 'w'): -3, 
            ('k', 'y'): -2, ('k', 'v'): -2, ('k', 'b'): 0, ('k', 'z'): 1, ('k', 'x'): -1, ('k', '*'): -4, 
            ('m', 'a'): -1, ('m', 'r'): -1, ('m', 'n'): -2, ('m', 'd'): -3, ('m', 'c'): -1, ('m', 'q'): 0, 
            ('m', 'e'): -2, ('m', 'g'): -3, ('m', 'h'): -2, ('m', 'i'): 1, ('m', 'l'): 2, ('m', 'k'): -1, 
            ('m', 'm'): 5, ('m', 'f'): 0, ('m', 'p'): -2, ('m', 's'): -1, ('m', 't'): -1, ('m', 'w'): -1, 
            ('m', 'y'): -1, ('m', 'v'): 1, ('m', 'b'): -3, ('m', 'z'): -1, ('m', 'x'): -1, ('m', '*'): -4,
            ('f', 'a'): -2, ('f', 'r'): -3, ('f', 'n'): -3, ('f', 'd'): -3, ('f', 'c'): -2, ('f', 'q'): -3, 
            ('f', 'e'): -3, ('f', 'g'): -3, ('f', 'h'): -1, ('f', 'i'): 0, ('f', 'l'): 0, ('f', 'k'): -3, 
            ('f', 'm'): 0, ('f', 'f'): 6, ('f', 'p'): -4, ('f', 's'): -2, ('f', 't'): -2, ('f', 'w'): 1, 
            ('f', 'y'): 3, ('f', 'v'): -1, ('f', 'b'): -3, ('f', 'z'): -3, ('f', 'x'): -1, ('f', '*'): -4, 
            ('p', 'a'): -1, ('p', 'r'): -2, ('p', 'n'): -2, ('p', 'd'): -1, ('p', 'c'): -3, ('p', 'q'): -1, 
            ('p', 'e'): -1, ('p', 'g'): -2, ('p', 'h'): -2, ('p', 'i'): -3, ('p', 'l'): -3, ('p', 'k'): -1, 
            ('p', 'm'): -2, ('p', 'f'): -4, ('p', 'p'): 7, ('p', 's'): -1, ('p', 't'): -1, ('p', 'w'): -4, 
            ('p', 'y'): -3, ('p', 'v'): -2, ('p', 'b'): -2, ('p', 'z'): -1, ('p', 'x'): -2, ('p', '*'): -4, 
            ('s', 'a'): 1, ('s', 'r'): -1, ('s', 'n'): 1, ('s', 'd'): 0, ('s', 'c'): -1, ('s', 'q'): 0, 
            ('s', 'e'): 0, ('s', 'g'): 0, ('s', 'h'): -1, ('s', 'i'): -2, ('s', 'l'): -2, ('s', 'k'): 0, 
            ('s', 'm'): -1, ('s', 'f'): -2, ('s', 'p'): -1, ('s', 's'): 4, ('s', 't'): 1, ('s', 'w'): -3, 
            ('s', 'y'): -2, ('s', 'v'): -2, ('s', 'b'): 0, ('s', 'z'): 0, ('s', 'x'): 0, ('s', '*'): -4, 
            ('t', 'a'): 0, ('t', 'r'): -1, ('t', 'n'): 0, ('t', 'd'): -1, ('t', 'c'): -1, ('t', 'q'): -1, 
            ('t', 'e'): -1, ('t', 'g'): -2, ('t', 'h'): -2, ('t', 'i'): -1, ('t', 'l'): -1, ('t', 'k'): -1, 
            ('t', 'm'): -1, ('t', 'f'): -2, ('t', 'p'): -1, ('t', 's'): 1, ('t', 't'): 5, ('t', 'w'): -2, 
            ('t', 'y'): -2, ('t', 'v'): 0, ('t', 'b'): -1, ('t', 'z'): -1, ('t', 'x'): 0, ('t', '*'): -4, 
            ('w', 'a'): -3, ('w', 'r'): -3, ('w', 'n'): -4, ('w', 'd'): -4, ('w', 'c'): -2, ('w', 'q'): -2, 
            ('w', 'e'): -3, ('w', 'g'): -2, ('w', 'h'): -2, ('w', 'i'): -3, ('w', 'l'): -2, ('w', 'k'): -3, 
            ('w', 'm'): -1, ('w', 'f'): 1, ('w', 'p'): -4, ('w', 's'): -3, ('w', 't'): -2, ('w', 'w'): 11, 
            ('w', 'y'): 2, ('w', 'v'): -3, ('w', 'b'): -4, ('w', 'z'): -3, ('w', 'x'): -2, ('w', '*'): -4, 
            ('y', 'a'): -2, ('y', 'r'): -2, ('y', 'n'): -2, ('y', 'd'): -3, ('y', 'c'): -2, ('y', 'q'): -1, 
            ('y', 'e'): -2, ('y', 'g'): -3, ('y', 'h'): 2, ('y', 'i'): -1, ('y', 'l'): -1, ('y', 'k'): -2,
            ('y', 'm'): -1, ('y', 'f'): 3, ('y', 'p'): -3, ('y', 's'): -2, ('y', 't'): -2, ('y', 'w'): 2, 
            ('y', 'y'): 7, ('y', 'v'): -1, ('y', 'b'): -3, ('y', 'z'): -2, ('y', 'x'): -1, ('y', '*'): -4, 
            ('v', 'a'): 0, ('v', 'r'): -3, ('v', 'n'): -3, ('v', 'd'): -3, ('v', 'c'): -1, ('v', 'q'): -2, 
            ('v', 'e'): -2, ('v', 'g'): -3, ('v', 'h'): -3, ('v', 'i'): 3, ('v', 'l'): 1, ('v', 'k'): -2, 
            ('v', 'm'): 1, ('v', 'f'): -1, ('v', 'p'): -2, ('v', 's'): -2, ('v', 't'): 0, ('v', 'w'): -3, 
            ('v', 'y'): -1, ('v', 'v'): 4, ('v', 'b'): -3, ('v', 'z'): -2, ('v', 'x'): -1, ('v', '*'): -4, 
            ('b', 'a'): -2, ('b', 'r'): -1, ('b', 'n'): 3, ('b', 'd'): 4, ('b', 'c'): -3, ('b', 'q'): 0, 
            ('b', 'e'): 1, ('b', 'g'): -1, ('b', 'h'): 0, ('b', 'i'): -3, ('b', 'l'): -4, ('b', 'k'): 0, 
            ('b', 'm'): -3, ('b', 'f'): -3, ('b', 'p'): -2, ('b', 's'): 0, ('b', 't'): -1, ('b', 'w'): -4, 
            ('b', 'y'): -3, ('b', 'v'): -3, ('b', 'b'): 4, ('b', 'z'): 1, ('b', 'x'): -1, ('b', '*'): -4, 
            ('z', 'a'): -1, ('z', 'r'): 0, ('z', 'n'): 0, ('z', 'd'): 1, ('z', 'c'): -3, ('z', 'q'): 3, 
            ('z', 'e'): 4, ('z', 'g'): -2, ('z', 'h'): 0, ('z', 'i'): -3, ('z', 'l'): -3, ('z', 'k'): 1, 
            ('z', 'm'): -1, ('z', 'f'): -3, ('z', 'p'): -1, ('z', 's'): 0, ('z', 't'): -1, ('z', 'w'): -3, 
            ('z', 'y'): -2, ('z', 'v'): -2, ('z', 'b'): 1, ('z', 'z'): 4, ('z', 'x'): -1, ('z', '*'): -4, 
            ('x', 'a'): 0, ('x', 'r'): -1, ('x', 'n'): -1, ('x', 'd'): -1, ('x', 'c'): -2, ('x', 'q'): -1, 
            ('x', 'e'): -1, ('x', 'g'): -1, ('x', 'h'): -1, ('x', 'i'): -1, ('x', 'l'): -1, ('x', 'k'): -1, 
            ('x', 'm'): -1, ('x', 'f'): -1, ('x', 'p'): -2, ('x', 's'): 0, ('x', 't'): 0, ('x', 'w'): -2, 
            ('x', 'y'): -1, ('x', 'v'): -1, ('x', 'b'): -1, ('x', 'z'): -1, ('x', 'x'): -1, ('x', '*'): -4, 
            ('*', 'a'): -4, ('*', 'r'): -4, ('*', 'n'): -4, ('*', 'd'): -4, ('*', 'c'): -4, ('*', 'q'): -4, 
            ('*', 'e'): -4, ('*', 'g'): -4, ('*', 'h'): -4, ('*', 'i'): -4, ('*', 'l'): -4, ('*', 'k'): -4, 
            ('*', 'm'): -4, ('*', 'f'): -4, ('*', 'p'): -4, ('*', 's'): -4, ('*', 't'): -4, ('*', 'w'): -4, 
            ('*', 'y'): -4, ('*', 'v'): -4, ('*', 'b'): -4, ('*', 'z'): -4, ('*', 'x'): -4, ('*', '*'): 1}

if __name__ == '__main__':
    pass