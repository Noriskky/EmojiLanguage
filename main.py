import pyperclip

EMOJI = ":regional_indicator_%s: "


def convert(input):
  output = ""
  for character in input:
    if character.isalpha():
      output += EMOJI % character.lower()
    else:
      output += character
  return output


def main():
  print("=======================================================")
  print("Hey this is EmojiLanguage!")
  print("it will convert your text to emojis made for Discord.")
  print("Written by @Noriskky")
  print("=======================================================")
  print("")

  print("Enter your text: ")
  input_text = input()
  pyperclip.copy(convert(input_text))
  pyperclip.paste()
  print("Converted text copied to clipboard!")


main()
