import json
import sys
import random
import logging
from io import StringIO

file_name = "fc.txt"
log_filename = ""
dic_score = {}
in_memory_file = StringIO()
in_out = ""
logging.basicConfig(filename='log.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level='DEBUG')


def get_exc_info(fx_name, error, verbose):
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    if verbose:
        print("Function name: ", fx_name, " Error: ", error)
        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)


def file_exists(p_file_name):
    try:
        with open(p_file_name, 'r', encoding='utf-8'):
            return True
    except EOFError as eof_err:
        get_exc_info(file_exists.__name__, eof_err, False)
        return False
    except FileNotFoundError as file_not_found_err:
        get_exc_info(file_exists.__name__, file_not_found_err, False)
        return False


def create_file(p_file_name):
    try:
        with open(p_file_name, 'w', encoding='utf-8') as file:
            file.write('{}')
            return True
    except EOFError as err_eof:
        get_exc_info(create_file.__name__, err_eof, False)
        return False
    except FileNotFoundError as err_fnf:
        get_exc_info(create_file.__name__, err_fnf, False)
        return False


def read_content_file(p_file_name):
    try:
        with open(p_file_name, 'r', encoding='utf-8') as file:
            return file.readlines()[0]
    except EOFError as rcf_err:
        get_exc_info(read_content_file.__name__, rcf_err, False)
        return None
    except FileNotFoundError as rcf_fnf:
        get_exc_info(read_content_file.__name__, rcf_fnf, False)
        return None


def get_content_file():
    dic_card = {}
    if file_exists(file_name):
        try:
            dic_card = json.loads(read_content_file(file_name))
            if not dic_card:
                # Empty dic
                create_file(file_name)
        except Exception as gcf_err:
            get_exc_info(get_content_file.__name__, gcf_err, False)
    else:
        create_file(file_name)

    return dic_card


def replace_content_file(p_file_name, new_content):
    try:
        with open(p_file_name, 'w', encoding='utf-8') as file:
            file.write(str(new_content))
            return True
    except EOFError as rcf_err:
        get_exc_info(replace_content_file.__name__, rcf_err, False)
        return False
    except FileNotFoundError as rcf_err_fnf:
        get_exc_info(replace_content_file.__name__, rcf_err_fnf, False)
        return False


def exists_key_by_value(d, str_definition):
    val_list = list(d.values())
    position = None
    try:
        position = val_list.index(str_definition)
    except ValueError as ve_err:
        get_exc_info(exists_key_by_value.__name__, ve_err, False)
        return False
    else:
        return True


def add(d):
    print("The card:")
    logging.debug("The card:")

    while True:
        card = input()
        logging.debug(card)

        k = dict.fromkeys(d)
        if card in k:
            print(f'The card "{card}" already exists. Try again:')
            logging.debug(f'The card "{card}" already exists. Try again:')
            continue
        else:
            break

    print("The definition of the card:")
    logging.debug("The definition of the card:")

    while True:
        definition = input()
        logging.debug(definition)

        if exists_key_by_value(d, definition):
            print(f'The definition "{definition}" already exists. Try again:')
            logging.debug(f'The definition "{definition}" already exists. Try again:')
        else:
            d[card] = definition
            try:
                replace_content_file(file_name, d)
            except Exception as add_err:
                get_exc_info(add.__name__, add_err, False)
            else:
                print(f'The pair ("{card}":"{definition}") has been added.')
                logging.debug(f'The pair ("{card}":"{definition}") has been added.')
                return d


def remove(d):
    print("Which card?")
    logging.debug("Which card?")

    while True:
        card = input()
        logging.debug(card)
        try:
            del d[card]
        except KeyError:
            print(f'Can\'t remove "{card}": there is no such card.')
            logging.debug(f'Can\'t remove "{card}": there is no such card.')
            return d
        else:
            print("The card has been removed.")
            logging.debug("The card has been removed.")
            break

    try:
        replace_content_file(file_name, d)
    except Exception as r_err:
        get_exc_info(remove.__name__, r_err, False)
    else:
        return d


