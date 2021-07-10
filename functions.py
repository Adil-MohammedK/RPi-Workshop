def say_hello(n):
    for x in range(0,n):
        print("Hello")

def make_polite(sentence):
	polite_sentence = sentence + ' please'
	return polite_sentence

say_hello(4)

print(make_polite('Pass the salt'))
