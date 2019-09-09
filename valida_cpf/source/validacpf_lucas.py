###################### 20-08-2019
########### Lucas Sampaio de Melo
####### validacpf_lucas.py
#### v1.0

import re
import os

class CPFvalidator:

    @classmethod
    def retira_formatacao(cls, num_cpf):
        ### Regex que verifica se o CPF digitado está no formato correto.
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', num_cpf):
            return 'Digite um CPF válido, no formato XXX.XXX.XXX-XX'

        else:
            cpf_formatado = num_cpf.replace(".", "").replace("-", "")
            
            if len(cpf_formatado) != 11 or len(set(list(cpf_formatado))) == 1:
                return False
            else:
                return cpf_formatado



    @classmethod
    def valida_cpf(cls, num_cpf):
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', num_cpf):
            return 'Digite um CPF válido, no formato XXX.XXX.XXX-XX'
        
        cpf_formatado = [int(digit) for digit in num_cpf if digit.isdigit()]

        validacao = sum(v1*v2 for v1, v2 in zip(cpf_formatado[0:9], range(10, 1, -1)))
        resto = (validacao * 10 % 11) % 10
        if cpf_formatado[9] != resto:
            return False
        else:
            validacao = sum(v3*v4 for v3, v4 in zip(cpf_formatado[0:10], range(11, 1, -1)))
            resto = (validacao * 10 % 11) % 10
            if cpf_formatado[10] != resto:
                return False
            else:
                return True

if __name__ == "__main__":
    while True:
        try:    
            objetivo = input("Deseja formatar ou validar o CPF? \n f = formatar \n v = validar\n Digite sua resposta:")
            
            if len(objetivo) > 1:
                os.system("clear")
                print("Digite apenas 'f' = formatar ou 'v' = validar.")
                objetivo = input("Digite sua resposta: ")

            os.system("clear")
            num_cpf = input("Digite um CPF válido, no formato XXX.XXX.XXX-XX\n")
            
            if objetivo == 'f':
                CPFvalidator.retira_formatacao(num_cpf)
            if objetivo == 'v':
                CPFvalidator.valida_cpf(num_cpf)

        except KeyboardInterrupt:
            exit(0)
