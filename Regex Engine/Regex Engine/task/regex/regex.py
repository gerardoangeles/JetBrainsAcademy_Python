def match(in_put):
    """An empty regex should always return True.
    An empty input string should always return False, except if the regex is also empty.
    An empty regex against an empty string always returns True.
    Accept two characters, a regex and an input;
    Compare the regex to the input and return a boolean indicating if there's a match;
    Support . as a wild card character that matches any input;
    Follow the special syntax rules outlined above."""
    pipe_sep = "|"
    dot_sep = "."
    empty_string = ""
    reg_exp = list(in_put)
    if reg_exp:
        if pipe_sep in reg_exp:
            if len(reg_exp) == 1:
                if reg_exp[0] == pipe_sep:
                    return True
                else:
                    return False
            elif len(reg_exp) == 2:
                if reg_exp[0] == pipe_sep and reg_exp[1] == empty_string:
                    return True
                elif reg_exp[0] == pipe_sep:
                    return True
                elif reg_exp[1] == pipe_sep:
                    if reg_exp[0] == empty_string:
                        return True
                    else:
                        return False
                else:
                    return False
            elif len(reg_exp) == 3:
                if reg_exp[1] == pipe_sep:
                    if reg_exp[0] == dot_sep:
                        return True
                    if reg_exp[0] == reg_exp[2]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    print(match(input()))
