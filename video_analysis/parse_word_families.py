# For a description of the word family corpus, visit this website: https://www.wgtn.ac.nz/lals/resources/paul-nations-resources/vocabulary-lists.

import re
from pathlib import Path
from collections import defaultdict
import pickle

word_families_folder = Path("video_analysis/external_data/basewords_130")
all_families = {}

for path in word_families_folder.iterdir():
    
    families = defaultdict(list)
    current_head = None
    level = re.search(r"basewrd(\d+)", path.name)
    if level:
        level = int(level.group(1))
    else:
        level = -1

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            if not raw.strip():
                continue

            # keep leading whitespace to detect indentation
            m = re.match(r"^(\s*)([A-Za-z'_-]+)\s+(\d+)\s*$", raw)
            if not m:
                continue

            lead_ws, word, freq = m.groups()
            freq = int(freq)
            is_member = len(lead_ws) > 0   # any indent (tab or spaces) → member

            if not is_member:
                # new family head
                current_head = word
                families[current_head].append((word, freq))
            else:
                if current_head is None:
                    # skip stray member lines just in case
                    continue
                families[current_head].append((word, freq))

    all_families[level] = families
    # NOTE the first item in each entry is the head of the family

with open("video_analysis/external_data/word_families.pkl", "wb") as f:
    pickle.dump(all_families, f)

if __name__ == '__main__':
    # Example: print first 3 families
    print(all_families.keys())
    for head, members in list(all_families[30].items())[:10]:
        print(head, "→", members)
