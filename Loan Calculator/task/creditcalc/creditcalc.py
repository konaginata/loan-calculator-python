import argparse

from math import ceil, floor, log, pow

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()
if args.type is None or args.type not in ('annuity', 'diff') or args.interest is None or args.interest < 0:
    print('Incorrect parameters')
    exit()
rate = args.interest / (12 * 100)
if args.type == 'annuity':
    required = None
    if args.payment is None and args.principal > 0 and args.periods > 0:
        required = "payment"
    if args.principal is None and args.payment > 0 and args.periods > 0:
        required = "principal"
    if args.periods is None and args.payment > 0 and args.principal > 0:
        required = "periods"
    match required:
        case 'payment':
            payment = args.principal * rate * pow(1 + rate, args.periods) / (pow(1 + rate, args.periods) - 1)
            print(f'Your annuity payment = {ceil(payment)}!')
            overpayment = ceil(payment) * args.periods - args.principal
            print(f'Overpayment = {overpayment}')
        case 'principal':
            principal = args.payment / (rate * pow(1 + rate, args.periods) / (pow(1 + rate, args.periods) - 1))
            print(f'Your loan principal = {floor(principal)}!')
            overpayment = args.payment * args.periods - floor(principal)
            print(f'Overpayment = {overpayment}')
        case 'periods':
            periods = ceil(log(args.payment / (args.payment - rate * args.principal), 1 + rate))
            if periods < 12:
                print(f'You need {periods} months to repay this loan!')
            else:
                years = periods // 12
                months = ceil(periods % 12)
                output = [f'{years} year{"s" if years != 1 else ""}']
                if months:
                    output.append(f'{months} month{"s" if months != 1 else ""}')
                print(f'It will take {" ".join(output)} to repay this loan!')
            overpayment = args.payment * periods - args.principal
            print(f'Overpayment = {overpayment}')
        case _:
            print('Incorrect parameters')
else:
    if args.payment is None and args.principal > 0 and args.periods > 0:
        total_payment = 0
        for m in range(1, args.periods + 1):
            payment = ceil(args.principal / args.periods + rate
                           * (args.principal - (args.principal * (m - 1) / args.periods)))
            total_payment += payment
            print(f'Month {m}: payment is {payment}')
        overpayment = total_payment - args.principal
        print(f'\nOverpayment = {overpayment}')
    else:
        print('Incorrect parameters')
