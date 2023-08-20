n = int(input())
ls = []

for i in range (n):
    ls.append(int(input()))
    
# print(ls)
q = int(input())
questions = []

for i in range (q):
    questions.append(int(input()))

def search(arr, x):
    
	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

for question in questions:
    print(search(ls, question))