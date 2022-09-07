from functions.helper_functions import return_max


class TestString:
    def test_number_in_string(self):
        string = "grgr$64523424234#%$^%435fdfertert$%54545\\"
        print()
        print(f"Input: {string}")
        print(f"Max: {return_max(string)}")
