import utils

def get_first_solution():
    inpt = utils.read_input("3")
    gamma = [1 if sum([int(inpt_row[idx]) for inpt_row in inpt]) >= len(inpt)/2 else 0 for idx in range(12)]
    alpha = [(1 - gamma_bit) for gamma_bit in gamma]

    alpha_dec = int("".join([str(bit) for bit in alpha]),2)
    gamma_dec = int("".join([str(bit) for bit in gamma]),2)

    print(alpha_dec * gamma_dec)

def get_second_solution():
    inpt = utils.read_input("3")

    co2_found = False
    oxy_found = False

    bit_idx = 0

    co2 = inpt.copy()
    oxy = inpt.copy()

    while (not co2_found) or (not oxy_found) or (bit_idx < 12):
        least_common_bit_co2 = 0 if sum([int(inpt_row[bit_idx]) for inpt_row in co2]) >= len(co2)/2 else 1
        most_common_bit_oxy = 1 if sum([int(inpt_row[bit_idx]) for inpt_row in oxy]) >= len(oxy)/2 else 0
        if not co2_found:
            co2 = [bits for bits in co2 if int(bits[bit_idx]) == least_common_bit_co2]
            if len(co2) == 1:
                co2_found = True
        if not oxy_found:
            oxy = [bits for bits in oxy if int(bits[bit_idx]) == most_common_bit_oxy]
            if len(oxy) == 1:
                oxy_found = True

        bit_idx += 1

    print(int(co2[0], 2) * int(oxy[0], 2))




if __name__ == "__main__":
    get_first_solution()
    get_second_solution()