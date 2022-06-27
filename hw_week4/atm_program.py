# TASK 2

# store money ascii art as a raw text to give to user (adapted from: https://ascii.co.uk/art/money)
money = r'''
--------------------------------------------------------------------.
| .--                                                            .-- |
| |_       ......           BANK OF ENGLAND                      |_  |
| __)    ``````````             ______            B93810455B     __) |
|      2        ___            /      \                     2        |
|              /|~\\          /  _-\\  \           __ _ _ _  __      |
|             | |-< |        |  //   \  |         |_  | | | |_       |
|              \|_//         | |-  o o| |         |   | `.' |__      |
|               ~~~          | |\   b.' |                            |
|       B83910455B           |  \ '~~|  |                            |
| .--  2                      \_/ ```__/    ....            2    .-- |
| |_        ///// ///// ////   \__\'`\/      ``  //// / ////     |_  |
| __)                        FIVE  POUNDS                        __) |
`--------------------------------------------------------------------'
'''

moneys = r'''
  .-------------------------------------------------------------------.
.-------------------------------------------------------------------. |
| .--                                                            .-- ||
| |_       ......           BANK OF ENGLAND                      |_  || 
| __)    ``````````             ______            B93810455B     __) ||
|      2        ___            /      \                     2        ||
|              /|~\\          /  _-\\  \           __ _ _ _  __      ||
|             | |-< |        |  //   \  |         |_  | | | |_       ||
|              \|_//         | |-  o o| |         |   | `.' |__      ||
|               ~~~          | |\   b.' |                            ||
|       B83910455B           |  \ '~~|  |                            ||
| .--  2                      \_/ ```__/    ....            2    .-- ||
| |_        ///// ///// ////   \__\'`\/      ``  //// / ////     |_  ||
| __)                        FIVE  POUNDS                        __) |.
`--------------------------------------------------------------------'
'''

# set the correct pin
correct_pin = '1111'


# check if pin is 4 characters long; raise error if not
def validate_pin_length(string):
    if len(string) == 4:
        return string
    else:
        raise ValueError('PIN must be 4 digits.')


# check if pin contains digits only; raise error if not
def validate_pin_char(pin_number):
    if pin_number.isdigit():
        return pin_number
    else:
        raise TypeError('PIN must be digits only.')


# check if withdrawal amount is within balance; raise error if not
def validate_withdrawal_amount(amount):
    if 0 < int(amount) <= 100:
        return amount
    else:
        raise ValueError('Not a correct amount.')


# check if withdrawal amount is multiple of five; raise error if not
def validate_withdrawal_multiple(amount):
    if float(amount) % 5 == 0:
        return amount
    else:
        raise ValueError('Not a correct amount.')


# ask for PIN input; raise appropriate errors if incorrect; exit after 3rd invalid try
def pin_tries():
    for i in range(3):
        pin = input("Enter your 4 digit PIN: ")
        attempts = 2
        try:
            validate_pin_length(pin)
            validate_pin_char(pin)
        except ValueError:
            print('PIN must be 4 digits.')
        except TypeError:
            print('PIN must be digits only.')
        if pin == correct_pin:
            return pin
        else:
            attempts = attempts - i
            print(f'Wrong PIN. {attempts} attempts left.')
            if attempts == 0:
                print(f'Your account has been locked. Please contact your bank.')


# ask for withdrawal input; raise appropriate errors if incorrect; give user money if correct
def atm():
    if pin_tries():
        balance = 100
        print(f'Your balance is: {balance}')
        withdrawal = input('Enter the withdrawal amount. Currently we only have £5 notes. ''')
        try:
            validate_withdrawal_amount(withdrawal)
            validate_withdrawal_multiple(withdrawal)
            balance = balance - int(withdrawal)
            print(f'Your balance is now: {balance}')
            if withdrawal == '5':
                print('Please take your money.' + '\n' + money)
            else:
                print('Please take your money.' + '\n' + moneys)
        except ValueError:
            print('Not a correct amount.')
        finally:
            print('Need a loan? Call us on: 111-222-333.')


if __name__ == '__main__':
    atm()
