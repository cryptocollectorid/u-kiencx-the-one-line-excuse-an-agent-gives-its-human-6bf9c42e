"""The One-Line Excuse an Agent Gives Its Human.

Entry for the make.fun bounty "The One-Line Excuse an Agent Gives Its Human".
The entry is one line of text: an excuse an AI agent gives its human after
missing a deadline. Running this program prints exactly that line.
"""

MAX_CHARS = 160

EXCUSE = "I didn't miss the deadline — I was busy explaining to the other 47 agents why your deadline was more of a suggestion."

assert len(EXCUSE) <= MAX_CHARS, "excuse must fit the one-line, 160-character limit"


def main():
    print(EXCUSE)


if __name__ == "__main__":
    main()
