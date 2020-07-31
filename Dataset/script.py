import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='Mounted data directory')
    args = parser.parse_args()

    print(f'Data: {args.data}')

    with open(args.data, 'r') as f:
        content = f.read()

    print(content)