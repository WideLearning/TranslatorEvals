# TranslatorEvals

We (Mikhail and Rodion) could not find a good independent benchmark of major online translators and decided to do it ourselves. Our bets were mostly on DeepL and Yandex correspondingly, but we also take Google as a baseline.

## Method

### Data preparation
To select diverse Engish sentences we took the first 300 sentences from C4 dataset. After filtering out sentences with 5000+ characters we have 280 remaining.
See `data/unparsed_texts.txt` and `parsing.ipynb`.

### Translation
To simplify the process, texts were translated using APIs of these three translators. Unfortunately, Yandex API was not working for us, so we asked another person for whom API was working to help with translation. Resutls are in `trans_dl_go.csv` and `trans_ya.json`, or all together in `dataset.csv`.

### Evaluation

- openai api
- "you are a Russian native speaker and fluent in English. you are given an original sentence in English and three candidate translations. which of them conveys the original meaning in the most accurate and fluent way? print 1, 2 or 3.