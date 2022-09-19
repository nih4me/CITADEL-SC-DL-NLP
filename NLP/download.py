from transformers import CamembertModel, CamembertTokenizer
import spacy

tokenizer = CamembertTokenizer.from_pretrained("camembert/camembert-base-wikipedia-4gb")
camembert = CamembertModel.from_pretrained("camembert/camembert-base-wikipedia-4gb")

nlp = spacy.load("fr_core_news_sm")
