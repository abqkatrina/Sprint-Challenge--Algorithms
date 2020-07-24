'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if word has fewer than two characters, it can't hold 'th'
    if len(word) < 2:
        return 0
    #if the first two characters are 'th', add 1 to count, move on (recursive)
    if word[0:2] == 'th':
        return 1 + count_th(word[1:])
    #if the first two characters aren't 'th', don't add 1, move on (recursive)
    else:
        return 0 + count_th(word[1:])
