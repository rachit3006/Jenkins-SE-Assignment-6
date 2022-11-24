import unittest

from calculator import add,mul,sub,div

class TestSum(unittest.TestCase):
	def test_1(self):
		x = 10
		y = 20
		result = add(x, y)
		self.assertEqual(result, 30.0)
		
	def test_2(self):
		x = 10
		y = 20
		result = mul(x, y)
		self.assertEqual(result, 200.0)

	def test_3(self):
		x = 10
		y = 20
		result = sub(x, y)
		self.assertEqual(result, -10.0)

	def test_4(self):
		x = 10
		y = 20
		result = div(x, y)
		self.assertEqual(result, 0.5)

	def test_5(self):
		x = 10
		y = 0
		result = div(x, y)
		self.assertEqual(result, "Division by zero not possible !")

if __name__ == '__main__':
	unittest.main()