#function to print rabbit pairs.
def print_pairs(n):
  #adding the first no of pairs of rabbit to the list
  rabbit_pair = [1,1]
  print("\nMonths\t\tNo of Pairs of Rabbit")
  #loop used to iterate upto n-months
  for i in range(0,n):
    #printing the month
    print(i+1,end="\t\t")
    #printing the pair of rabbits
    print(rabbit_pair[i])
    rabbit_pair.append(rabbit_pair[i]+rabbit_pair[i+1])

no_of_months = int(input("Enter the month upto which you want the table : "))
print_pairs(no_of_months)