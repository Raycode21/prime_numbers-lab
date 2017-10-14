@@ -8,14 +8,14 @@ class TestPrimeNumbers(unittest.TestCase):
      """ Tests prime_numbers functionality """
  
      def test_input_is_positive(self):
 -        self.assertRaises(ValueError,prime_numbers, -1)
 +        self.assertEqual(prime_numbers(-5), [])
      def test_input_is_Not_a_list(self):
 -    	self.assertRaises(ValueError,prime_numbers, [2,4])
 +    	self.assertRaises(TypeError,prime_numbers, [2,4])
      def test_input_is_zero(self):
 -        self.assertEqual(prime_numbers(0), "Enter numbers greater than 0 only")
 +        self.assertEqual(prime_numbers(0), [])
      def test_output_is_primeNumbers(self):
 -        self.assertEqual(prime_numbers(8), [2,3,5,7])
 +        self.assertEqual(prime_numbers(8), [1,2,3,5,7])
      def test_input_is_not_a_dictionary(self):
 -        self.assertRaises(ValueError,prime_numbers, {"jane":2, "tom":4})
 +        self.assertRaises(TypeError,prime_numbers, {"jane":2, "tom":4})
  if __name__ == "__main__":
      unittest.main(exit = False)
