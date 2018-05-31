"""This file is used for the logic of the translation."""

import sys
from num2words import num2words


def change(test=None):
    """Translate the string."""
    try:
        message = ''
        new = ''
        num_stuff = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        n, o, m, p, e, f, r, t = False, False, False, False, False, False, \
            False, False
        valid_non_letters = [',', ' ', '_', '?', '!', '(', ')', ':']
        fail = 'Try again. Valid inputs are letters, spaces, numbers and' \
            ' these special characters: . , - _ ? ! ( ) :'
        num = False
        count = 0

        if test:
            message = test.lower()
            message += ' '
        else:
            for item in sys.argv[1:]:
                message += item.lower()
                message += ' '

        last = ''
        for letter in message:
            if last == 'h':
                last = ''
            elif last == 'a':
                last = 'ki'
            elif last == 'q':
                last = 'ss'
            elif last == 'b':
                last = 'ul'
            elif last == 'c':
                last = 'va'
            elif last == 'd':
                last = 'po'
            elif last == 'i':
                last = 'on'
            elif last == 'j':
                last = 'bov'
            elif last == 'k':
                last = 'ae'
            elif last == 'l':
                last = 'ka'
            elif last == 'u':
                last = 'n'
            elif last == 'v':
                last = 'u'
            elif last == 'w':
                last = 'nn'
            elif last == 'x':
                last = 'er'
            elif last == 'y':
                last = 'th'
            elif last == 'z':
                last = 'wat'
            elif last == 's' and letter != 's':
                last = 'sh'
            elif last == 's' and letter == 's':
                last = 'sha'
                letter = ''
            elif last == 'n' and n is False:
                last = 'bo'
                n = True
            elif last == 'n' and n is True:
                last = 'be'
            elif last == 'o' and o is False:
                last = 'do'
                o = True
            elif last == 'o' and o is True:
                last = 'de'
            elif last == 'm' and m is False:
                last = 'be'
                m = True
            elif last == 'm' and m is True:
                last = 'bo'
            elif last == 'p' and p is False:
                last = 's'
                p = True
            elif last == 'p' and p is True:
                last = 'i'
            elif last == 'e' and e is False:
                last = 'mo'
                e = True
            elif last == 'e' and e is True:
                last = 'ma'
            elif last == 'f' and f is False:
                last = 'as'
                f = True
            elif last == 'g' and letter != 'g':
                last = 'bav'
            elif last == 'g' and letter == 'g':
                last = 'bavo'
                letter = ''
            elif last == 'f' and f is True:
                last = 'us'
            elif last == 'r' and r is False:
                last = 'ch'
                r = True
            elif last == 'r' and r is True:
                last = 'och'
            elif last == 't' and t is False:
                last = 'pi'
                t = True
            elif last == 't' and t is True:
                last = 'no'
            elif last in valid_non_letters:
                n, o, m, p, e, f, r, t = False, False, False, False, False, \
                    False, False, False
            elif last == '':
                last = ''
            elif (last == '.' or last == '-') and letter in num_stuff:
                if count > 0:
                    pass
                else:
                    temp, message, count = gather(message)
                    new += temp
                    num = True
            elif last == '.' or last == '-':
                n, o, m, p, e, f, r, t = False, False, False, False, False, \
                    False, False, False
            elif last in num_stuff:
                if count > 0:
                    pass
                else:
                    temp, message, count = gather(message)
                    new += temp
                    num = True
            else:
                last = 'FAILED'
            if num is True:
                num = False
            elif count > 0:
                count -= 1
            else:
                new += last
            last = letter

        if 'FAILED' in new:
            return fail
        else:
            return new

    except Exception:
        return fail


def gather(message):
    """
    Gather up the nums and return the translation.

    Input the full message as a string and this will find the first
    instance of numbers and translate the whole number including negatives
    and decimals.

    This will output the final translated number, the original message not
    including the now translated number, and the length of the removed section
    of the string.  This will be formated in that order in a tuple.
    """
    num_stuff = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']
    new = ''

    num = 0

    for char in message:
        if char in num_stuff and (num == 0 or num == 1):
            num = 1
            message = message.replace(char, '', 1)
            new += char
        elif num == 1:
            break

    if new[-1] == '.':
        new = new[:-1]

    count = len(new) - 1

    if '.' in new:
        new = change(num2words(float(new)))
    else:
        new = change(num2words(int(new)))

    return (new, message, count)


if __name__ == '__main__':
    print(change())
