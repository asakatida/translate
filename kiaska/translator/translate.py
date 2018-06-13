"""This file is used for the logic of the translation."""

import string
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
        elif last in string.digits:  # if a number
            if count > 0:  # used for skipping the remainder of a number
                pass
            else:
                temp, message, count = gather(message)
                new += temp
                num = True

        if last in valid_non_letters:  # reset instances at end of word
            for char in extras:
                change_cases[char]['switch'] = False

        if num:  # if a number is found then skip insertion
            num = False
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
    num_stuff = '1234567890.-'
    new = ''

    is_num = False  # for loop below will always loop once
    neg_start = False
    dash = False

    for char in message:  # loop to strip number out of message
        if neg_start and char == '-':
            message = message.replace(char, '', 1)
            dash = True
            break
        elif char in num_stuff:
            neg_start = True
            is_num = True
            message = message.replace(char, '', 1)
            new += char
        elif is_num:
            break

    if new[-1] == '.':  # false positive decimal number handling
        new = new[:-1]

    if dash:
        count = len(new)
    else:
        count = len(new) - 1

    if '.' in new:  # float or int?
        new = change(num2words(float(new)))
    else:
        new = change(num2words(int(new)))

    if dash:
        new += '-'

    return (new, message, count)
