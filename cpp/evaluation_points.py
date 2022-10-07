import numpy as np

import sys

def main():
    if len(sys.argv) < 4:
        exit("Give the following arguments: min max number_of_points")

    min_value = np.log10(float(sys.argv[1]))
    max_value = np.log10(float(sys.argv[2]))
    number =    int(sys.argv[3])

    values = np.logspace(min_value, max_value, num=number)
    values_string = " ".join([str(i) for i in values])
    print(values_string)


if __name__ == "__main__":
    main()