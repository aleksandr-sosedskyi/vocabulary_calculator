import click
from text_processor import TextProcessor as tp
from utils import save_words_to_file


@click.command()
@click.option("--limit", help="number of words to extract", type=click.INT)
@click.option("--save_to", help="custom path to save to", type=click.Path())
@click.argument("file_path", type=click.Path(exists=True))
def calc(file_path: str, save_to: str | None, limit: int | None) -> None:
    """Calculate vocabulary from pdf file"""
    if file_path.endswith(".pdf"):
        file_text = tp.extract_text_from_pdf(file_path)
    else:
        file_text = tp.extract_text_from_file(file_path)

    words_from_text = list(tp.lemmatize_words(file_text))
    words_counter = tp.get_words_counter(words_from_text)

    save_words_to_file(words_counter, save_to, limit)
    print(f"Total words: {words_counter.total()}")


if __name__ == "__main__":
    calc()
