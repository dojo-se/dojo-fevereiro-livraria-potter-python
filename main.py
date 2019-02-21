# coding=utf8

import unittest
import random
import re


def testarNumeros(livros):
    valor = 42         
    return quantidade_livros(livros) * valor
    
def quantidade_livros(livros):
    quantidade = 0
    for livro in livros:
        quantidade += livro['quantidade']          
    return quantidade
    
def quantidade_livros_distintos(livros):
    livros_distintos = {}

    for livro in livros:
        livros_distintos[livro['nome']] = 1

    quantidade = 0
    for chave, valor in livros_distintos.items():
        quantidade += 1
    return quantidade

def aplicar_porcentagem(livros):
    val = 0.0
    for livro in livros:
        val += livro['quantidade'] * 42
        
    livros_distintos = quantidade_livros_distintos(livros)
    porcentagens = {
        "1": 0,
        "2": 0.05,
        "3": 0.10,
        "4": 0.15,
        "5": 0.20
    }

    return porcentagens[str(livros_distintos)] * val
    

               
  


############# CLASSE DE TESTE ###############
class LivrariaHarryPotterTest(unittest.TestCase):
    livros = [
        {'nome': 'Livro 1', 'quantidade': 1},
        {'nome': 'Livro 2', 'quantidade': 1},
        {'nome': 'Livro 3', 'quantidade': 1},
        {'nome': 'Livro 4', 'quantidade': 1},
        {'nome': 'Livro 5', 'quantidade': 1},
        {'nome': 'Livro 6', 'quantidade': 1},
        {'nome': 'Livro 7', 'quantidade': 1}
    ]
    #def teste(self):
    #    self.assertEqual(0, testarNumeros(self.livros))

    #def teste2(self):
    #    self.assertEqual(42, testarNumeros(self.livros))

    def test_quantidade_livros(self):
        self.assertEqual(7, quantidade_livros(self.livros))

    def test_quantidade_livros_distintos(self):
        self.assertEqual(1, quantidade_livros_distintos([
            {'nome': 'Livro 1', 'quantidade': 1},
            {'nome': 'Livro 1', 'quantidade': 1}
        ]))

    def test_valor_livros(self):
        self.assertEqual(7*42, testarNumeros(self.livros))

    def test_aplica_porcentagem(self):
        self.assertEqual(4.2, aplicar_porcentagem([
            {'nome': 'Livro 1', 'quantidade': 1},
            {'nome': 'Livro 2', 'quantidade': 1}
        ]))

    #def testar_soma_sem_desconto(84, testarNumeros(livros))


if __name__ == '__main__':
    unittest.main()