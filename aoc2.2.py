rules = {
   # Their Rock      Paper     Scissors 
     'X': {'A': 'C', 'B': 'A', 'C': 'B'},  # Lose
     'Y': {'A': 'A', 'B': 'B', 'C': 'C'},  # Draw
     'Z': {'A': 'B', 'B': 'C', 'C': 'A'},  # Win
}
              #  Rock  Paper   Scissors 
shape_scores = {'A': 1, 'B': 2, 'C': 3} 
outcome_scores = {'X': 0, 'Y': 3, 'Z': 6} 


with open("input.txt", "r") as f:
    score = 0
    for _, line in enumerate(f):
        their, outcome = line.strip().split(' ')
        mine = rules[outcome][their]
        score += shape_scores[mine] + outcome_scores[outcome]

print(score)
