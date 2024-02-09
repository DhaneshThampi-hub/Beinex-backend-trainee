# Using for loop 
fibonacci_sequence = [0, 1]
for i in range(8):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
print("First 10 Fibonacci numbers using 'for' loop:", fibonacci_sequence)


# Using while loop 
fibonacci_sequence = [0, 1]
count = 2 

while count < 10:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
    count += 1
print("First 10 Fibonacci numbers using 'while' loop:", fibonacci_sequence)
