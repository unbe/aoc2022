shape_pairs = {
     # Their Rock  Paper   Scissors 
     'X': {'A': 3, 'B': 0, 'C': 6},  # My Rock
     'Y': {'A': 6, 'B': 3, 'C': 0},  # My Paper
     'Z': {'A': 0, 'B': 6, 'C': 3},  # My Scissors
}
              #  Rock  Paper   Scissors 
shape_scores = {'X': 1, 'Y': 2, 'Z': 3} 


with open("input.txt", "r") as f:
    score = 0
    for _, line in enumerate(f):
        their, mine = line.strip().split(' ')
        score += shape_scores[mine]
        score += shape_pairs[mine][their]

print(score)
