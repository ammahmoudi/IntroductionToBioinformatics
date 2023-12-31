#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Local Alignment with Affine Gap Penalty
Rosalind ID: LAFF
Rosalind #: 103
URL: http://rosalind.info/problems/laff/
'''


def local_alignment_affine_gap_penalty(v, w, scoring_matrix, sigma, epsilon):
    '''
    Returns the score and local alignment substrings for strings v, w with the
    given scoring matrix, gap opening penalty sigma, and gap extension penalty epsilon.
    '''

    # Initialize the matrices.
    S_lower = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    S_middle = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    S_upper = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    backtrack = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]

    # Initialize the maximum score below the lowest possible score.
    max_score = -1
    max_i, max_j = 0, 0

    # Fill in the Score and Backtrack matrices.
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            S_lower[i][j] = max([S_lower[i-1][j] - epsilon, S_middle[i-1][j] - sigma])
            S_upper[i][j] = max([S_upper[i][j-1] - epsilon, S_middle[i][j-1] - sigma])
            middle_scores = [S_lower[i][j], S_middle[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S_upper[i][j], 0]
            S_middle[i][j] = max(middle_scores)
            backtrack[i][j] = middle_scores.index(S_middle[i][j])

            if S_middle[i][j] > max_score:
                max_score = S_middle[i][j]
                max_i, max_j = i, j

    # Initialize the indices to start at the position of the high score.
    i, j = max_i, max_j

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    # Note: the solution format specifically asks for substrings, so no indel insertion necessary.
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
        elif backtrack[i][j] == 1:
            i -= 1
            j -= 1
        elif backtrack[i][j] == 2:
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return str(max_score), v_aligned, w_aligned


if __name__ == '__main__':
    import FASTA
    import scoring_matrices

   # Parse the two input protein strings.
    s, t = [fasta[1] for fasta in FASTA.ReadFASTA('5.txt')]

    # Get the local alignment (given sigma = 11, epsilon = 1 in problem statement).
    alignment = local_alignment_affine_gap_penalty(s, t, scoring_matrices.BLOSUM62(), 11, 1)

    # Print and save the answer.
    print ('\n'.join(alignment))
    with open('5_out.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))