def generate_password(length: int) -> str:
    """
    generate password with given length
    """
    return ''


def encrypt_message(message: str) -> str:
    """
    TODO on lecture
    encrypt message
    """
    key = 2
    return ''.join(
        chr(num + key)
        for num in map(ord, message)
    )


def lucky_number(ticket: str) -> bool:
    """
    lucky number (tram ticket)
    667766 - is lucky (6 + 6 + 7 == 7 + 6 + 6)
    """
    return True


def fizz_buzz(num: int) -> str:
    """
    fizz buzz
    усли число, кратно трем, программа должна выводить слово «Fizz»,
    а вместо чисел, кратных пяти — слово «Buzz».
    Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
    в остальных случаях число как строку
    """
    return ''


def password_is_strong(password) -> bool:
    """
    is password is strong
    (has number, char, lowercase, uppercase, at least length is 10)
    """
    return True


def number_is_prime(num: int) -> bool:
    """
    number is prime
    """
    return True


def decrypt_message(message: str) -> str:
    """
    decrypt message
    """
    return ''


def volume_of_sphere(radius: float) -> float:
    """
    Volume of a Sphere
    round to 2 places
    """
    return 0.0


def days_diff(start_date: ..., end_date: ...) -> ...:
    """
    calculate number of days between two dates.
    """
    return


def prs(client_choice) -> bool:
    """
    paper rock scissors
    """
    return True


def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    """
    return ''


if __name__ == '__main__':
    assert encrypt_message('Dima') == 'Fkoc'
