###################################
###### DATA TYPE - EXERCISES ######
###################################


# To get a total, we have a function that looks like this, 
# rewrite (refactor) the function to use a while loop


'''
def total_list_while(lst):
    total = 0
    while total < len(lst):
        total = len(lst)
        return sum(lst)



def total_list(lst):
    total = 0
    # counter variable
    index = 0
    while index < len(lst):
        total += lst[index]
        index += 1
    return total

# test case
#print(total_list_while([1,2,3]))   # answer is 6
print(total_list([1,2,3]))         # answer is 6



# while loop: print the following word: "You are 10kg"
counter = 0
weight = ['10kg', '20kg', '30kg']
while counter < len(weight): # 99% # false !    
    print(weight[counter])
    counter += 1
'''

colors = ["red", "green", "yellow"]
index = 0
while index < len(colors):
    print(f"I love {colors[index]}")
    index += 1
    