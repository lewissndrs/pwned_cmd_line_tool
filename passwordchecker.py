#  cmd line program to test passwords using the pwnedpasswords API

import hashlib
import requests
import sys

def main(inputPW):
    # encrypt password & print hash to line
    hashedPw = hashlib.sha1(inputPW.encode('utf-8')).hexdigest().upper()
    print('')
    print('your password is: '+ hashedPw)
    print('')

    # assign head and tail to variables
    head = hashedPw[:5]
    tail = hashedPw[5:]

    # make url request (maybe put in a helper function)
    url = 'https://api.pwnedpasswords.com/range/' + head

    res = requests.get(url)
    # put the response into a dict
    hashes = dict(h.split(':') for h in res.text.splitlines())

    # iterate through list to see if any matches occur
    found = False
    for key in hashes:

        if key == tail:
            found = True
            print('match found!: '+ key)
            print('this password has been leaked '+hashes.get(key) +' times')

    if found == False:
        print('No matches found! Your password is probably fine.')

    # end of function
    return

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))