import sys


def change(test=None):
    try:
        message = ''
        new = ''
        n = False
        o = False
        m = False
        p = False
        e = False
        f = False
        r = False
        t = False

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
            elif last == ' ' or last == '-':
                n = False
                o = False
                m = False
                p = False
                e = False
                f = False
                r = False
                t = False
            elif last == '':
                last == ''
            else:
                last = 'FAILED'
            new += last
            last = letter

        if 'FAILED' in new:
            return 'Try again. Valid inputs are letters, spaces, and dashes.'
        else:
            return new

    except Exception:
        return 'Try again. Valid inputs are letters, spaces, and dashes.'


if __name__ == '__main__':
    print(change())
