import re
from collections import defaultdict

# Print first 10 most frequent words in text.
text = """
In friendship diminution instrument so. Son sure paid door with say them. Two among sir sorry men court. Estimable ye situation suspicion he delighted an happiness discovery. Fact are size cold why had part. If believing or sweetness otherwise in we forfeited. Tolerably an unwilling arranging of determine. Beyond rather sooner so if up wishes or.

Departure so attention pronounce satisfied daughters am. But shy tedious pressed studied opinion entered windows off. Advantage dependent suspicion convinced provision him yet. Timed balls match at by rooms we. Fat not boy neat left had with past here call. Court nay merit few nor party learn. Why our year her eyes know even how. Mr immediate remaining conveying allowance do or.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and.
"""


if __name__ == "__main__":
    text_d = defaultdict(lambda: 0)
    print(text_d)

    # words = text.split(" ")
    words = re.split(" |\n|\\.", text)
    words = list(map(lambda w: w.strip().lower(), words))
    print(words)
    for w in words:
        if w != "":
            text_d[w] += 1
    print(text_d)

    r = sorted(text_d.items(), key=lambda x: x[1], reverse=True)
    # r = list(map(lambda x: x[0], r))[:10]
    r = list(r)[:10]
    print(r)

