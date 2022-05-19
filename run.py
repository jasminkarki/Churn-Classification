import argparse

from src.main import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--out', default=None)

    args = parser.parse_args()
    main(args.data)