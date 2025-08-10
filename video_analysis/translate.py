import argostranslate.package
import argostranslate.translate

from language_codes import reverse_lookup_iso6391_from_phoible_name
from language_codes import iso_mapping
from language_codes import argos_6391_list

FROM_CODE = "en"  # Translate from English by default

def install_argo_packages(to_lang, from_code = FROM_CODE):
    # Download and install Argos Translate package
    to_code = str(reverse_lookup_iso6391_from_phoible_name(to_lang, iso_mapping, argos_6391_list)[0])

    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    # for package in available_packages:
    #     print(package)
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    # TODO add something to check whether a package has already been downloaded; also add error catching

def translate_text(text: str, to_lang: str, from_lang: str = FROM_CODE) -> str:
    """
    Translate a string of text from from_lang to to_lang, which are language names in Phoible.
    """
    to_code = str(reverse_lookup_iso6391_from_phoible_name(to_lang, iso_mapping, argos_6391_list)[0])
    return argostranslate.translate.translate(text, from_lang, to_code)

if __name__ == "__main__":
    # Print available languages
    print("Available languages:")
    for lang in argostranslate.translate.get_installed_languages():
        print(f"{lang.code}: {lang.name}")

    # Example usage
    to_lang = 'Mandarin Chinese'

    # Install necessary pacakges
    if to_lang not in argostranslate.translate.get_installed_languages():
        install_argo_packages(to_lang=to_lang)

    # Translate
    translatedText = translate_text(
        "There were only two ways to get out of this mess if they all worked together. The problem was that neither was all that appealing. One would likely cause everyone a huge amount of physical pain while the other would likely end up with everyone in jail. In Sam's mind, there was only one thing to do. He threw everyone else under the bus and he secretly sprinted away leaving the others to take the fall without him.", 
        to_lang=to_lang)
    print(translatedText)