def load(d=None, import_file=None):  # import
    if import_file is None:
        print("File name*:")
        logging.debug("File name:")
        in_file_name = input()
        logging.debug(in_file_name)
    else:
        in_file_name = import_file
        logging.debug(in_file_name)

    if file_exists(in_file_name):
        content_file = None
        try:
            with open(in_file_name, "r") as f:
                content_file = f.readlines()

        except Exception as json_decode_error:
            get_exc_info(load.__name__, json_decode_error, False)
            return d
        else:
            try:
                content_file = content_file[0]
                import_dictionary = json.loads(content_file.replace("'", '"'))
                # print(import_dictionary, type(import_dictionary))  # remove?
            except Exception as json_loads_error:
                get_exc_info(load.__name__, json_loads_error, False)
                return d
            else:
                d.update(import_dictionary)
                if len(d) == 1:
                    print(f'{len(d)} card have been loaded.')
                    logging.debug(f'{len(d)} card have been loaded.')
                else:
                    print(f'{len(d)} cards have been loaded.')
                    logging.debug(f'{len(d)} cards have been loaded.')
                # len(dic_card.keys())
                # If you like to count unique words in the file, you could just use set and do like
                # len(set(open(dic_card).read().split()))
    else:
        print("File not found.")
        logging.debug("File not found.")

    return d


