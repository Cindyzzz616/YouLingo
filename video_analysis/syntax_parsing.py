# import stanza
# # stanza.download('en')

# from collections import defaultdict

# tree = defaultdict(list)

# nlp = stanza.Pipeline('en')
# doc = nlp("Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`.")

# dependencies = doc.sentences[0].dependencies

# for head, rel, dep in dependencies:
#     head_text = head.text
#     dep_text = dep.text
#     tree[head_text].append((rel, dep_text))

# print(tree['fox'])
# print(tree)
# # [('det', 'The'), ('amod', 'quick'), ('amod', 'brown')]'

# for head, rel, dep in dependencies:
#     print(f"{dep.text} --[{rel}]--> {head.text}")

# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.DiGraph()

# for head, rel, dep in dependencies:
#     G.add_edge(head.text, dep.text, label=rel)

# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, arrows=True)
# edge_labels = nx.get_edge_attributes(G, 'label')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps over the lazy dog.")

print(doc)

for token in doc:
    print(token.dep_)

pause_positions = []
for token in doc:
    if token.dep_ in ("punct", "cc", "mark", "advcl", "conj", "parataxis"):
        pause_positions.append(token.i)

print([doc[i].text for i in pause_positions])
