current_hour = int(input("Enter the Current Hour [0-11]: "))
duration = int(input("Enter the duration (any pos int): "))

print(f"After {duration} hour(s),the clock will " +
f"read {(duration + current_hour) % 12} hour(s).")