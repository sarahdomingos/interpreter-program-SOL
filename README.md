# Viper - An Interpreter for SOL Programs
Viper is a Python-based interpeter that utilizes a domain-specific language for interpreting SOL (Online Session) porgrams, 
posessing a top-down recursive descent implementation approach.

# Overview
Viper serves as a functional interpreter capable of controlling the Chrome browser. 
It enables automated actions for various online services, including email (Gmail), 
video (YouTube), Whatsapp Web, video conferencing (Google Meet), and handling PDF files. 
Additionally, the interpreter incorporates error handling mechanisms for lexical and syntactical analysis and supports comments denoted by the '//' symbol, ignoring the whole line that follows it.

# Implementation
Viper is implemented using Python, leveraging the Selenium library, 
particularly the webdriver package, to establish connections with the Chrome browser and its service links.

# Requirements
To run the Viper interpreter, ensure that you have the following prerequisites installed:

### 1. [Python 3.8+](https://www.python.org/downloads/)
### 2. Selenium 4.0.0
```
pip install selenium==4.0.0
```
### 3. Webdriver-manager package
```
pip install webdriver-manager
```

### 4. Py Simple Gui
```
pip install pysimplegui
```

# Run with multiples examples (no interface)
All inputs examples are in the `program.sol` file, which is called by `main.py` to execute the commands.

To run the interpreter you need to insert the following command in your terminal:

```
python3 main.py
```
OR

```
python main.py
```

# Run single command line (with interface)
```
python mainInterface.py
```
OR
```
python3 mainInterface.py
```

