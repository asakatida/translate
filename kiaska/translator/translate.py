"""This file is used for the logic of the translation."""

import string
import re
from num2words import num2words  # used for accurately translating numbers


def change(new_input):
    """Translate the string."""
    new = ''  # final translation
    last = ''  # temp for modifying
    extras = 'efmnoprt'  # multi instance cases
    valid_non_letters = f'{string.punctuation} '
    fail = 'Invalid input.'
    num = False  # if a num has been seen
    count = 0  # number length count
    change_cases = {
        'h': {'one': ''},  # Empty case
        'a': {'one': 'ki'},  # Basic cases
        'b': {'one': 'ul'},
        'c': {'one': 'va'},
        'd': {'one': 'po'},
        'i': {'one': 'on'},
        'j': {'one': 'bov'},
        'k': {'one': 'ae'},
        'l': {'one': 'ka'},
        'q': {'one': 'ss'},
        'u': {'one': 'n'},
        'v': {'one': 'u'},
        'w': {'one': 'nn'},
        'x': {'one': 'er'},
        'y': {'one': 'th'},
        'z': {'one': 'wat'},
        'e': {  # Multi instance cases
            'one': 'mo',  # first instance
            'extra': 'ma',  # extra instances
            'switch': False,  # used to see if instance exists yet
        },
        'f': {
            'one': 'as',
            'extra': 'us',
            'switch': False,
        },
        'm': {
            'one': 'be',
            'extra': 'bo',
            'switch': False,
        },
        'n': {
            'one': 'bo',
            'extra': 'be',
            'switch': False,
        },
        'o': {
            'one': 'do',
            'extra': 'de',
            'switch': False,
        },
        'p': {
            'one': 's',
            'extra': 'i',
            'switch': False,
        },
        'r': {
            'one': 'ch',
            'extra': 'och',
            'switch': False,
        },
        't': {
            'one': 'pi',
            'extra': 'no',
            'switch': False,
        },
        'g': {  # Double cases
            'one': 'bav',  # g
            'two': 'bavo',  # gg
        },
        's': {
            'one': 'sh',  # s
            'two': 'sha',  # ss
        },
    }

    if new_input:
        message = new_input.lower()
        message += ' '  # used for the letter/last assignment
    else:
        return fail

    for letter in message:  # letter is assigned to last and last is modified
        if last in change_cases.keys():  # if letter
            if 'switch' in change_cases[last].keys():  # if multi instance case
                if change_cases[last]['switch']:  # if seen
                    last = change_cases[last]['extra']
                else:  # if first instance
                    change_cases[last]['switch'] = True
                    last = change_cases[last]['one']
            elif 'two' in change_cases[last].keys():  # if double case
                if letter == last:  # if double
                    last = change_cases[last]['two']
                    letter = ''
                else:  # if single
                    last = change_cases[last]['one']
            else:  # if base case
                last = change_cases[last]['one']

        if (last == '.' or last == '-') and letter in string.digits:
            # used for numbers like .12 or -12
            if count > 0:  # used for skipping the remainder of a number
                pass
            else:
                temp, message, count = gather(message)
                new += temp
                num = True
        elif last and last in string.digits:  # if a number
            if count > 0:  # used for skipping the remainder of a number
                pass
            else:
                temp, message, count = gather(message)
                new += temp
                num = True

        # reset instances if end of word
        if last and last in valid_non_letters:
            for char in extras:
                change_cases[char]['switch'] = False

        if num:  # if a number is found then skip insertion
            num = False
            count -= 1
        elif count > 0:  # wait to insert until through the number
            count -= 1
        else:  # add translated letter (or number) to new string
            new += last

        last = letter

    return new


def gather(message):
    """
    Gather up the numbers and return the translation.

    Input the full message as a string and this will find the first
    instance of numbers and translate the whole number including negatives
    and decimals.

    This will output the final translated number, the original message not
    including the now translated number, and the length of the removed section
    of the string.  This will be formated in that order in a tuple.
    """
    r = '-?(?=\d|\.)\d*\.?(?=\d)\d*'
    match = re.search(r, message)
    new = match.group(0)

    message = message.replace(new, '', 1)
    count = len(new)

    if new[0] == '-' and new[1] == '.':
        count -= 1

    if '.' in new:  # float or int?
        new = change(num2words(float(new)))
    elif new:
        new = change(num2words(int(new)))

    return (new, message, count)
