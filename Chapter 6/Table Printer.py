# Chapter 6 Practice Project
def findWidths(data: list) -> list:
    colWidths = [0] * len(data)
    for position, row in enumerate(data):
        for item in row:
            if len(item) > colWidths[position]:
                colWidths[position] = len(item)

    return colWidths

def printTable(data: list) -> str:
    widths = findWidths(data)
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(widths[j]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)