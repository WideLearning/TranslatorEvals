import random
import pandas as pd
from typing import Any


dataset = list(pd.read_csv("data/dataset.csv").iterrows())


def format_prompt(original: str, translations: list[str]) -> str:
    assert len(translations) == 3
    prefix = "You are given an original sentence in English and three candidate translations. Which of them conveys the original meaning in the most accurate and fluent way? Score each one from 1 to 10, print only these three numbers, separated by spaces."
    add_index = lambda idx_text: f"{idx_text[0]}) {idx_text[1]}"
    options = list(map(add_index, enumerate(translations, 1)))
    return "\n".join([prefix, original] + options)


def run_human_evaluation(
    dataset: list[tuple[Any, pd.Series]],
) -> tuple[list[list[int]], list[list[str]]]:
    n = len(dataset)
    scores: list[list[int]] = [[] for i in range(n)]
    labels: list[list[str]] = [[] for i in range(n)]

    for idx, (_df_idx, row) in enumerate(dataset):
        print("Sample #", idx + 1)
        labels[idx] = ["google", "deepl", "yandex"]
        random.shuffle(labels[idx])
        original = row["sentence"]
        translations = [row[label] for label in labels[idx]]
        print(format_prompt(original, translations))
        while True:
            try:
                scores[idx] = list(map(int, input("Scores: ").split()))
                break
            except Exception as e:
                print(e)
                print("Try again")
                continue

    return scores, labels


model = input("Name: ")
scores, labels = run_human_evaluation(dataset[:5])
for c, l in zip(scores, labels):
    m = model
    try:
        print(*c, *l, m, sep=",")
    except:
        print(",,,,,,")
