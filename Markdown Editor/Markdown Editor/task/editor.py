# import markdown
# output = markdown. markdown('''#John Lennon
# or *John Winston Ono Lennon* was one of *The Beatles*.
# Here are the songs he wrote I like the most:
# - Imagine
# - Norwegian Wood
# - Come Together
# - In My Life
# - ~~Hey Jude~~ (that was McCartney)''')
# print(output)

# 0. Implement a separate function for each of the formatters
# 1. Ask a user to input a formatter.
# 2. If the formatter doesn't exist,
#       print the following error message: Unknown formatting type or command
# 3. Ask a user to input a text that will be applied to the formatter: Text: <user's input>.
# 4. Save the text with the chosen formatter applied to it and print the markdown.
#       Each time you should print out the whole text in markdown accumulated so far.
# * Different formatters may require different inputs.
# * The new-line formatter does not require text input.

formatter = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
special_cmd = ["!help", "!done"]


def plain(text):
    return text


def bold(text):
    return "**" + text + "**"


def italic(text):
    return f"*{text}*"


def header(level, text):
    pound = "#" * int(level)
    return f"{pound} {text}\n"


def link(lbl, lnk):
    return f"[{lbl}]({lnk})"


def inline_code(text):
    return f"`{text}`"


def read_input_lst():
    error_lst = "The number of rows should be greater than zero"
    while True:
        try:
            n_rows = int(input("Number of rows:"))
            if n_rows <= 0:
                print(error_lst)
                continue
            else:
                return n_rows

        except ValueError:
            return False
        except Exception as ex_read_in_lst:
            print(f"Input error {ex_read_in_lst}")


def ftm_rows(lst_type, lst_rows):
    try:
        items = []
        for i in range(1, lst_rows + 1):
            items.append(input(f"Row #{i}: "))

        text = ""
        if lst_type == "unordered-list":
            for i in range(0, len(items)):
                text += f"* {items[i]}\n"

        else:  # ordered-list
            for i in range(0, len(items)):
                text += f"{i + 1}. {items[i]}\n"

        return text

    except ValueError:
        return False
    except Exception as ex_ftm_rows:
        print(f"Input error {ex_ftm_rows}")


def new_line(text):
    return text + "\n"


def val_in():
    try:
        return input("Text:")
    except ValueError:
        return False
    except Exception as val_in_ex:
        print(f"Input error {val_in_ex}")


def val_level_in():
    while True:
        try:
            lvl = int(input("Level:"))
            if 1 <= lvl <= 6:  # if level >= 1 and level <= 6:
                txt_lvl = input("Text:")
                return header(lvl, txt_lvl)
            else:
                print("The level should be within the range of 1 to 6")
                continue
        except ValueError:
            return False
        except Exception as val_in_ex:
            print(f"Input error {val_in_ex}")


def save_results(content):
    try:
        with open('output.md', 'w') as md_file:
            md_file.write(content)
    except EOFError:
        pass
    finally:
        pass

def main():
    users_txt = ""
    while True:
        fmt = input("Choose a formatter:")
        if fmt not in formatter:
            if fmt == "!help":
                print("Available formatters:", " ".join(formatter), "\nSpecial commands:", " ".join(special_cmd))
            elif fmt == "!done":
                save_results(users_txt)
                break
            else:
                print("Unknown formatting type or command")
            continue
        else:
            if fmt == "plain":
                txt = val_in()
                users_txt += plain(txt)
            elif fmt == "bold":
                txt = input("Text:")
                users_txt += bold(txt)
            elif fmt == "italic":
                txt = input("Text:")
                users_txt += italic(txt)
            elif fmt == "header":
                users_txt += val_level_in()
            elif fmt == "link":
                label = input("Label:")
                url = input("URL:")
                users_txt += link(label, url)
            elif fmt == "inline-code":
                txt = input("Text:")
                users_txt += inline_code(txt)
            elif fmt == "new-line":
                users_txt = new_line(users_txt)

            elif fmt == "ordered-list" or fmt == "unordered-list":
                rows = read_input_lst()
                users_txt += ftm_rows(fmt, rows)

        print(users_txt)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
