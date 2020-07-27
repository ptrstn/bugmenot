import argparse

import pandas

import bugmenot
from bugmenot import __version__


def parse_arguments():
    parser = argparse.ArgumentParser(description="An unofficial BugMeNot.com client")

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument("url", help="URL to the website")

    return parser.parse_args()


def main():
    args = parse_arguments()
    website = args.url
    credentials = bugmenot.get_credentials(website)
    print(pandas.DataFrame(credentials))


if __name__ == "__main__":
    main()
