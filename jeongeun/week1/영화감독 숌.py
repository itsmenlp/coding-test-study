def find_end_of_world_number(n):
    count = 0
    current_number = 666
    
    while True:
        if '666' in str(current_number):
            count +=1
            if count == n:
                return current_number
        current_number += 1
        
n = int(input())
print(find_end_of_world_number(n))
