# Supported languages: https://cloud.google.com/translate/docs/languages
# TODO do the code-language conversion

from google.cloud import translate

def translate_text(text="Hello, world!", project_id="youjujube", to_code='zh'):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": to_code,
        }
    )

    # print(response.translations)

    translated_text = []

    for translation in response.translations:
        # print("Translated text: {}".format(translation.translated_text))
        translated_text.append(translation.translated_text)

    return translated_text

if __name__ == '__main__':
    translated_text = translate_text(text="There were only two ways to get out of this mess if they all worked together. The problem was that neither was all that appealing. One would likely cause everyone a huge amount of physical pain while the other would likely end up with everyone in jail. In Sam's mind, there was only one thing to do. He threw everyone else under the bus and he secretly sprinted away leaving the others to take the fall without him.",
                                     to_code='ne')
    print(translated_text)
