import urllib3


def main(http):
    return [http.request('HEAD', 'http://example.com') for _ in range(1000)]


if __name__ == '__main__':
    http = urllib3.PoolManager()
    _ = main(http)
