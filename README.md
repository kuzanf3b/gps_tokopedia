# gps_tokopedia

A sentiment analysis project for Tokopedia Google Play Store reviews. This repository collects app reviews, preprocesses Indonesian text, and trains deep learning models to classify sentiment into three classes: **negative**, **neutral**, and **positive**.

## Project Overview

The project contains two main parts:

1. **Data collection**
   - Scrapes Tokopedia reviews from Google Play Store using `google-play-scraper`.
   - Automatically labels reviews based on star ratings.
   - Exports the data into `dataset_sentimen.csv`.

2. **Sentiment analysis model**
   - Cleans and normalizes Indonesian text.
   - Removes stopwords and handles slang normalization.
   - Balances the dataset across sentiment classes.
   - Trains and compares multiple neural network architectures.

## Repository Contents

- `scraping.py` — Scrapes Google Play reviews and builds the labeled dataset.
- `gps_tokped.ipynb` — Main notebook for preprocessing, training, evaluation, and inference.
- `dataset_sentimen.csv` — Scraped and labeled review dataset.
- `requirements.txt` — Python dependencies used in the project.

## Methodology

The notebook implements the following workflow:

- Load the labeled review dataset
- Normalize text using a custom slang dictionary
- Remove punctuation, numbers, and stopwords
- Filter very short reviews
- Balance the dataset across three sentiment labels
- Convert text into padded token sequences
- Train and evaluate three model variants:
  - **Skema 1:** LSTM + Keras Embedding
  - **Skema 2:** Bi-LSTM + Keras Embedding
  - **Skema 3:** Bi-LSTM + Word2Vec Embedding
- Run inference on new review text

## Dataset Details

The dataset is built from Tokopedia reviews collected from Google Play Store.

- Source app package: `com.tokopedia.tkpd`
- Language: Indonesian
- Labels:
  - `negatif`
  - `netral`
  - `positif`

The notebook balances the data to approximately **10,200 samples** total, with **3,400 samples per class**.

## Results

The notebook reports the following test accuracies:

- **Skema 1:** 91.62%
- **Skema 2:** 89.41%
- **Skema 3:** 86.86%

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Dependencies include:

- `google-play-scraper`
- `pandas`
- `numpy`
- `scikit-learn`
- `tensorflow`
- `gensim`
- `nltk`

## How to Run

### 1. Scrape and prepare the dataset

Run:

```bash
python scraping.py
```

This will:

- collect Tokopedia reviews from Google Play Store
- label the data by rating
- save the result to `dataset_sentimen.csv`

### 2. Train and evaluate the model

Open and run the notebook:

```bash
jupyter notebook gps_tokped.ipynb
```

or run it in Google Colab.

## Inference Example

The notebook includes an inference function that can classify new text input into sentiment categories and return confidence scores.

Example use case:

- Negative review about errors or crashes
- Neutral review with mixed feedback
- Positive review praising app features or usability

## Notes

- The repository is written primarily in Indonesian notebook code, but this README is provided in English.
- Some model settings and metrics are optimized for experimentation and comparison.
- The project uses Indonesian stopwords and a custom slang normalization dictionary.

## License

No license file was provided in the repository.
