import random


# Exception messages
exc_msg_001_invalid_input = 'No one is joining for the party'
# Business rule
condition_not_less_than_or_eq = 0


def get_n_decimals(q, d):
    return round(q, d)


def check_user_input(some_input, msg=None):
    try:
        # Convert it into integer
        _ = int(some_input)
    except ValueError:
        try:
            # Convert it into float
            _ = float(some_input)
        except ValueError:
            if msg is not None:
                print(msg)
            exit()


def start():
    friends_input = input('Enter the number of friends joining (including you):\n')

    check_user_input(friends_input, exc_msg_001_invalid_input)

    friends_number = int(friends_input)

    try:
        # assert not friends_number <= condition_not_less_than_or_eq, exc_msg_001_invalid_input
        assert not friends_number <= condition_not_less_than_or_eq, exc_msg_001_invalid_input
    except AssertionError:
        # (previous stage) 1. If there are no people to split the bill
        # (the number of friends is: 0 or an invalid input), output "No one is joining for the party";
        # print(exc_msg_001_invalid_input)
        # 1. In case of an invalid number of people, "No one is joining for the party" is expected as an output;
        print(exc_msg_001_invalid_input)
        exit()

    friends_dict = {}
    print('Enter the name of every friend (including you), each on a new line:')

    for f in range(friends_number):
        friends_dict[input()] = 0.00

    # 3. take user input: the final bill;
    total_bill_input = input("Enter the total bill value:\n")
    total_bill_value = int(total_bill_input)

    # 2. Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
    is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    # 4. If a user wants to use the feature
    lucky_friend = None
    if is_lucky == "Yes":
        # Otherwise, if the user choice is Yes,
        # choose a name from the dictionary keys at random and print the following:
        lucky_friend = random.choice(list(friends_dict.keys()))
        print(lucky_friend + ' is the lucky one!\n')
        # 2. re-split the bill according to the feature;
        total_bill_equally_among = total_bill_value / (friends_number - 1)
    else:
        # 5. If the user enters anything else, print No one is going to be lucky.
        print("No one is going to be lucky\n")
        # ?. Split the total bill equally among everyone;
        total_bill_equally_among = total_bill_value / friends_number
        # 2. Split the total bill equally among everyone;
        # total_bill_equally_among = total_bill_value / friends_number

    # exit()  # cropped version stage (3)

    # 3. Round the split value to two decimal places;
    total_bill_equally_among = get_n_decimals(total_bill_equally_among, 2)

    # 4. Update the dictionary with new split values
    for k in friends_dict:
        if is_lucky == "Yes" and k == lucky_friend:
            # and 0 for the lucky person;
            friends_dict.update({k: 0.0})
        else:
            friends_dict.update({k: total_bill_equally_among})

    # 5. Print the updated dictionary.
    print(friends_dict)


if __name__ == '__main__':
    start()
