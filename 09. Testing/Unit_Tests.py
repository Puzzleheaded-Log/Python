""" Exercise 1: Reverse string. """

def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    text = input("Enter text: ")
    print(reverse_text(text))


#Testing the function
def test_normal_text():
    assert reverse_text("relu") == "uler"

def test_empty_text():
    assert reverse_text("") == ""

def test_text_with_spaces():
    assert reverse_text("relu nebunu") == "unuben uler"

def test_single_character():
    assert reverse_text("r") == "r"
