"""This file is used for the logic of the translation."""

import string
import re
from num2words import num2words  # used for accurately translating numbers


def change(new_input):
    """Translate the string."""
    new = ''  # final translation
    extras = 'efmnoprt'  # multi instance cases
    valid_non_letters = f'{string.punctuation} '
    fail = 'Invalid input.'
    count = 0  # number length count
    i = 0  # index for iterating through message
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
            'seen': False,  # used to see if instance exists yet
        },
        'f': {
            'one': 'as',
            'extra': 'us',
            'seen': False,
        },
        'm': {
            'one': 'be',
            'extra': 'bo',
            'seen': False,
        },
        'n': {
            'one': 'bo',
            'extra': 'be',
            'seen': False,
        },
        'o': {
            'one': 'do',
            'extra': 'de',
            'seen': False,
        },
        'p': {
            'one': 's',
            'extra': 'i',
            'seen': False,
        },
        'r': {
            'one': 'ch',
            'extra': 'och',
            'seen': False,
        },
        't': {
            'one': 'pi',
            'extra': 'no',
            'seen': False,
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
        # the extra space here is for the index handling assignment
        message = new_input.lower() + ' '
    else:
        return fail

    for _ in range(len(message) - 1):
        if message[i] in change_cases.keys():  # if letter
            if 'seen' in change_cases[message[i]].keys():  # if multi instance
                if change_cases[message[i]]['seen']:  # if seen
                    temp = change_cases[message[i]]['extra']
                else:  # if first instance
                    change_cases[message[i]]['seen'] = True
                    temp = change_cases[message[i]]['one']
            elif 'two' in change_cases[message[i]].keys():  # if double case
                if message[i + 1] == message[i]:  # if double
                    temp = change_cases[message[i]]['two']
                    i += 1  # skip second letter in double
                    message += ' '  # for finishing the for loop
                else:  # if single
                    temp = change_cases[message[i]]['one']
            else:  # if base case
                temp = change_cases[message[i]]['one']

        if is_number(message, i):
            if count == 0:
                number, message, count = gather(message)
                new += number

        # reset instances if end of word
        if message[i] and message[i] in valid_non_letters:
            temp = message[i]
            for char in extras:  # efmnoprt
                change_cases[char]['seen'] = False

        if count > 0:  # wait to insert until through the number
            count -= 1
        else:  # add translated letter (or number) to new string
            new += temp

        i += 1  # next letter

    for j in range(len(new) - 1, 0, -1):  # remove spaces at the end
        if new[j] == ' ':
            new = new[:-1]
        else:
            break

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
    r = '-?(?=\d|\.)\d*\.?(?=\d)\d*'  # |42|4.2|.42|-42|-4.2|-.42|
    match = re.search(r, message)
    new = match.group(0)
    special_case = False

    count = len(new)  # used for skipping the number in the translate for loop
    for i in range(len(new)):
        message = message.replace(new[i], ' ', 1)  # remove number from message

    if new[0] == '-' and (new[1] == '.' or new[1] == '0'):  # weird case
        special_case = True

    new = change(num2words(float(new)))

    if special_case:
        new = 'beonbonsh ' + new

    return (new, message, count)


def is_number(message, i):
    """
    Check to see if the values given make a number.

    True: .1
    True: -1
    True: 1
    True: -.1
    False: ..
    False: --
    False: a
    False: -a
    False: .a
    """
    check_one = bool(message[i] == '.' or message[i] == '-')
    check_two = bool(check_one and message[i + 1] in string.digits)
    check_three = bool(message[i] and message[i] in string.digits)
    check_four = bool(message[i] == '-' and message[i + 1] == '.')
    check_five = bool(check_four and message[i + 2] in string.digits)
    return check_two or check_three or check_five
