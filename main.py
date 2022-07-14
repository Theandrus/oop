class Alphabet:
    def __init__(self, language, lst):
        self.language = language
        self.lst = lst

    def prnt_all_letters(self):
        print("The language is", self.language, ":", self.lst)

    def number_letters(self):
        print('In ', self.language, 'alphabet is ', len(self.lst), 'letters')


class EngAlphabet(Alphabet):
    def __init__(self, language, lst):
        super().__init__(language, lst)
        self.letters_len = 26

    def is_letter_eng(self, letter):
        if letter in self.lst:
            print("Letter", letter, "is in English alphabet")
        else:
            print("Letter", letter, "is not in English alphabet")

    def eng_text(self):
        print("This is example in English. Have a nice day :)")



ukr = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = Alphabet("Ukrainian", ukr)
b = EngAlphabet("English", eng)
a.prnt_all_letters()
a.number_letters()
b.number_letters()
b.is_letter_eng('u')
b.eng_text()