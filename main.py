# imports
import sys
import operator

# initialize variables
numArguments = len(sys.argv)
erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']

# make sure the user enters exactly 3 arguments
if numArguments < 3 or numArguments >= 4:
    print("\nError! You entered " + str(len(sys.argv)) + " argument(s) (" + str(sys.argv) +
          "). Please enter exactly 3 arguments and try again.")
    sys.exit(1)
else:
    # allow the program to open any file
    storyFile = str(sys.argv[1])
    toSkipFile = str(sys.argv[2])

# manipulate file 1
with open(storyFile, "r") as story:
    words = story.read().lower()    # convert to lowercase; lower()

    for char in erasures:
        if char in words:
            words = words.replace(char, " ") # remove erasures; replace()

    words = words.split()   # convert to list; split()

# manipulate file 2
with open(toSkipFile, "r") as skip:   # file 2
    toDelete = skip.read().split(',')   # convert to list; split()

# remove identical words
for i in toDelete:
    while i in words:
        words.remove(i)

# create a dictionary
myDictionary = dict()

# add list elements to dictionary
for i in range(0, len(words) - 1):
    key = words[i] + ', ' + words[i + 1]
    try:
        myDictionary[key] += 1
    except:
        myDictionary[key] = 1

# sort values then reverse() to get top 5 pairs
myDictionary = sorted(myDictionary.items(), key=operator.itemgetter(1), reverse=True)[:5]

# display information
print("\nStory file name: %s" % sys.argv[1])
print("Skip word file name: %s" % sys.argv[2])
print("Skip Words: %s" % toDelete)
print("The five most frequently occuring word pairs are: ")

# print results
for az in myDictionary:
    print(az)
