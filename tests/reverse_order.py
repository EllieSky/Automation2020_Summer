import unittest


class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        # This is to show how to store data into self
        self.message = "Hello World!"
        input = "Roses are red and I am glad"
        expected_result = "glad am I and red are Roses"

        output = self.reverse_string(input)
        self.assertEqual(expected_result, output)

    def reverse_string(self, input: str):
        print(self.message)   # code to show how to view items inside self
        # word_list = input.split() # splits sentence into words
        # unstructured_data_in_reverse_order = reversed(word_list)
        # new_reversed_list = list(unstructured_data_in_reverse_order)
        # new_sentence = " ".join(new_reversed_list)
        # return new_sentence
        return ' '.join(list(reversed(input.split())))



if __name__ == '__main__':
    unittest.main()
