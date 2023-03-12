import math

with open("TPSC_large.txt", "r") as infile, open("TPSC_large_output.txt", "w") as outfile:
    # read the number of test cases
    T = int(infile.readline())

    # loop through all test cases
    for t in range(1, T+1):
        # read the input values
        B, C, D = map(int, infile.readline().split())
        customers = list(map(int, infile.readline().split()))

        # calculate the total number of customers
        N = sum(customers)

        # initialize variables
        bench_count = 0
        stool_count = 0
        total_rent = 0

        # loop through the time intervals
        for i, num_customers in enumerate(customers):
            # calculate the required seating capacity
            required_capacity = math.ceil(num_customers / 2)

            # check if additional furniture is needed
            if required_capacity > bench_count + stool_count:
                # calculate the number of benches and stools needed
                num_benches = required_capacity - (stool_count + bench_count)
                if num_benches % 2 == 1:
                    num_benches -= 1
                    bench_count += 1
                    total_rent += D

                num_stools = num_benches // 2
                stool_count += num_stools
                total_rent += num_stools * C

            # update the seating counts for the next interval
            if i % B == B-1:
                bench_count = 0
                stool_count = 0

        # write the output for the test case
        outfile.write(f"Case #{t}: {bench_count+stool_count} {total_rent}\n")
