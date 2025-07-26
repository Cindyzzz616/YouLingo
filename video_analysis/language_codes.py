import pandas as pd
import csv

LANG_REPLACEMENTS = {
    'sqi': 'als',
    'ara': 'arb',
    'ave': 'NA',
    'aym': 'ayr',
    'aze': 'azb',
    'bel': 'NA',
    'bis': 'NA',
    'bos': 'NA',
    'nya': 'NA',
    'zho': 'cmn',
    'cor': 'NA',
    'cos': 'NA',
    'cre': 'NA',
    'epo': 'NA',
    'est': 'ekk',
    'ful': 'NA',
    'grn': 'NA',
    'hat': 'NA',
    'hmo': 'NA',
    'ina': 'NA',
    'ile': 'NA',
    'ipk': 'NA',
    'ido': 'NA',
    'iku': 'NA',
    'kau': 'knc',
    'kaz': 'NA',
    'kon': 'NA',
    'kur': 'ckb',
    'lat': 'NA',
    'lim': 'NA',
    'lub': 'NA',
    'lav': 'lvs',
    'glv': 'NA',
    'mlg': 'plt',
    'msa': 'zsm',
    'mah': 'NA',
    'nau': 'NA',
    'nep': 'npi',
    'nno': 'NA',
    'nbl': 'nde',
    'oji': 'ojg',
    'chu': 'NA',
    'orm': 'hae',
    'ori': 'ory',
    'pli': 'NA',
    'fas': 'pes',
    'pus': 'NA',
    'que': 'qul',
    'srd': 'sro',
    'smo': 'NA',
    'swa': 'swh',
    'ssw': 'NA',
    'tsn': 'NA',
    'tso': 'NA',
    'twi': 'NA',
    'tah': 'NA',
    'uzb': 'uzn',
    'ven': 'NA',
    'vol': 'NA',
    'wln': 'NA',
    'yid': 'ydd',
    'zha': 'NA'
}

LANG_REPLACEMENTS_NAMES = {
    'als': 'Albanian',
    'arb': 'Arabic',
    'ayr': 'Aymara',
    'azb': 'South Azerbaijani',
    'cmn': 'Mandarin Chinese',
    'ekk': 'Estonian',
    'knc': 'Kanuri',
    'ckb': 'Kurdish',
    'lvs': 'Latvian',
    'plt': 'Malagasy',
    'zsm': 'Malay',
    'npi': 'NEPALI',
    'nde': 'Ndebele',
    'ojg': 'Ojibwa',
    'hae': 'Oromo, Eastern',
    'ory': 'Oriya',
    'pes': 'Persian',
    'qul': 'Bolivian Quechua',
    'sro': 'Campidanese Sardinian',
    'swh': 'Swahili',
    'uzn': 'UZBEK',
    'ydd': 'Standard Yiddish'
}

def extract_iso_codes_from_argos(file_path):
    iso_codes = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                iso_codes.append(row[1].strip())
    return iso_codes

