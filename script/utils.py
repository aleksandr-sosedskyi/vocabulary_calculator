import csv
from collections import Counter


def save_words_to_file(
    words_counter: Counter, save_to: str | None, limit: int | None
) -> None:
    save_path = "vocab.csv" if save_to is None else save_to

    """Save words to file"""
    with open(save_path, "w") as file:
        if save_path.endswith(".csv"):
            csv_writer = csv.writer(file, delimiter=";")
            csv_writer.writerow(["Word", "Count"])
            for word, count in words_counter.most_common(limit):
                csv_writer.writerow([word, count])
        else:
            for word, count in words_counter.most_common(limit):
                file.write(f"{word} {count}\n")

    print(f"File with {len(words_counter)} was saved to {save_path}")
