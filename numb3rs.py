import random

print("hello")
# Create an array of 10 items, 1 through 10
array = list(range(1,401))
#print(array)
# Shuffle the array using random.shuffle
#random.shuffle(array)

#print(array)

# Define a function to shuffle an array using Fisher-Yates algorithm
def fisher_yates_shuffle(array):
    # Loop from the last element to the second element
    for i in range(len(array)-1,0,-1):
        # Generate a random index from 0 to i
        j = random.randint(0,i)
        # Swap array[i] and array[j]
        array[i],array[j] = array[j],array[i]

# Create another array of 10 items, 1 through 10
array2 = list(range(1,401))

# Shuffle the array using fisher_yates_shuffle
fisher_yates_shuffle(array2)

array = [0]*400
##print(array)
# Print the shuffled array
##print(array2)

for i in range(0,200000):
    #print(" ")

    fisher_yates_shuffle(array2)
    ##print(array2)
    
    for j in range (0,400):
        array[j] = array[j] + array2[j]
    ##print(array)

#print(array)

for k in range (0,400):
    array[k] = array[k]/10000000

for k in range (0,400):
    array[k] = array[k]-4
    array[k] = round((array[k]+.05)*100,2)
    
array3 = [0]*130

for k in range (0,400):
    print(array[k])
    #print(round(array[k],1))
    num = round(array[k],1)*10
    num = int(num)
    array3[num] = array3[num] + 1

#print(array)

array.sort()

print(array3)
