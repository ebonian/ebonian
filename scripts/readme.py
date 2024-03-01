import re
import random

filename = "README.md"

phrase = "Hi, I'm Tanadon"

emojis = ["😊", "😄", "😎", "👋", "🎉", "👍", "💡", "💻", "🖥️", "👨‍💻", "👩‍💻", "⌨️", "🖱️", "📱", "🌟", "✨", "💬"]

with open(filename, mode="r", encoding="utf-8") as file:
    file_contents = file.readlines()

for i, line in enumerate(file_contents):
    if phrase in line:
        existing_emoji = re.findall(r'(\s*\S)$', line)
        line = re.sub(r'\s*\S$', '', line)
        new_emojis = [emoji for emoji in emojis if emoji != existing_emoji[0]]
        random_emoji = random.choice(new_emojis)
        file_contents[i] = line.rstrip() + f" {random_emoji}\n"
        break

with open(filename, mode="w", encoding="utf-8") as file:
    file.writelines(file_contents)

print("Finished updating README.md")
