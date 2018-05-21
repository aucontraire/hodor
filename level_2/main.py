#!/usr/bin/python3
import requests


def cheat_vote(times=1):
    """cheat_vote - cheat online voting form
    Args:
        times (int): number of times to vote

    """
    payload = {'id': '350', 'holdthedoor': 'Submit', 'key': '0'}
    url = "http://158.69.76.135/level2.php"
    session = requests.Session()
    cookies = dict(HoldTheDoor='0')

    user_agent = [
        "Mozilla/5.0",
        "(Windows NT 5.1)",
        "AppleWebKit/537.11",
        "(KHTML, like Gecko)",
        "Chrome/23.0.1271.6 Safari/537.11"
    ]

    session.headers.update(
        {
            'User-Agent': " ".join(user_agent),
            'Connection': 'keep-alive',
            'Referer': 'http://158.69.76.135/level2.php',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )

    for i in range(times):
        r = session.post(url, payload, cookies=cookies)


if __name__ == '__main__':
    times = 1024
    cheat_vote(times)
