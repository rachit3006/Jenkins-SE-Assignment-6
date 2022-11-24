import unittest

from calculator import div,sqrt

class TestSum(unittest.TestCase):
  def test_1(self):
		x = 10
		y = 0
		result = div(x, y)
		self.assertEqual(result, "Error ! Division by 0 not possible")

	def test_5(self):
		x = -10
		result = sqrt(x)
		self.assertEqual(result, "Error ! Square root of negative numbers not possible")

if __name__ == '__main__':
	unittest.main()
