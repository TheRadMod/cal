#!/usr/bin/env python3

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import argparse
import sys
from pyxirr import xirr

def get_value_time_combo(combos) -> list:
    
    try:
        new_combos = []
        for x in combos:
            split = x.split(':')
            if len(split) != 2:
                print("error: Input values must be in the format 'value(float):time(int)'")
                sys.exit(1)
            new_combos.append({float(split[0]):int(split[1])})
        combos = new_combos
    except:
        print("error: Input values must be in the format 'value(float):time(int)'")
        sys.exit(1)
    return combos


def main():
    
    if not sys.stdin.isatty():
        input_values = sys.stdin.read().split()
        input_values = get_value_time_combo(input_values)
    else:
        input_values = []


    parser = argparse.ArgumentParser(description="Calculate the xirr for a series of cash flows")
    parser.add_argument('-t', '--time', type=str, choices=['y', 'm', 'd'], help="Time in years, monthyl or daily")
    parser.add_argument('value_time_combo', type=str, nargs='+', help="Value and time of the cash flows")
    args = parser.parse_args()

    parser_value_time_combos = [x for combo in args.value_time_combo for x in combo.split()]

    parser_value_time_combos = get_value_time_combo(parser_value_time_combos) 

    total_value_time_combos = input_values + parser_value_time_combos

    if len(total_value_time_combos) <= 1:
        parser.error('You need to provide at least two value.')

    if not args.time:
        time = 'm'
    else:
        time = args.time
    today = datetime.today()    
    values_list = []
    date_list = []
    for combo in total_value_time_combos:
        for value, time_back in combo.items():
            values_list.append(value)
            if time == 'y':
                date = today - relativedelta(years=time_back)
            elif time == 'm':
                date = today - relativedelta(months=time_back)
            elif time == 'd':
                date = today - timedelta(days=time_back)
            date_list.append(date)

    my_xirr = xirr(date_list, values_list) 
    # print(f'{total_values=}, {input_values=}, {args.values=}, {args.monthly=}, {args.time=}')
    print(f"{my_xirr*100:.2f}")

if __name__ == "__main__":
    main()

