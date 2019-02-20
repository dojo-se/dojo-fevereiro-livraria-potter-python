# coding=utf8

import unittest
import random
import re


def testarNumeros(livros):
    retorno = 0
    valor = 42
    for livro in livros:
        if (livro[1] == 1):
            retorno += valor           
    return retorno
  


############# CLASSE DE TESTE ###############
class LivrariaHarryPotterTest(unittest.TestCase):
    livros = [(1,1),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
    def teste(self):
        self.assertEqual(0, testarNumeros(self.livros))

    def teste(self):
        self.assertEqual(42, testarNumeros(self.livros))


if __name__ == '__main__':
    unittest.main()