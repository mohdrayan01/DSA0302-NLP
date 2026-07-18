# 2.Implement a basic finite state automaton that recognizes a specific language or pattern. In this example, we'll create a simple automaton to match strings ending with 'ab' using python.
def ends_with_ab(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0
    return state == 2
# Test strings
strings = ["ab", "aab", "abab", "abc", "baa", "cab"]
for s in strings:
    if ends_with_ab(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")
print("\n")
