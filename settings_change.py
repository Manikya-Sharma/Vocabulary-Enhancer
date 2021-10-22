def defaults():
    # bg_color = (0,0,0)
    # q_color = (155,155,255)
    # options_color = (255,155,255)
    # difficulty = easy
    with open("configure.txt", "w") as file:
        file.write("bg_color = (0,0,0)\n")
        file.write("q_color = (155,155,255)\n")
        file.write("options_color = (255,155,255)\n")
        file.write("difficulty = easy")


def change_bg_color(new_color):
    new_color = str(new_color)
    st = ''
    for i in new_color:
        if not i.isspace():
            st += i
    new_color = st
    with open("configure.txt", 'r+') as file:
        data = file.read()
        words = data.split()
        for word in words:
            if 'bg_color' in word:
                ind = words.index(word)
                words[ind + 2] = new_color
        new_st = ''
        i = 1
        for word in words:
            if '_color' in word or 'difficulty' in word:
                i = -2
            if i == 0:
                new_st += word + '\n'
                i = 1
            else:
                new_st += word + ' '
            i += 1
        file.seek(0)
        file.write(new_st)


def change_q_color(new_color):
    new_color = str(new_color)
    st = ''
    for i in new_color:
        if not i.isspace():
            st += i
    new_color = st
    with open("configure.txt", 'r+') as file:
        data = file.read()
        words = data.split()
        for word in words:
            if 'q_color' in word:
                ind = words.index(word)
                words[ind + 2] = str(new_color)
        new_st = ''
        i = 1
        for word in words:
            if '_color' in word or 'difficulty' in word:
                i = -2
            if i == 0:
                new_st += word + '\n'
                i = 1
            else:
                new_st += word + ' '
            i += 1
        file.seek(0)
        file.write(new_st)


def change_options_color(new_color):
    new_color = str(new_color)
    st = ''
    for i in new_color:
        if not i.isspace():
            st += i
    new_color = st
    with open("configure.txt", 'r+') as file:
        data = file.read()
        words = data.split()
        for word in words:
            if 'options_color' in word:
                ind = words.index(word)
                words[ind + 2] = str(new_color)
        new_st = ''
        i = 1
        for word in words:
            if '_color' in word or 'difficulty' in word:
                i = -2
            if i == 0:
                new_st += word + '\n'
                i = 1
            else:
                new_st += word + ' '
            i += 1
        file.seek(0)
        file.write(new_st)


def change_difficulty(new_diff):
    with open("configure.txt", 'r+') as file:
        data = file.read()
        words = data.split()
        new_st = ''
        for word in words:
            if 'difficulty' in word:
                ind = words.index(word)
                words[ind + 2] = str(new_diff)
        new_st = ''
        i = 1
        for word in words:
            if '_color' in word or 'difficulty' in word:
                i = -2
            if i == 0:
                new_st += word + '\n'
                i = 1
            else:
                new_st += word + ' '
            i += 1
        file.seek(0)
        file.write(new_st)
        file.seek(0)
        file.write(new_st)
