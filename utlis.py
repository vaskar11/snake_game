numbers=[10,34,22,12,45]
def findmax(numbers) :
    maximum=0
    for i in numbers:
      if i > maximum:
          maximum=i
    return maximum

maxx=findmax(numbers)
print(maxx)

