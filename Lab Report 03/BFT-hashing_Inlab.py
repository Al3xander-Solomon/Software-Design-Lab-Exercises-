def HashingofT(TableofHash):
    for i in range(len(TableofHash)):
        print(i, end=" ")

        for j in TableofHash[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


# Creating Hashtable as
# a nested list.
TableofHash = [[] for _ in range(10)]


# Hashing Function to return
def Hashing(key):
    return key % len(TableofHash)


# Insert Function to add
# values to the hash table
def insertofval(TableofHash, key, value):
    hash_key = Hashing(key)
    TableofHash[hash_key].append(value)


# Driver Code
insertofval(TableofHash, 11, 'Japan')
insertofval(TableofHash, 22, 'Philippines')
insertofval(TableofHash, 44, 'China')
insertofval(TableofHash, 45, 'Singapore')
insertofval(TableofHash, 24, 'Vietnam')
insertofval(TableofHash, 19, 'Indonesia')

HashingofT(TableofHash)