import random
from collections import defaultdict

class MarkovChainTextGenerator:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.model[current_word].append(next_word)

    def generate(self, start_word, length=50):
        if start_word not in self.model:
            return "Start word not found in training data."
        result = [start_word]
        current_word = start_word
        for _ in range(length - 1):
            next_words = self.model.get(current_word, None)
            if not next_words:
                break
            current_word = random.choice(next_words)
            result.append(current_word)
        return ' '.join(result)

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        sample_text = f.read()

    generator = MarkovChainTextGenerator()
    generator.train(sample_text)

    start_word = "Technology"
    generated_text = generator.generate(start_word=start_word, length=50)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Generated Text:\n")
        f.write(generated_text)

    print(f"Text generated and saved to {output_file} ✅")

if __name__ == "__main__":
    main()
