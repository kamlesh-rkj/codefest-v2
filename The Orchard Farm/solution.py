# open input and output files
with open('TOF_small.txt', 'r') as f, open('TOF_small_output.txt', 'w') as out_file:
    # read the first line which contains the quantity
    qty = int(f.readline().strip())

    # initialize an empty list to store the results
    result = []

    # loop over the remaining lines in the file
    for line in f:
        # split each line into two values
        value1, value2 = map(int, line.strip().split())

        # calculate the growth rate and add it to the results list
        growth_rate = (value2 - value1) / value1
        result.append(growth_rate)

    # sort the results in descending order
    result.sort(reverse=True)

    # write the top "qty" growth rates to the output file
    for i in range(qty):
        out_file.write(str(result[i]) + '\n')
