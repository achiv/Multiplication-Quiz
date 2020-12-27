import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(2,15)
    num2 = random.randint(2,9)

    prompt = '#%s: %s x %s = ' %(questionNumber+1, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)], blockRegexes = ['.*'], timeout=5, limit=2)

    except pyip.TimeoutException:
        print('Out of time!\nCorrect Answer is %s' %(num1 * num2))
    except pyip.RetryLimitException:
        print('Out of tries!\nCorrect Answer is %s' %(num1 * num2))
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

    time.sleep(2)   # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
