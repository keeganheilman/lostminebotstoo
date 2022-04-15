# MIT License

# Copyright (c) 2022 Molly White

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import re
from data.honeypot_data import *


def hydrate_template(template):
    words_needed = re.findall("{(.*?)}", template)
    chosen_words = {}
    for word in words_needed:
        chosen_words[word] = random.choice(WORDS[word])
    return template.format(**chosen_words)


def random_punct():
    return random.choice([".", "!", "!!", "!!!", "..."])


def write_honeypot_tweet():
    tweet_template = ""
    if random.random() < 0.8:
        tweet_template += random.choice(PREFIX) + " "
    tweet_template += random.choice(TEMPLATES) + random_punct()
    if random.random() < 0.8:
        tweet_template += " " + random.choice(SUFFIX)
        if not tweet_template.endswith("?"):
            tweet_template += random_punct()
    return hydrate_template(tweet_template)