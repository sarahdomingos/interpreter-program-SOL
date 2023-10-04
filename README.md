# Viper - A language for the Programa_SOL Interpreter
Viper is a domain-specific language for interpreting Programa_SOL (Online Session Program), 
utilizing a top-down recursive descent implementation approach.

# Overview
Viper serves as a functional interpreter capable of controlling the Chrome browser. 
It enables automated actions for various online services, including email (Gmail), 
video (Youtube), Whatsapp Web, video conferencing (Google Meet), and handling PDF files. 
Additionally, the interpreter incorporates error handling mechanisms for lexical and syntactical analysis. 
Furthermore, Viper can process comments denoted by the `#` symbol, ignoring any text following it.

# Implementation
Viper is implemented using Python, leveraging the Selenium library, 
particularly the webdriver package, to establish connections with the Chrome browser and its service links.

# Requirements

To run the Viper interpreter, ensure you have the following prerequisites installed:

### 1. [Python 3.8+](https://www.python.org/downloads/)
### 2. Selenium 4.0.0
```
pip install selenium==4.0.0
```
### 3. Webdriver-manager package
```
pip install webdriver-manager
```

# Usage

All inputs examples are in the `program.sol` file, which is called by `main.py` to execute the commands.

To run the interpreter you need to insert the following command in your terminal:

```
python3 main.py
```
OR

```
python main.py
```
