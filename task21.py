def all_unique(numbers):
    for i in range (0,len(numbers)):
        if numbers[i]==numbers[i+1]:
            break
        print(False)
    else: print(True)

all_unique(10)