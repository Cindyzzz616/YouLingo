import argostranslate.package
import argostranslate.translate

from language_codes import reverse_lookup_iso6391_from_phoible_name
from language_codes import iso_mapping
from language_codes import argos_iso6391_list

FROM_CODE = "en"  # English
TO_CODE = "zh"  # Chinese


def install_argo_packages(to_code):
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == FROM_CODE and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

def translate_text(text: str, from_lang: str = FROM_CODE, to_lang: str = TO_CODE) -> str:
    to_code = str(reverse_lookup_iso6391_from_phoible_name(to_lang, iso_mapping, argos_iso6391_list)[0])
    print(to_code)
    install_argo_packages(to_code)
    return argostranslate.translate.translate(text, from_lang, to_code)

if __name__ == "__main__":
    # Print available languages
    print("Available languages:")
    for lang in argostranslate.translate.get_installed_languages():
        print(f"{lang.code}: {lang.name}")

    # Example translation
    print(f"Translating from {FROM_CODE} to {TO_CODE}...")
    # Translate
    translatedText = translate_text('Hello world', to_lang='Malay')
    print(translatedText)