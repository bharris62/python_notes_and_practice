# look up someone not in the phone book to be cleanly caught by the except block.

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

try:
    phone_book['Jamie Theakston']
except:
    print('sorry! not in the little black book')