def map_iso6391_to_6393(tsv_file_path, iso6391_codes):
    mapping = {}
    with open(tsv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            part1 = row.get("Part1", "").strip()
            id_6393 = row.get("Id", "").strip()
            if part1:
                mapping[part1] = id_6393

    # Build result: look up each input ISO 639-1 code in the mapping
    result = {code: mapping.get(code, None) for code in iso6391_codes}
    return result

def map_iso6391_to_language_name(tsv_file_path, iso6391_codes):
    mapping = {}
    with open(tsv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            id_6391 = row.get("Part1", "").strip()
            ref_name = row.get("Ref_Name", "").strip()
            if id_6391:
                mapping[id_6391] = ref_name

    # Build result: look up each input ISO 639-1 code in the mapping
    result = {code: mapping.get(code, None) for code in iso6391_codes}
    return result

# def find_argos_langs_in_phoible(tsv_file_path, iso6393_codes):
#     mapping = {}
#     with open(tsv_file_path, mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file, delimiter='\t')
#         for row in reader:
#             id_6393 = row.get("ISO6393", "").strip().strip('"').lower()
#             lang_name = row.get("LanguageName", "").strip().strip('"').lower()
#             if id_6393 and lang_name:
#                 mapping[id_6393] = lang_name

#     print("First few entries in mapping from Phoible:")
#     for k in list(mapping.keys())[:5]:
#         print(repr(k))

#     print("Sample 639-3 codes from Argos:")
#     for k in argos_langs_6393[:5]:
#         print(repr(k))

#     # Build result: look up each input ISO 639-1 code in the mapping
#     result = {code: mapping.get(code, None) for code in iso6393_codes}
#     return result

def find_argos_langs_in_phoible(df_phoible, iso6393_codes):
    # Drop rows with missing ISO6393 values and strip whitespace
    df_clean = df_phoible.dropna(subset=['ISO6393']).copy()
    df_clean['ISO6393'] = df_clean['ISO6393'].astype(str).str.strip()
    df_clean['LanguageName'] = df_clean['LanguageName'].astype(str).str.strip()

    # Drop duplicates to map each ISO6393 code to one language name
    lang_map = df_clean.drop_duplicates(subset='ISO6393')[['ISO6393', 'LanguageName']]
    mapping = dict(zip(lang_map['ISO6393'], lang_map['LanguageName']))

    # Look up each 639-3 code
    result = {code: mapping.get(code) for code in iso6393_codes}
    return result

def reverse_lookup_iso6391_from_phoible_name(
    phoible_lang_name,
    iso6393_to_iso6391_map,
    argos_iso6391_list
):
    """
    Given a Phoible language name, return the ISO 639-1 code used in Argos Translate.
    """
    phoible_df = pd.read_csv(phoible_file_path)

    # Step 1: Find ISO 639-3 code for the Phoible language
    match = phoible_df[phoible_df['LanguageName'].str.strip().str.lower() == phoible_lang_name.strip().lower()]
    
    if match.empty:
        return None, "Language not found in Phoible"
    
    iso6393_code = match['ISO6393'].values[0].strip()

    if iso6393_code in LANG_REPLACEMENTS_NAMES.keys():
        rev_map_names = {v: k for k, v in LANG_REPLACEMENTS.items()}
        iso6393_code = rev_map_names[iso6393_code]
    
    # Step 2: Check for replacement (if needed)
    if iso6393_code in LANG_REPLACEMENTS.values():
        for k, v in LANG_REPLACEMENTS.items():
            if v == iso6393_code:
                iso6391_code = k
                break
        else:
            return None, "No matching ISO 639-1 code found in LANG_REPLACEMENTS"
    else:
        # Use direct mapping from ISO 639-3 to ISO 639-1
        rev_map = {v: k for k, v in iso6393_to_iso6391_map.items()}
        iso6391_code = rev_map.get(iso6393_code)

    # Step 3: Confirm the code is in Argos Translate
    if iso6391_code in argos_iso6391_list:
        return iso6391_code, "Found in Argos"
    else:
        return iso6391_code, "Mapped but not in Argos"

# Example usage
file_path = 'video_analysis/argos_languages.csv'  # Replace with your file path
codes = extract_iso_codes_from_argos(file_path)
print(codes)
print(len(codes))

# Sample list of ISO 639-1 codes
iso6391_list = codes  # 'xx' is invalid on purpose

# Path to the tab-separated ISO 639-3 registry file
tsv_file_path = "video_analysis/iso-639-3.txt"  # Replace with your actual path

iso_mapping = map_iso6391_to_6393(tsv_file_path, iso6391_list)
iso_language_names = map_iso6391_to_language_name(tsv_file_path, iso6391_list)

for code1, code3 in iso_mapping.items():
    print(f"{code1} → {code3}")

for code1, lang_name in iso_language_names.items():
    print(f"{code1} → {lang_name}")

# Find Argos languages in Phoible
phoible_file_path = "video_analysis/phoible.csv"
phoible_df = pd.read_csv(phoible_file_path)
argos_langs_6393 = [code for code in iso_mapping.values() if code is not None]
phoible_langs = find_argos_langs_in_phoible(phoible_df, argos_langs_6393)
for code3, lang_name in phoible_langs.items():
    if lang_name:
        print(f"{code3} → {lang_name}")
    elif LANG_REPLACEMENTS[code3] != 'NA':
        print(f"{code3} → {LANG_REPLACEMENTS_NAMES[LANG_REPLACEMENTS[code3]]}")
    else: 
        print(f"{code3} → Not found in Phoible")

argos_iso6391_list = extract_iso_codes_from_argos('video_analysis/argos_languages.csv')
iso_mapping = map_iso6391_to_6393("video_analysis/iso-639-3.txt", argos_iso6391_list)

# Lookup
code, status = reverse_lookup_iso6391_from_phoible_name(
    "Mandarin Chinese", iso_mapping, argos_iso6391_list
)
print(f"ISO 639-1 Code: {code}, Status: {status}")