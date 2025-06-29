
# 🧠 Infix to Postfix Converter — Python 📘

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/project-active-brightgreen.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

> A classic **Stack-based algorithm** to convert infix expressions (like `A + B`) to postfix (like `AB+`). Handy for compilers, interpreters, and nerding out in data structures.

---

## 🚀 Features

- 🧮 Converts valid infix expressions to postfix (aka Reverse Polish Notation)
- 🧠 Implements a custom `Stack` class (no cheating with Python’s `list` methods)
- 🧪 Easy to test, extend, and learn from
- ✅ Handles operator precedence & parentheses
- 👨‍💻 Beginner-friendly Python code

---

## 🛠️ How to Use

```bash
# 💾 Clone this repo
git clone https://github.com/nisuhR31/infixToPostfix.git
cd infixTpPostfix

# 🏃 Run it
python file.py

# 🧑‍🎓 Sample input
# enter your infix expression: a+b*c^d-f/g+g
# Infix: a+b*c^d-f/g+g
# Postfix: abcd^*+fg/-g+
````

---

## 🧰 Code Overview

```python
infix_expression = input("enter your infix expression: ")
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}")
```

---

## 📂 Project Structure

```
📁 infixToPostfix/
│
├── 📄 file.py  # Main code
└── 📄 README.md             # This file
```

---

## 🧠 Learn the Logic

> We use a **Stack** to track operators and parentheses:

* Operands go directly to the output.
* Operators are pushed or popped based on **precedence**.
* Parentheses are used to override precedence and grouped logic.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
