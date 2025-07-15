# 🧠 Markov Chain Text Generator

This project implements a simple **Markov Chain-based text generation algorithm** using Python. It reads input from a text file, builds a statistical model of word transitions, and generates new text that mimics the input style. The result is saved in a separate output file.

---

## 🚀 Features

- Reads text from a file (`input.txt`)
- Generates text based on 1st-order Markov chains
- Saves the generated output to `output.txt`
- Uses only built-in Python libraries — no installation required!

---

## 📂 Project Structure

| File/Folder     | Description                                    |
|----------------|------------------------------------------------|
| `main.py`       | 🔁 Main script containing the text generation logic |
| `input.txt`     | 📥 Input file containing sample text for training  |
| `output.txt`    | 📤 Output file where generated text is saved       |
| `README.md`     | 📘 This file, with instructions and structure      |

---

## 🛠️ How It Works

1. The program reads `input.txt` as training data.
2. It splits the text into words and builds a **Markov chain model**.
3. A starting word is chosen (default: `"Technology"`).
4. Using the model, it predicts the next word 50 times to form a sentence.
5. The generated result is saved into `output.txt`.

---

## 🧪 Example

**Input (`input.txt`):**

> Technology has rapidly transformed the world we live in...

**Output (`output.txt`):**

> Technology has rapidly transformed the world we live in an age of data collection? What happens to jobs as machines...

---

## ▶️ How to Run

```bash
python main.py
```

Make sure `input.txt` is in the same directory.

---

## 💡 Notes

- If `output.txt` doesn't exist, it will be automatically created.
- You can change the starting word by editing the `start_word` value inside `main.py`.

---

## 🧾 License

This project is licensed under the MIT License. Free to use and modify.

---
