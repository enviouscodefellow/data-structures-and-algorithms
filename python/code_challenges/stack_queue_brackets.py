from data_structures.queue import Queue


def multi_bracket_validation(string):
    stack = []
    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack
