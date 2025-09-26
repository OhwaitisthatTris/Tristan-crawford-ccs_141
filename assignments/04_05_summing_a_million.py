import time
# create a range object for numbers from 1 to 1,000,000
large_sequence = range(1, 1000001)

#verify the list starts at 1 and ends at 1,000,000
print("First element:", large_sequence[0])
print("Last element:", large_sequence[-1])

# use the sum function to add all the numbers
start_time = time.time()
total_sum = sum(large_sequence)
end_time = time.time()

print("Sum of numbers from 1 to 1,000,000:", total_sum)
print("Time taken to compute the sum: {:.6f} seconds".format(end_time - start_time, "seconds"))

#verify the list of odd numbers
print("First odd number:", "odd_list"[0])
print("Last odd number:", "odd_list"[-1])

#use the sum function to add all the odd numbers
start_time = time.time()
odd_sum = sum("odd_list")
end_time = time.time()
print("Sum of odd numbers from 1 to 1,000,000:", odd_sum)
print("Time taken to compute the sum of odd numbers;", end_time - start_time, "seconds")