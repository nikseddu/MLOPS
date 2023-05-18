# tagifai/data.py
from nltk.stem import PorterStemmer
import re

from config import config

from collections import Counter



def preprocess(df, lower, stem, min_freq):
    """Preprocess the data."""
    df["text"] = df.title + " " + df.description  # feature engineering
    df.text = df.text.apply(clean_text, lower=lower, stem=stem)  # clean text
    df = replace_oos_labels(
        df=df, labels=config.ACCEPTED_TAGS, label_col="tag", oos_label="other"
    )  # replace OOS labels
    df = replace_minority_labels(
        df=df, label_col="tag", min_freq=min_freq, new_label="other"
    )  # replace labels below min freq

    return df




def clean_text(text, lower=True, stem=False, stopwords=config.STOPWORDS):
    """Clean raw text."""
    # Lower
    if lower:
        text = text.lower()

    # Remove stopwords
    if len(stopwords):
        pattern = re.compile(r'\b(' + r"|".join(stopwords) + r")\b\s*")
        text = pattern.sub('', text)

    # Spacing and filters
    text = re.sub(
        r"([!\"'#$%&()*\+,-./:;<=>?@\\\[\]^_`{|}~])", r" \1 ", text
    )  # add spacing between objects to be filtered
    text = re.sub("[^A-Za-z0-9]+", " ", text)  # remove non alphanumeric chars
    text = re.sub(" +", " ", text)  # remove multiple spaces
    text = text.strip()  # strip white space at the ends

    # Remove links
    text = re.sub(r"http\S+", "", text)

    # Stemming
    if stem:
        text = " ".join([stemmer.stem(word, to_lowercase=lower) for word in text.split(" ")])

    return text



def replace_oos_labels(df, labels, label_col, oos_label="other"):
    """Replace out of scope (oos) labels."""
    oos_tags = [item for item in df[label_col].unique() if item not in labels]
    df[label_col] = df[label_col].apply(lambda x: oos_label if x in oos_tags else x)
    return df

def replace_minority_labels(df, label_col, min_freq, new_label="other"):
    """Replace minority labels with another label."""
    labels = Counter(df[label_col].values)
    labels_above_freq = Counter(label for label in labels.elements() if (labels[label] >= min_freq))
    df[label_col] = df[label_col].apply(lambda label: label if label in labels_above_freq else None)
    df[label_col] = df[label_col].fillna(new_label)
    return df
