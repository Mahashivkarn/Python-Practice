words = ["Donkey", "bad", "bekar"]

with open("files.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("files.txt", "w") as f:
    f.write(content)