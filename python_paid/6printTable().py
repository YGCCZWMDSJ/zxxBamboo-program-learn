#! python 311
tableData=[['apples','oranges','cherried','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
numWidth=len(tableData) # 几列
coWidth=[max(len(item) for item in col) for col in tableData] # 几宽
for row in range(len(tableData[0])): # 几行
    for col in range(numWidth):
        print(tableData[col][row].rjust(coWidth[col]),end=' ')
    print()