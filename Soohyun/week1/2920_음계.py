scale = [int(i) for i in input().split()]
if sorted(scale) == scale: print("ascending")
elif sorted(scale, reverse=True) == scale: print("descending")
else: print("mixed")