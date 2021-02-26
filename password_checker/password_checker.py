import hashlib
import sys

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data: {res.status_code}. Try again?')
    return res


def get_password_leaked_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if hash_to_check in h:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, tail = sha1password[:5], sha1password[5:]
    passwords = request_api_data(first_5)
    return get_password_leaked_count(passwords, tail)


def main(args):
    for password in args:
        compromised = pwned_api_check(password)
        if compromised:
            print(f"{password} has been compromised {compromised} times.")
        else:
            print(f"{password} has not been compromised!")
    return "Finished."


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
