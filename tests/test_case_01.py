import unittest
import dataset_generator


class MyTestCase(unittest.TestCase):
    def test_hex_to_color(self):
        test_data = ['#9dac80', '#c8247a', '#2835ea', '#267f92']
        test_answer = [(157, 172, 128), (200, 36, 122), (40, 53, 234), (38, 127, 146)]
        for hex_data, rgb_data in zip(test_data, test_answer):
            self.assertEqual(dataset_generator.hex_to_rgb(hex_data), rgb_data)

    def test_color_generator(self):
        print(dataset_generator.generate_colors())
        print(dataset_generator.generate_colors_2())


if __name__ == '__main__':
    unittest.main()
