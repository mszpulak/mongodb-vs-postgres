import random
import string


def generate_random_text(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))
