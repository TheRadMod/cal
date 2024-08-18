#!/usr/bin/env python3

import argparse
import sys


def main():
    
    if not sys.stdin.isatty():
        input_values = sys.stdin.read().split()
        try:
            input_values = [float(x) for x in input_values]
        except:
            print("error: Input values must be numbers")
            sys.exit(1)

        if len(input_values) > 2:
            print("error: You need to provide at most two values (begin and end)")
            sys.exit(1)
    else:
        input_values = []


    parser = argparse.ArgumentParser(description="Calculate the cagr of an investment")
    parser.add_argument('-m', '--monthly', action = 'store_true', help="Is the investment monthly?")
    parser.add_argument('-d', '--daily', action = 'store_true', help="Is the investment monthly?")
    parser.add_argument('values', type=float, nargs='*', help="Values of Investment. Atleast one (end) is needed. begin is optional and defaults to 1")
    parser.add_argument('-t', '--time', type=float, required=True, help="Time (years is default)")
    args = parser.parse_args()

    total_values = input_values + args.values

    if len(total_values) > 2:
        parser.error('You need to provide at most two values (begin and end)')
    elif len(total_values) <= 0:
        parser.error('You need to provide at least one value (end)')

    begin = 1
    end = 1

    if len(total_values) == 1:
        end = total_values[0]
    elif len(total_values) == 2:
        begin = total_values[0]
        end = total_values[1]


    time = args.time if args.monthly is False else args.time / 12
    time = time if args.daily is False else args.time / 365

    cagr = (end / begin) ** (1 / time) - 1
    # print(f'{total_values=}, {input_values=}, {args.values=}, {args.monthly=}, {args.time=}')
    print(f"{cagr*100:.2f}")

if __name__ == "__main__":
    main()

