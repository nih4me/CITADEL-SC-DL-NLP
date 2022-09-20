# CITADEL-SC-DL-NLP

## Install `pipenv`

```sh
pip install pipenv
```

## Install packages for NLP

```sh
cd NLP
pipenv install
pipenv shell
pip install torch
python3 -m spacy download fr_core_news_sm
python download.py # For downloading the cammembert model, nltk data, ... locally
```

## Install packages for DL

```sh
cd DL
pipenv install
pipenv shell
python download.py # For downloading .... locally
```
