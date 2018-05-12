#!/usr/bin/python3
import requests


def cheat_vote(times=1):
    """cheat_vote - cheat online voting form
    Args:
        times (int): number of times to vote

    """
    payload = {'id': '350', 'holdthedoor': 'Submit'}
    url = "http://158.69.76.135/level0.php"

    session = requests.Session()
    for i in range(times):
        r = session.post(url, payload)


if __name__ == '__main__':
    times = 1024
    cheat_vote(times)
