import string

def P12_CompareFiles ():
    harvard_data = open("./Havard.txt", 'r', encoding='cp949')
    mit_data = open("./MIT.txt", "r", encoding='cp949')
    harvard_wset = set([])
    mit_wset = set([])

    for line in harvard_data:
        line_list = line.split()
        for word in line_list:
            word.strip(string.punctuation)
            word.lower()
            if len(word) >= 4:
                harvard_wset.add(word)
            

    for line in mit_data:
        line_list = line.split()
        for word in line_list:
            word.strip(string.punctuation)
            word.lower()
            if len(word) >= 4:
                mit_wset.add(word)

    print("Count of unique words of length 4 or greater")
    print("Harvard: {}, MIT: {}".format(len(harvard_wset), len(mit_wset)))
    print()
    print(" Operations                 Count ")
    print("==================================")
    print("{} {:26d}".format("Union", len(harvard_wset.union(mit_wset))))
    print("{} {:18d}".format("Intersection", len(harvard_wset.intersection(mit_wset))))
    print("{} {:11d}".format("Symmetric Difference", len(harvard_wset.symmetric_difference(mit_wset))))
    print("{} {:19d}".format("Harvard-MIT", len(harvard_wset.difference(mit_wset))))
    print("{} {:19d}".format("MIT-Harvard", len(mit_wset.difference(harvard_wset))))
    

print("#12")
P12_CompareFiles()
