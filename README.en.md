# 🛡️ Secure Password Generator

A password generator developed in **Python with Tkinter**, allowing you to create secure and customized passwords easily.

---

## ✨ Features

- ✅ User-friendly graphical interface with Tkinter.
- ✅ Allows including/excluding:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- ✅ Minimum length control (8 characters).
- ✅ Random generation using the **`secrets`** library (cryptographically secure).
- ✅ Button to copy to clipboard using **pyperclip**.

---

## 🚀 Requirements

- [Python 3.8+](https://www.python.org/downloads/)  
- Required libraries:  
  - tkinter (included by default in Python)  
  - pyperclip  

Install additional dependencies:

```bash
pip install pyperclip
```

---

## ▶️ Execution
Clone the repository and run the script:

```bash
python generador_contraseñas.py
```

A GUI window will open where you can:

- Select password options.
- Adjust the length.
- Generate and copy with a click.

---

## 📸 Screenshot (example)
![Password Generator](https://github.com/albertoh88/generador_de_contrasenhas/blob/main/generador_de_contrasenhas.png)

---

## 💡 Improvement ideas

Save generated password history.

- Add a password "strength" meter.
- Export passwords to an encrypted file.
- Create an executable (.exe) for users without Python.
