# Personal Rephrasing Assistant

Welcome to the Personal Rephrasing Assistant, a Python terminal app designed to help you rephrase your text with ease. Whether you're working in a word processor, a code editor, or a web browser, our app recognizes the application you're in and tailors the rephrasing accordingly. Simply select the text and press `command + control + r` to get a fresh rephrase!

## Features

-   **Context-Aware Rephrasing**: The app recognizes the application you're using and adjusts the rephrasing to fit the context.
-   **Quick Access**: Rephrase any selected text with a simple keyboard shortcut.

## Installation

### 1. Clone the Repository

\```
git clone https://github.com/NoyHanan/rephrasing-assistant.git
cd rephrasing-assistant
\```

### 2. Set Up a Virtual Environment (Optional but recommended)

\```python -m venv venv
source venv/bin/activate  # On Windows, use`venv\Scripts\activate`
\```

### 3. Install Dependencies

\```
pip install -r requirements.txt
\```

## Usage

To start the Personal Rephrasing Assistant, run the following command in your terminal:

\```
mpiexec -np 2 python main.py
\```

Once the app is running, simply select the text you want to rephrase in any application and press `command + control + r`. The app will rephrase the text based on the context of the application you're using.

## Contributing

We welcome contributions! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
