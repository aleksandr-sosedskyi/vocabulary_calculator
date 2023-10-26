# Readme

## Vocabulary Calculator

This Python script, `main.py`, calculates the vocabulary of a file (Currently only PDF is supported). It processes the text content of the file, tokenizes it, and lemmatizes the words to extract unique words. It then counts the frequency of each word and saves the results to a file (CSV and common text file are supported). Additionally, you can specify a limit for the number of words to extract and provide a custom path for saving the file.

## Prerequisites

Before running the script, ensure you have the necessary dependencies and libraries installed. You can use the provided Makefile to simplify the setup process:

```shell
make install
```

This command will install the project's dependencies using Poetry, download the English language model for spaCy, and install pre-commit hooks for code quality checks.

## Usage

To use the Vocabulary Calculator, execute the script `main.py` with the following command:

```shell
poetry run python script/main.py [OPTIONS] FILE_PATH
```

### Options

- `--limit`: The number of words to extract. This option limits the output to the most frequently occurring words.
- `--save_to`: A custom path to save the output CSV file. By default, the file is saved as "vocab.csv" in the current directory.

### Example

Calculate the vocabulary of a PDF file and save the results to a custom path:

```shell
python main.py --limit 100 --save_to custom_vocab.csv my_pdf.pdf
```