def save(d, ex_file=None):  # export : write
    if ex_file is None:
        print('File name:')
        logging.debug('File name:')
        export_file = input()
        logging.debug(export_file)
    else:
        export_file = ex_file
        logging.debug(ex_file)  # remove???

    try:
        with open(export_file, 'w', encoding='utf-8') as file:
            file.write(str(d))
            if len(d) == 1:
                print(f'{len(d)} card have been saved.')
                logging.debug(f'{len(d)} card have been saved.')
            else:
                print(f'{len(d)} cards have been saved.')
                logging.debug(f'{len(d)} cards have been saved.')

            print("TEST LINE. EXPORT =", export_file, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")
            try:
                with open(export_file, 'r') as file:
                    lines = file.readlines()
                    print("Lines = ", len(lines))
                    for line in lines:
                        print(line[0])
            except EOFError as ex_eof_error:
                print(ex_eof_error)
                get_exc_info(save.__name__, ex_eof_error, True)
            print(" < < < < < < < < < < < < < < < < < < < < < < < < < < TEST LINE. EXport file =", export_file, "\n")

            return True

    except EOFError as e_err:
        get_exc_info(save.__name__, e_err, True)
        return False
    except FileNotFoundError as e_fnf_err:
        get_exc_info(save.__name__, e_fnf_err, True)
        return False


def get_key_by_value(dic, str_definition):
    # list out keys and values separately
    key_list = list(dic.keys())
    val_list = list(dic.values())

    try:
        position = val_list.index(str_definition)
        return key_list[position]
    except ValueError:
        return None


def get_rdn_range(start_inclusive, end_inclusive):
    return random.randint(start_inclusive, end_inclusive)


def has_key(d, k):
    # verify if the key exist
    has = False
    if k in dic_score:
        has = True
        # print(f"The key {k} exists")
    else:
        has = False
        # print(f"Does not contain the key: {k} ")

    return has


def score(the_dic, the_key):
    if has_key(the_dic, the_key):
        # print("Increment score")
        dic_score[the_key] = dic_score[the_key] + 1
    else:
        # print("Add key")
        dic_score[the_key] = 1


def ask(cards):
    print('How many times to ask?')
    logging.debug('How many times to ask?')

    times = int(input())
    logging.debug(times)

    vals = cards.values()
    for idx in range(0, times):
        k_idx = get_rdn_range(0, len(cards) - 1)

        c = list(cards)[k_idx]
        r = list(vals)[k_idx]

        # print(f'{count} Print the definition of "{c}":')
        print(f'Print the definition of "{c}":')
        logging.debug(f'Print the definition of "{c}":')

        answer = input()
        logging.debug(answer)

        if answer == r:  # answer == cards[c]:
            print("Correct!")
            logging.debug("Correct!")
        else:
            other_term = get_key_by_value(cards, answer)
            if other_term is not None:
                print(f'Wrong. The right answer is "{cards[c]}", but your definition is correct for "{other_term}".')
                logging.debug(
                    f'Wrong. The right answer is "{cards[c]}", but your definition is correct for "{other_term}".')
            else:
                print(f'Wrong. The right answer is "{cards[c]}".')
                logging.debug(f'Wrong. The right answer is "{cards[c]}".')

            # Score
            score(cards, c)


def view_log():
    with open('log.log', 'r') as reader:
        print(reader.read())


def show(d):
    print(d)
    print(dic_score)
    # view_log()


def erase_log_content(the_file):
    with open(the_file, 'w') as f:
        pass


def write_logging(msg):
    logging.basicConfig(filename=log_filename,
                        filemode='a',
                        format='%(message)s',
                        level='DEBUG')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_format = '%(asctime)s | %(levelname)s: %(message)s'
    console_handler.setFormatter(logging.Formatter(log_format))
    # start the logging and show the messages
    logger.info(msg)


def write_log_content(the_file, the_content):
    with open(the_file, 'w') as f:
        f.write(the_content)


def read_in_mem_file():
    print(in_memory_file.read())


def write_in_mem_file(txt):
    in_memory_file.write(txt + "\n")
    return ""


def get_in_mem_content():
    return in_memory_file.getvalue()


def log():
    global log_filename
    print("File name:")
    logging.debug("File name:")

    log_filename = str(input())
    logging.debug(log_filename)

    log_content = ""
    with open('log.log', 'r') as reader:
        log_content = reader.read()

    with open(log_filename, 'w') as writer:
        writer.write(log_content)

    # erase_log_content(log_filename)
    # write_logging(log_content)
    print("The log has been saved.")
    logging.debug("The log has been saved.")


def hardest_card(the_dic):
    # get max score

    if the_dic == {}:
        print("There are no cards with errors.")
        return

    try:
        max_hardest_card = max(the_dic.values())
    except ValueError as ex_hc:
        get_exc_info(file_exists.__name__, ex_hc, False)

    if max_hardest_card == 0:
        print("There are no cards with errors.")
        logging.debug("There are no cards with errors.")

    else:
        iteration = 0
        one_message = ""
        msg_part_1 = f'The hardest cards are '

        message = ""
        msg_part_3 = f'. You have {max_hardest_card} errors answering them.'

        for key, value in the_dic.items():
            if value == max_hardest_card:
                message = message + f'"{key}", '
                iteration = iteration + 1

        # remove comma
        message = message[:-2]
        if iteration == 1:
            message = f'The hardest card is {message}. You have {max_hardest_card} errors answering it.'
        else:
            message = msg_part_1 + message + msg_part_3

        print(message)
        logging.debug(message)
        # return message


def reset_dic_values(the_dic):
    # the_dic.clear()
    for k in dic_score:
        dic_score[k] = 0


def reset_stats(the_dic):
    try:
        reset_dic_values(the_dic)
    except Exception as e_reset_stats:
        get_exc_info(save.__name__, e_reset_stats, False)
        return False
    else:
        print("Card statistics have been reset.")


def load_data():
    return {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
    }


def load_score(num_errors):
    if num_errors == 1:
        return {
            "1": 0,
            "2": 0,
            "3": 5,
            "4": 0,
            "5": 0,
        }

    if num_errors == 2:
        return {
            "1": 10,
            "2": 0,
            "3": 5,
            "4": 0,
            "5": 10,
        }

    if num_errors == 3:
        return {
            "1": 0,
            "2": 3,
            "3": 0,
            "4": 2,
            "5": 1,
        }


def get_file_name(idx):
    opt = sys.argv[idx]
    equal = opt.find("=") + 1
    return opt[equal:]


def read_args(d, cfg=None):
    arg_limit = 2
    first_file = 1
    second_file = 2

    if len(sys.argv) == arg_limit:
        arg_idx_1 = 1
        if "--import" in sys.argv[arg_idx_1]:  # I M P O R T
            import_f_name = get_file_name(first_file)

            print("TEST LINE. IMport file =", import_f_name, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")
            try:
                with open(import_f_name, 'r') as file:
                    lines = file.readlines()
                    print("Lines = ", len(lines))
                    for line in lines:
                        print(line)
            except EOFError as ex_eof_error:
                get_exc_info(save.__name__, ex_eof_error, False)
            print(" < < < < < < < < < < < < < < < < < < < < < < < < < < TEST LINE. IMport file =", import_f_name, "\n")

            d = load(d, import_f_name)

            return d

        if "--export" in sys.argv[arg_idx_1]:  # E X P O R T
            # if cfg == "init":
            #     return d

            export_f_name = get_file_name(first_file)

            print("TEST LINE. EXPORT =", export_f_name, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")

            save(d, export_f_name)

            return d

    elif len(sys.argv) > arg_limit:
        arg_idx_2 = 2
        if "--export" in sys.argv[arg_idx_2]:  # Import and export

            import_f_name = get_file_name(first_file)

            print("TEST LINE. 1-IM-EX-IM file =", import_f_name, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")
            try:
                with open(import_f_name, 'r') as file:
                    lines = file.readlines()
                    print("Lines = ", len(lines))
                    for line in lines:
                        print(line)
            except EOFError as ex_eof_error:
                get_exc_info(save.__name__, ex_eof_error, False)
            print(" < < < < < < < < < < < < < < < < < < < < < < < < < < TEST LINE. 1-IM-EX file =", import_f_name, "\n")

            d = load(d, import_f_name)

            export_f_name = get_file_name(second_file)

            print("TEST LINE. 2-IM-EX file =", export_f_name, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")
            try:
                with open(export_f_name, 'r') as file:
                    lines = file.readlines()
                    print("Lines = ", len(lines))
                    for line in lines:
                        print(line)
            except EOFError as ex_eof_error:
                get_exc_info(save.__name__, ex_eof_error, False)
            print(" < < < < < < < < < < < < < < < < < < < < < < < < < < TEST LINE. 2-IM-EX file =", export_f_name, "\n")

            save(d, export_f_name)

            return d

        if "--import" in sys.argv[arg_idx_2]:  # Export and import

            export_f_name = get_file_name(first_file)

            if d == {}:  # empty dict
                # or load dummy_file
                d = {'Texas': 'Austin', 'Florida': 'Tallahassee', 'California': 'Sacramento'}

            save(d, export_f_name)

            import_f_name = get_file_name(second_file)

            print("TEST LINE. B-EX-IM file =", import_f_name, "\n > > > > > > > > > > > > > > > > > > > > > > > > > > >")
            try:
                with open(import_f_name, 'r') as file:
                    lines = file.readlines()
                    print("Lines = ", len(lines))
                    for line in lines:
                        print(line)
            except EOFError as ex_eof_error:
                get_exc_info(save.__name__, ex_eof_error, False)
            print(" < < < < < < < < < < < < < < < < < < < < < < < < < < TEST LINE. B-EX-IM file =", import_f_name, "\n")

            d = load(d, import_f_name)

            return d

    else:
        # print("no args")
        return 0


def start():
    global dic_score
    global in_out
    flashcard = {}
    logging.debug(sys.argv)

    if len(sys.argv) == 1:
        # If such an argument is not provided,
        #       the set of cards should initially be empty and no message about card loading should be output.
        #
        # not flashcard:  # d == {}    Empty dictionary
        # flashcard = load(flashcard, "fc.txt")
        flashcard = {}

    if len(sys.argv) > 1:
        # Arguments provided
        flashcard = read_args(flashcard, "init")

    print("TEST LINE. Memory flashcard =", flashcard, "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    while True:
        print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
        logging.debug("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")

        option = input()
        logging.debug(option)

        if option == "add":
            add(flashcard)

        elif option == "remove":
            remove(flashcard)

        elif option == "import":  # read
            flashcard = load(flashcard)

        elif option == "export":  # write
            save(flashcard)

        elif option == "ask":
            ask(flashcard)

        elif option == "load":
            flashcard = load_data()
            dic_score = flashcard
            reset_stats(dic_score)
        elif len(option) == 1:
            dic_score = load_score(int(option))
        elif option == "show":
            show(flashcard)

        elif option == "exit":
            if len(sys.argv) > 1:
                # Arguments provided
                read_args(flashcard)

            print("Bye bye!")
            logging.debug("Bye bye!")
            exit(0)

        elif option == "log":
            log()

        elif option == "log":
            log()

        elif option == "hardest card":
            try:
                hardest_card(dic_score)
            except Exception as e_hardest:
                get_exc_info(save.__name__, e_hardest, False)
        elif option == "reset stats":
            reset_stats(dic_score)
        else:
            continue
        print()


if __name__ == '__main__':
    try:
        start()
    except Exception as main_err:
        get_exc_info(__name__, main_err, False)
