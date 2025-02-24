import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--link', dest='url', help='Please give a URL to download', type=str)
    parser.add_argument('--num', dest='num', help='Some Number', type=str)

    args = parser.parse_args()

    filename = args.url
    numbers = args.number

    print("filename: ", filename)
    print("number is: ", numbers)


if __name__=='__main__':
    demo()