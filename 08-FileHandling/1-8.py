def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
file_words = file_content.split()

total = 0
for item in file_words:
   total += 1

print(total)

