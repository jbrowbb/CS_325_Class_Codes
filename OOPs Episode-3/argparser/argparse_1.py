import argparse

# Example command to run this program: python3 argparse_1.py 3 7
# Or python3 argparse_1.py -h

def demo() -> None:
    parse = argparse.ArgumentParser()

    parse.add_argument(help="first integer value", dest='value1', type= int)
    parse.add_argument(help="second interger number", dest='value2', type= int)

    args = parse.parse_args()

    x = args.value1
    y = args.value2

    print(" the addition and scaled up values of the input numbers are", x+y, x*2 + y*2)


if __name__=="__main__":
    demo()