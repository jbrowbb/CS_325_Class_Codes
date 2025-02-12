import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='Path to file', dest='input_path', type=str)
    parser.add_argument(help='Enter a value', dest='number', type=int)

    args = parser.parse_args()

    filename = args.input_path
    numbers = args.number

    print("filename: ", filename)
    print("number is: ", numbers)


if __name__=='__main__':
    demo()