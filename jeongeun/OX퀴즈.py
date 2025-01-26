num_cases = int(input())
test_cases = []

for _ in range(num_cases):
    test_cases.append(input().strip())

for case in test_cases:
    
    score = 0
    current_streak = 0
    
    for result in case:
        
        if result == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0
            
    print(score)
