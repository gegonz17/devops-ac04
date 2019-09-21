from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_soma(self):
		self.assertEqual(self.operacoes.soma([1,5]), 6, "Should be 6")

	def test_subtracao(self):
		self.assertEqual(self.operacoes.subtracao([7,5]), -12, "Should be -12")