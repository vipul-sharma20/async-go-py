import requests


def main():
    return [requests.head('http://example.com') for i in range(1000)]


if __name__ == '__main__':
    _ = main()
