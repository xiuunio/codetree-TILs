score = int(input())

grade = 0 if score == 100 else 1
print("pass") if grade==0 else print("failure")