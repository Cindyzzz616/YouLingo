import nltk
nltk.download("cmudict")
nltk.download('averaged_perceptron_tagger_eng')

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets_json')

nltk.help.upenn_tagset()
tokens = nltk.word_tokenize("Hello world, this is a test.")
tags = nltk.pos_tag(tokens)
print(tags)

# use this ./.venv/bin/python -m pip install package to specify where the package should be installed
# activate the virtual environment: source .venv/bin/activate