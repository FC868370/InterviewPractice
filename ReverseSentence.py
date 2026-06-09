def reverse(str input)
  output = ""
  letters = input.split()
  letters.reverse()
  for letter in letters
    output.append(letter)

  return output
