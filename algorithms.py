from matrices import blosum62
import numpy as np

def basic_scoring(a, b):
    if a == b:
        return +1
    else:
        return -1
    
def scoring(a, b, matrix = blosum62):
    score = matrix.get((a, b))
    if score is not None:
        return score
    else:
        return matrix.get((b, a))


def needlemanWunsch(seqA: str, seqB: str, scoring_function = scoring, gap_penalty=-8):
    lenA = len(seqA.lower()) # horizontal, i
    lenB = len(seqB.lower()) # vertical, j

    similirity_matrix = np.zeros((lenA + 1, lenB + 1), dtype=int)
    traceback_matrix = np.zeros((lenA + 1, lenB + 1, 3), dtype=int)

    similirity_matrix[:, 0] = np.arange(0, (lenA + 1) * gap_penalty, gap_penalty) 
    similirity_matrix[0, :] = np.arange(0, (lenB + 1) * gap_penalty, gap_penalty) 

    traceback_matrix[0, :, 0] = 1
    traceback_matrix[:, 0, 2] = 1

    for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                top_candidate = similirity_matrix[i-1,j] + gap_penalty
                left_candidate = similirity_matrix[i,j-1] + gap_penalty
                top_left_candidate = similirity_matrix[i-1,j-1] + scoring_function(seqA[i-1], seqB[j-1])

                maxscore = max(top_candidate, left_candidate, top_left_candidate)
                similirity_matrix[i,j] = maxscore

                #(left, topleft, top)
                if maxscore == left_candidate:
                    traceback_matrix[i, j, 0] = 1
                if maxscore == top_left_candidate:
                    traceback_matrix[i, j, 1] = 1
                if maxscore == top_candidate:
                    traceback_matrix[i, j, 2] = 1

    alignments = []
    i, j = lenA, lenB
    def traceback(i, j, alignment1, alignment2):
        if i == 0 and j == 0:
            alignments.append((alignment1[::-1], alignment2[::-1]))
            return
        if traceback_matrix[i, j, 0]: # left
            traceback(i, j-1, alignment1 + '-', alignment2 + seqB[j - 1])
        if traceback_matrix[i, j, 1]: # topleft
            traceback(i-1, j-1, alignment1 + seqA[i - 1], alignment2 + seqB[j - 1])
        if traceback_matrix[i, j, 2]: # top
            traceback(i-1, j, alignment1 + seqA[i - 1], alignment2 + '-')
        
    traceback(i, j, '', '')
    return alignments

if __name__ == "__main__":
    alignments = needlemanWunsch("TCGTT","GTTAC")
    for pair in alignments:
        print(f"{pair[0]}\n{pair[1]}\n")
