def printTable(tableData):
    # Create a list to store the maximum width of each column
    colWidths = [0] * len(tableData)

    # Find the longest string in each column
    for col in range(len(tableData)):
        for item in tableData[col]:
            if len(item) > colWidths[col]:
                colWidths[col] = len(item)

    # Print the table row by row
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print()
