from collections import OrderedDict

class Roman_Convert:
    roman_dict = OrderedDict([
    (1000, 'M'),
    (500,  'D'),
    (100,  'C'),
    (50,   'L'),
    (10,   'X'),
    (5,    'V'),
    (1,    'I')
    ])

    def verify_number(number):
        """
        Verifica se o número está no intervalo 0 < number < 3999
        """
        number = int(number)
        return print(0 < number and number <= 3999)

if __name__ == "__main__":
    number = input("Digite um número para ser convertido: \n")
    Roman_Convert.verify_number(number)