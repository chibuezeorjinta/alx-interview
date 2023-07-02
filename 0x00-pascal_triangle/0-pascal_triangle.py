#!/usr/bin/python3
# for the pascals triangle.
#my attempt will use recursion

def pascal_triangle(n) -> list:
	if n <= 0:
		return []
	pascalsList = [
		[1]
	]
	count = 1
	return createnewlist(pascalsList, count, n)

def createnewlist(mainList: list, count, n) -> list:
	if count == n:
		return mainList
	else:
		lastlist = mainList[-1]
		workingList = [0, 0]
		newList = []

		for item in lastlist:
			workingList.insert(len(workingList) - 1, item)
		for i in range(len(workingList) - 1):
			newList.append(workingList[i] + workingList[i+1])
		mainList.append(newList)
		count += 1
		return createnewlist(mainList, count, n)
