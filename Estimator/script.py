import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--meaning', type=int, help='What is the meaning of life?')
    args = parser.parse_args()

    print(f'The meaning of life is {args.meaning}.')