#Implement a cypher which converts text to emoji or something.

text_to_emoji_mapping = {"food": "🍔", "cat": "🐱", "dog": "🐕", "happy": "😊"} 


def text_to_emoji(user_input):
	words = ""
	if "," in user_input:
		user_input = user_input.replace(' ', '')
		words = user_input.split(",")
	else:
		words = user_input.split(' ')
	emoji_output = ""
	for word in words:
		if word not in text_to_emoji_mapping:
			print ("")
			print ("")
			print (("%s is not a valid word, please re-do your request with a list of valid words") %(word))
			exit()

		emoji_output = emoji_output + text_to_emoji_mapping[word] + " "
	print ("")
	print ("")
	print (emoji_output)


def main():
	print ("")
	print ("")
	print ("Words available: food, cat, dog, happy")
	print ("")
	print ("")
	user_input = input("Enter the desired text you would like converted to emojis: ")
	text_to_emoji(user_input)

	

main()