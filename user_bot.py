


def script(check, x, y):
    if (check('level') == 1):
        if (not (check('wall', x + 2, y))):
            if check('gold', x, y) > 0:
                return 'take'
            return 'right'
        if (check('level') == 1):
            if (check('gold', x, y) > 0):
                return 'take'
            return 'down'
    if (check('level') == 2):
        if (check('gold', x, y) > 0):
            return 'take'
        if (not (check('wall', x + 2, y)) and not (check('gold', x, y - 1)) and not (check('gold', x, y + 1))):
            return 'right'
        elif (not (check('wall', x, y - 1)) and not (check('gold', x, y + 1)) and not (check('gold', x + 1, y))):
            return 'up'
        elif (not (check('wall', x, y + 1)) and not (check('gold', x + 1, y))):
            return 'down'
        return 'right'

    if (check('level') == 3):
        if check('gold', x, y):
            return 'take'
        if check('wall', x - 1, y) and not check('wall', x, y - 1):
            return 'up'
        if check('wall', x, y - 1) and not check('wall', x + 1, y):
            return 'right'
        if check('wall', x, y + 1) or check('wall', x - 1, y + 1):
            return 'left'
        if check('wall', x + 1, y) or check('wall', x + 1, y + 1):
            return 'down'
        if check('wall', x - 1, y - 1):
            return 'up'
        if check('wall', x + 1, y - 1):
            return 'right'

    if check('level') == 4:
        if check('gold', x, y):
            return 'take'
        if check('wall', x - 1, y) and check('wall', x + 2, y) and check('wall', x - 1, y - 3):
            return 'right'

        if check('wall', x, y + 2) and check('wall', x, y - 3) and (check('gold', x + 4, y - 6) or check('gold', x + 4, y - 5)):
            return 'up'

        if check('wall', x, y - 1) and not check('wall', x + 1, y):
            return 'right'

        if check('wall', x + 1, y) and not check('wall', x, y + 1):
            return 'down'

        if (check('wall', x - 1, y) and not check('wall', x, y - 1)) or check('wall', x - 1, y - 1):
            return 'up'

        if check('wall', x, y + 1) or check('wall', x - 1, y + 1):
            return 'left'

        if check('wall', x + 1, y - 1):
            return 'right'

        if check('wall', x + 1, y + 1):
            return 'down'


