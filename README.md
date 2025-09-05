# Digit Extractor in Python  

This is a simple Python program that takes an integer as input, calculates the number of digits, extracts each digit mathematically, and prints them in order.  

## 📌 Features
- Counts the number of digits in a given integer  
- Extracts each digit using modular arithmetic (no string conversion)  
- Displays the digits in correct order (left → right)  

---

## 💻 Example  

### Input:
ENTER: 54321

### Output:
The digits are:
5 4 3 2 1


---

## 🛠️ How It Works
1. Finds the total number of digits by repeatedly multiplying powers of 10.  
2. Extracts each digit using modulo (`%`) and subtraction.  
3. Stores digits in a list and then prints them in correct order.  

---

## 📂 Project Structure
digit_extractor/
│── digit_extractor.py # main Python script
│── README.md # project documentation

---

## ▶️ Usage
Clone this repository:
```bash
git clone https://github.com/SoumikSinha/digit-extractor.git
cd digit-extractor

Run the program:
python3 digit_extractor.py
