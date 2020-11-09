
import random

ANSWERS = (
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    )


def ask_question():
    return input("Ask the almighty eightball a question (ENTER to quit): ")


def give_answer():
    #answer = random.randrange(len(ANSWERS))
    #answer = random.randint(0,len(ANSWERS)-1)
    return random.choice(ANSWERS)


# if this returns True, keep asking questions
# if this returns False, end the program
def the_magic_eight_ball():
    # user asks the eight ball a question
    if len(ask_question()) == 0:
        return False

    # reply with random answer
    print(give_answer())
    return True


# loop until user is done
while the_magic_eight_ball():
    pass
