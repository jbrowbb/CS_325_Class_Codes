import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help="Enter a path", dest="input_path", type=str)
    parser.add_argument(help="Enter a number", dest="number", type=int)

    args = parser.parse_args()

    path = args.input_path
    num = args.number

    print("The path is: ", path)
    print("The number is: ", num)