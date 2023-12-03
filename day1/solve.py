import re

with open("codes.txt", "r") as f:
    ls = f.read().split("\n")

ns = [n for l in ls for n in [re.findall(r"[0-9]", l)]]
# print(sum(int(n[0] + n[-1]) for n in ns))

v = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
ns = [
    n
    for l in ls
    for n in [
        re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", l)
    ]
]

# replace text with number, if it is text, otherwise it is the number already
print(sum(int(v.get(n[0], n[0]) + v.get(n[-1], n[-1])) for n in ns))
