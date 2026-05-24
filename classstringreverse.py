class reverse:
    def __init__(self, s=""):
        self.s = s
    def reverse_words(self):
        words_list = self.s.split()
        reversed_list = []
        for i in range(len(words_list) - 1, -1, -1):
            reversed_list.append(words_list[i])
        final_string = " ".join(reversed_list)
        return final_string
user_text = input("Enter a sentence: ")
my_reverser = reverse(user_text)
output = my_reverser.reverse_words()
print("Reversed sentence:")
print(output)
