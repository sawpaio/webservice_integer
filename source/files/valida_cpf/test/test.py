###################### 20-08-2019
########### Lucas Sampaio de Melo
####### test.py
#### v1.0

import unittest
from source.validacpf_lucas import CPFvalidator

class Test(unittest.TestCase):
    
    def test_formation1(self):
        self.assertEqual(CPFvalidator.retira_formatacao('123.456.789-09'), '12345678909')

    def test_formation2(self):
        self.assertFalse(CPFvalidator.retira_formatacao('123.4567.89-09'))

    def test_formation3(self):
        self.assertFalse(CPFvalidator.retira_formatacao('123.J58.999-09'))

    def test_formation4(self):
        self.assertFalse(CPFvalidator.retira_formatacao('111.111.111-11'))
        
    def test_formation5(self):
        self.assertFalse(CPFvalidator.retira_formatacao('bom dia'))

    def test_validate1(self):
        self.assertFalse(CPFvalidator.valida_cpf('123.456.678-10'))
    
    def test_validate2(self):    
        self.assertTrue(CPFvalidator.valida_cpf('123.456.789-09'))

    def test_formation3(self):    
        self.assertFalse(CPFvalidator.valida_cpf('1234.56.789-10'))


if __name__ == '__main__':
    unittest.main()
