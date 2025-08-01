# import re
# class CleanText:
#     def __init__(self,):
#
#     def clean_text(self):
#         # Supprimer les URLs
#         self.text = re.sub(r'https?://\S+|www\.\S+', '', self.text)
#
#         # Supprimer les mentions @username
#         self.text = re.sub(r'@\w+', '', self.text)
#
#         # Supprimer les hashtags #mot (mais garder le mot si tu veux)
#         self.text = re.sub(r'#\w+', '', self.text)
#
#         # Supprimer les emojis (Unicode ranges)
#         emoji_pattern = re.compile(
#             "["
#             "\U0001F600-\U0001F64F"  # emoticons
#             "\U0001F300-\U0001F5FF"  # symbols & pictographs
#             "\U0001F680-\U0001F6FF"  # transport & map symbols
#             "\U0001F1E0-\U0001F1FF"  # flags
#             "]+", flags=re.UNICODE)
#         self.text = emoji_pattern.sub(r'', self.text)
#
#         # Supprimer les espaces en trop
#         self.text = re.sub(r'\s+', ' ', self.text).strip()
#
#
#
# st="""Salut @you! Regarde ce site https://example.com 😄 #cool"""
# d=CleanText(st)
# print(d.text)
import re

def clean_text(text):
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

class CleanText:
    def __init__(self, text):
        self.original = text
        self.cleaned = clean_text(text)

    def get(self):
        return self.cleaned

# if __name__ == "__main__":
#     d = CleanText("Salut @you! Regarde ce site https://example.com 😄 #cool")
#     print(d.get())
