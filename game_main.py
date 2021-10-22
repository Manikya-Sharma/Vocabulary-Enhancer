from english_words import english_words_set
from nltk.corpus import wordnet
import random
import pygame
from exclude_word import is_excluded

pygame.init()  # INITIALIZE
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)
icon = pygame.image.load("Images/Icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Vocabulary Enhancer")

# Constants:-

running = True
invalid = False
l = list(english_words_set)

font = pygame.font.Font('freesansbold.ttf', 32)

with open('configure.txt', 'r') as file:
    data = file.read()
    _list = data.split('\n')
    for elem in _list:
        if 'bg_color' in elem:
            x = elem.split('=')
            bg_color = eval(x[1])
        elif 'q_color' in elem:
            x = elem.split('=')
            q_color = eval(x[1])
        elif 'options_color' in elem:
            x = elem.split('=')
            options_color = eval(x[1])
        elif 'difficulty' in elem:
            x = elem.split('=')
            difficulty = x[1]

q_x = 5
q_y = 50

op1_x = 200
op1_y = 300

op2_x = 700
op2_y = 300

op3_x = 200
op3_y = 500

op4_x = 700
op4_y = 500

difficulty = difficulty.strip()
if difficulty == "easy":
    num_ques = 10
    add_score = 10
    sub_score = 0
elif difficulty == "medium":
    num_ques = 12
    add_score = 10
    sub_score = 5
elif difficulty == "hard":
    num_ques = 20
    add_score = 5
    sub_score = 4
else:  # Default
    num_ques = 10
    add_score = 10
    sub_score = 0

x = 1

clicked = False
corr_option = None

points = 0
begin = True
ans = ''


# Functions
def show_ques():
    global ans
    while True:
        ans = random.choice(l)  # Word has been determined
        if is_excluded(ans):
            ans = random.choice(l)
        else:
            break
    synsets = wordnet.synsets(ans)
    invalid = True
    while invalid:
        if len(synsets) == 0:
            invalid = True
            means = ""
            ans = random.choice(l)  # Word has been determined
            synsets = wordnet.synsets(ans)
        else:
            invalid = False
            means = random.choice(synsets).definition()
            if len(means) > 60:
                synsets = []  # explicitly make its length zero
                invalid = True
                continue
            for word in means.split():
                if is_excluded(word):
                    synsets = []
                    invalid = True
                    break
            else:
                means = means.capitalize()
                means = means.strip()
                means = str(x) + '. ' + means
                means = means.center(100)
                synonyms = []
                for syn in synsets:
                    for lem in syn.lemmas():
                        synonyms.append(lem.name())
    valid_words = False
    while not valid_words:
        valid_words = True
        word1 = random.choice(l).capitalize()
        word2 = random.choice(l).capitalize()
        word3 = random.choice(l).capitalize()
        ans = ans.capitalize()
        t = (word1, word2, word3)
        if len(set(t)) < 3:
            valid_words = False
            continue
        for word in t:
            if word in synonyms:
                valid_words = False
                break
            if is_excluded(word):
                valid_words = False
    q_text = font.render(means, True, q_color)
    ans_text = font.render(ans, True, options_color)
    option1_text = font.render(word1, True, options_color)
    option2_text = font.render(word2, True, options_color)
    option3_text = font.render(word3, True, options_color)
    return q_text, ans_text, option1_text, option2_text, option3_text


def find_click(x, y):
    global clicked
    clicked = True
    if x in range(op1_x - 50, op1_x + 250):
        if y in range(op1_y - 50, op1_y + 100):
            return 0
        elif y in range(op3_y - 50, op3_y + 100):
            return 2
        else:
            clicked = False
    elif x in range(op2_x - 50, op2_x + 200):
        if y in range(op1_y - 50, op1_y + 100):
            return 1
        elif y in range(op3_y - 50, op3_y + 100):
            return 3
        else:
            clicked = False
    else:
        clicked = False


def show_over():
    over_text = font.render('GAME OVER', True, (255, 255, 255))
    score_text = font.render("Your Score: " + str(points), True, (255, 255, 255))
    screen.fill(bg_color)
    screen.blit(over_text, (475, 250))
    screen.blit(score_text, (460, 360))
    pygame.display.update()


# Renders and blit for initialization

q_text = font.render('', True, (255, 255, 255))
a = font.render('', True, (255, 255, 255))
b = font.render('', True, (255, 255, 255))
c = font.render('', True, (255, 255, 255))
d = font.render('', True, (255, 255, 255))

# Game loop
while running:
    screen.fill(bg_color)
    score = font.render("SCORE : " + str(points), True, (155, 155, 155))
    screen.blit(score, (1000, 550))
    if begin:
        text1 = font.render("Click On the Correct Option", True, (q_color))
        text2 = font.render("Correct answer gives %u points" % (add_score), True, (q_color))
        text3 = font.render("Wrong answer subtracts %u points" % (sub_score), True, (q_color))
        clicked = True
        screen.blit(text1, (400, 100))
        screen.blit(text2, (380, 200))
        screen.blit(text3, (360, 300))
        pygame.display.update()
        begin = False
    if invalid:
        invalid = False  # Will pass not render invalid text
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if clicked:
            q_text, a_text, op1_text, op2_text, op3_text = show_ques()
            lis = [a_text, op1_text, op2_text, op3_text]
            random.shuffle(lis)
            a, b, c, d = lis
            corr_option = (a, b, c, d).index(a_text)
            clicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepress = pygame.mouse.get_pressed()
            if mousepress[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                option = find_click(mouse_x, mouse_y)
                if option == corr_option:
                    points += add_score
                    for i in range(points - add_score, points + 1):
                        screen.fill(bg_color)
                        text = font.render('CORRECT ANSWER!', True, (255, 255, 255))
                        screen.blit(text, (450, 275))
                        p_text = font.render("SCORE : " + str(i), True, (255, 255, 255))
                        screen.blit(p_text, (525, 350))
                        pygame.display.update()
                        pygame.time.wait(100)
                    pygame.time.wait(100)
                    x += 1
                elif not clicked:
                    pass  # Not Clicked
                else:
                    points -= sub_score
                    for i in range(points + sub_score, points - 1, -1):
                        w_text = font.render("Wrong Answer", True, (255, 255, 255))
                        corr = font.render("CORRECT ANSWER : " + ans, True, (255, 255, 255))
                        screen.fill(bg_color)
                        screen.blit(w_text, (500, 300))
                        screen.blit(corr, (350, 350))
                        p_text = font.render("SCORE : " + str(i), True, (255, 255, 255))
                        screen.blit(p_text, (525, 400))
                        pygame.display.update()
                        pygame.time.wait(50)
                    pygame.time.wait(1000)
                    x += 1
                if x > num_ques:
                    show_over()
                    pygame.time.wait(1500)
                    running = False
    screen.blit(q_text, (q_x, q_y))
    screen.blit(a, (op1_x, op1_y))
    screen.blit(b, (op2_x, op2_y))
    screen.blit(c, (op3_x, op3_y))
    screen.blit(d, (op4_x, op4_y))
    pygame.display.update()

pygame.quit()
