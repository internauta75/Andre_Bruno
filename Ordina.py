# Application test, problem:
# You have an array containing integers, and you have a reference number.
# Example:
# Array = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
# Reference = 10
# You have to sort the array, based on the distance from the reference number, from the closest to the most distant, and get a result similar to this:
# {10,9,11,8,12,7,13,6,14,5,15,4,16,3,17,2,18,1,19,20}
# The input sequence can be different and random, there may be duplicate numbers. Different outputs can be valid, in the example also the sequence that starts with {10,11,9 ...}.
# Another example to test your algorithm:
# Reference = 25
# Input: {11,7,42,7,3,8,5,48,24,45,32,21}
# Output: {24,21,32,11,8,42,7,7,5,45,3,48}
# The winner will be the one who writes the algorithm that does this faster. I will do a benchmark test to test the speed.
# Send me the solution privately so the others don't copy it
# You can take this code as a base and complete it:
# https://dotnetfiddle.net/mwzSZ4
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Se voglio una lista di 13 unita generate randomicamente, uso il modulo random #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# import random
# Matrice_random= []   creo la lista vuota che conterra i 13 numeri generati dal for successivo 
# for i in range(1,13):
#     Matrice_random.append(random.randrange(1,100)) # Riempio la lista per 13 volte con dei numeri randomici 

Matrice =[11,7,42, 7,3,8,5,48,24,45,32,21]
Riferimento = 25
DictOutput = []

for n,v in enumerate(Matrice): #cambiare con Matrice_random se si vuole usare una lista casuale
    if v >Riferimento:
        n = v - Riferimento
        DictOutput.append([n,v])
    elif v < Riferimento:
        n = Riferimento - v
        DictOutput.append([n,v]) 
    elif v == Riferimento:
        DictOutput.append([1,v]) 
    else:
        print("Error")

nuova_dict = sorted(DictOutput[:])

sorted_list_output = []
for k,v in sorted(DictOutput[:]):
    sorted_list_output.append(v)

print(sorted_list_output)
