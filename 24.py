import utils

def get_inpt():
    inpt = utils.read_input("24")
    inpt_parsed = []
    for line in inpt:
        command = line.split(" ")[0]
        variables = line.split(" ")[1:]
        inpt_parsed.append((command, variables))

    inpt_batched = []
    batch = []
    batch.append(inpt_parsed[0])
    for line in inpt_parsed[1:]:
        if line[0] == "inp":
            inpt_batched.append(batch)
            batch = []
        batch.append(line)
    inpt_batched.append(batch)
            
    return inpt_batched

#Findings:
# - w is always equal to latest input
# - x and y are always "reset" before they are used in each input cycle
# - z is carried over from each input cycle
# => Each cycle is determined by input digit and z, and returns a new value for z

# There is a pattern in the code - only two of the input rows matter for the batch
# Row 6 : Used in the modulo check -> a
# Row 16 : Offset in the final output -> b
# -> Simplified in the function batch_output

def batch_output(inpt_digit, z, a, b):
    # Returns z for a given batch using input digit, z input and batch variables
    cond = int(z % 26 + a != inpt_digit)
    if a < 0:
        z = z // 26
    if cond:
        z = z * 26 + inpt_digit + b

    return z

def get_batch_variables():
    # Returns batch parameters for each batch
    inpt = get_inpt()
    batch_variables = []
    for batch in inpt:
        batch_variables.append([int(batch[5][1][1]), int(batch[15][1][1])])

    return batch_variables

def find_digits(batch_variables):
    z_all = dict()
    #The first line of input is and z = 0
    z_batch = {0}
    z_all[-1] = z_batch

    # For each batch, find the valid output using last batch's valid z output and any digit
    for batch, batch_vars in enumerate(batch_variables):
        z_batch_out = set()
        for z in z_batch:
            for inpt_digit in range(1, 10):
                z_out = batch_output(inpt_digit, z, *batch_vars)
                if batch_vars[0] > 0 or (batch_vars[0] < 0 and (z % 26 + batch_vars[0] == inpt_digit)):
                    z_batch_out.add(z_out)
        z_batch = z_batch_out
        z_all[batch] = z_batch

    #Start finding all valid digits
    digit_candidates = dict()

    #Loop backwards since the final z is known
    for batch, batch_vars in zip(range(14)[::-1], batch_variables[::-1]):
        digit_candidates[batch] = set()

        #All valid input values
        z_candidates = z_all[batch - 1]

        #All valid output values
        z_targets = z_all[batch]

        for z in z_candidates.copy():
            found_any = False
            for input_digit in range(1,10):
                if batch_output(input_digit, z, *batch_vars) in z_targets:
                    #Valid input leads to valid output - save the input digit
                    digit_candidates[batch].add(input_digit)
                    found_any = True
            if not found_any:
                z_all[batch - 1].remove(z)
    return digit_candidates

def get_first_solution():
    # Collection of variables a and b for each batch
    batch_variables = get_batch_variables()

    res = find_digits(batch_variables)
    solution = ""
    for digit in res.values():
        solution += str(max(digit))
    solution = solution[::-1]

    print(solution)

def get_second_solution():
    batch_variables = get_batch_variables()

    res = find_digits(batch_variables)
    solution = ""
    for digit in res.values():
        solution += str(min(digit))
    solution = solution[::-1]

    print(solution) 
    

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()