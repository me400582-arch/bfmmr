import itertools
def sum_of_values(values, keys):
  sum= 0
  n = len(values)
  for i in range (n):
    sum += values [i] * keys[i]
  return sum

def knapsack_problem(profits, weights, capacity, goal):
  n = len(profits)
  sequence = itertools.product([0,1],repeat = n)
  for sequence in sequence:
       if sum_of_values(weights, sequence) <= capacity\
       and sum_of_values(profits, sequence) >= goal:
             return sequence
  return False