# import re
# import spacy
# import emoji
#
# class ClaimExtractor:
#     def __init__(self, lang_model="en_core_web_md"):
#         try:
#             self.nlp = spacy.load(lang_model)
#         except OSError:
#             raise Exception(f"SpaCy model '{lang_model}' not installed. Run: python -m spacy download {lang_model}")
#
#     def clean_text(self, text):
#         text = re.sub(r"http\S+|www\S+", "", text)        # remove URLs
#         text = re.sub(r"@\w+", "", text)                  # remove mentions
#         text = re.sub(r"#\w+", "", text)                  # remove hashtags
#         text = emoji.replace_emoji(text, replace="")      # remove emojis
#         text = re.sub(r"[^\w\s.,!?]", "", text)           # remove special characters
#         return text.strip().lower()
#
#     def is_claim(self, sentence):
#         opinion_starters = ["i think", "i believe", "in my opinion", "i feel"]
#         if any(sentence.text.lower().startswith(p) for p in opinion_starters):
#             return False
#         has_verb = any(token.pos_ == "VERB" for token in sentence)
#         has_entity = len(sentence.ents) > 0
#         return has_verb and has_entity
#
#     def classify_claim(self, sentence):
#         text = sentence.text.lower()
#         if "never" in text or "always" in text:
#             return "expressive false"
#         elif "confirmed" in text or "announced" in text:
#             return "true"
#         elif "rumor" in text or "not confirmed" in text:
#             return "false"
#         else:
#             return "expressive true"
#
#     def extract_claims(self, text):
#         results = []
#         cleaned = self.clean_text(text)
#         doc = self.nlp(cleaned)
#
#         for sent in doc.sents:
#             if self.is_claim(sent):
#                 label = self.classify_claim(sent)
#                 entities = [ent.text for ent in sent.ents]
#                 results.append({
#                     "claim": sent.text,
#                     "entities": entities,
#                     "confidence": 0.9,
#                     "label": label
#                 })
#         return results
#
# if __name__ == "__main__":
#     text = """
#     The president announced a new reform yesterday.
#     I think it's a good move.
#     The reform has never been approved by Congress.
#     """
#
#     extractor = ClaimExtractor()
#     claims = extractor.extract_claims(text)
#
#     if claims:
#         for claim in claims:
#             print(claim)
#     else:
#         print("No claims detected.")


# import re
# import stanza
# import emoji
#
# class ClaimExtractor:
#     def __init__(self, lang="en"):
#         try:
#             self.nlp = stanza.Pipeline(lang=lang, processors='tokenize,ner,pos', use_gpu=False)
#         except Exception as e:
#             raise Exception(f"Stanza pipeline for '{lang}' could not be loaded: {e}")
#
#     def clean_text(self, text):
#         text = re.sub(r"http\S+|www\S+", "", text)        # remove URLs
#         text = re.sub(r"@\w+", "", text)                  # remove mentions
#         text = re.sub(r"#\w+", "", text)                  # remove hashtags
#         text = emoji.replace_emoji(text, replace="")      # remove emojis
#         text = re.sub(r"[^\w\s.,!?]", "", text)           # remove special characters
#         return text.strip().lower()
#
#     def is_claim(self, sentence):
#         opinion_starters = ["i think", "i believe", "in my opinion", "i feel"]
#         sent_text = sentence.text.lower()
#         if any(sent_text.startswith(p) for p in opinion_starters):
#             return False
#         has_verb = any(word.upos == "VERB" for word in sentence.words)
#         has_entity = len(sentence.ents) > 0
#         return has_verb and has_entity
#
#     def classify_claim(self, sentence):
#         text = sentence.text.lower()
#         if "never" in text or "always" in text:
#             return "expressive false"
#         elif "confirmed" in text or "announced" in text:
#             return "true"
#         elif "rumor" in text or "not confirmed" in text:
#             return "false"
#         else:
#             return "expressive true"
#
#     def extract_claims(self, text):
#         results = []
#         cleaned = self.clean_text(text)
#         doc = self.nlp(cleaned)
#
#         for sent in doc.sentences:
#             if self.is_claim(sent):
#                 label = self.classify_claim(sent)
#                 entities = [ent.text for ent in sent.ents]
#                 results.append({
#                     "claim": sent.text,
#                     "entities": entities,
#                     "confidence": 0.9,
#                     "label": label
#                 })
#         return results
#
# if __name__ == "__main__":
#     text = """
#     The president announced a new reform yesterday.
#     I think it's a good move.
#     The reform has never been approved by Congress.
#     """
#
#     extractor = ClaimExtractor()
#     claims = extractor.extract_claims(text)
#
#     if claims:
#         for claim in claims:
#             print(claim)
#     else:
#         print("No claims detected.")


#
#
# import re
# import stanza
# import emoji
#
# class ClaimExtractor:
#     def __init__(self, lang="en"):
#         """
#         Initialise le pipeline Stanza pour la langue donnée.
#         """
#         try:
#             self.nlp = stanza.Pipeline(lang=lang, processors='tokenize,ner,pos', use_gpu=False)
#             self.lang = lang
#         except Exception as e:
#             raise Exception(f"Stanza pipeline for '{lang}' could not be loaded: {e}")
#
#     def clean_text(self, text):
#         """
#         Nettoie le texte en supprimant URLs, mentions, hashtags, emojis, caractères spéciaux (sauf ponctuation basique),
#         et en normalisant les espaces.
#         """
#         text = re.sub(r"http\S+|www\S+", "", text)           # URLs
#         text = re.sub(r"@\w+", "", text)                     # Mentions
#         text = re.sub(r"#\w+", "", text)                     # Hashtags
#         text = emoji.replace_emoji(text, replace="")         # Emojis
#         # Conserver accents et ponctuation de base (.,!?) en supprimant autres caractères spéciaux
#         text = re.sub(r"[^\w\sàâçéèêëîïôûùüÿñæœ.,!?-]", "", text, flags=re.UNICODE)
#         text = re.sub(r"\s+", " ", text)                     # Espaces multiples → simple espace
#         return text.strip()
#
#     def is_claim(self, sentence):
#         """
#         Détermine si une phrase est potentiellement un claim :
#         - ne commence pas par une opinion
#         - contient au moins un verbe
#         - contient au moins une entité nommée ou un nombre/datetime
#         """
#         opinion_starters = ["i think", "i believe", "in my opinion", "i feel", "je pense", "je crois", "à mon avis"]
#         sent_text = sentence.text.lower()
#
#         if any(sent_text.startswith(p) for p in opinion_starters):
#             return False
#
#         has_verb = any(word.upos == "VERB" for word in sentence.words)
#         has_entity = len(sentence.ents) > 0
#
#         # Vérifie la présence de nombres, dates ou entités types utiles
#         has_numbers_or_dates = any(ent.type in ["DATE", "TIME", "MONEY", "PERCENT", "QUANTITY", "CARDINAL"] for ent in sentence.ents)
#
#         return has_verb and (has_entity or has_numbers_or_dates)
#
#     def classify_claim(self, sentence):
#         """
#         Classification simple basée sur la présence de mots clés,
#         retourne une catégorie indicative.
#         """
#         text = sentence.text.lower()
#
#         keywords = {
#             "expressive_false": ["never", "pas du tout", "jamais", "aucun", "impossible", "not confirmed", "rumor", "rumeur"],
#             "true": ["confirmed", "announced", "déclaré", "confirmé", "officiel", "official"],
#             "expressive_true": ["probably", "likely", "peut-être", "possible", "possible que"]
#         }
#
#         for label, kw_list in keywords.items():
#             if any(kw in text for kw in kw_list):
#                 return label
#
#         return "neutral"
#
#     def extract_claims(self, text):
#         """
#         Extrait les claims d'un texte nettoyé.
#         Retourne une liste de dictionnaires avec claim, entités, confiance et label.
#         """
#         results = []
#         cleaned = self.clean_text(text)
#         doc = self.nlp(cleaned)
#
#         for sent in doc.sentences:
#             if self.is_claim(sent):
#                 label = self.classify_claim(sent)
#                 entities = [ent.text for ent in sent.ents]
#                 results.append({
#                     "claim": sent.text,
#                     "entities": entities,
#                     "confidence": 0.9,   # tu peux ajuster ou calculer dynamiquement
#                     "label": label
#                 })
#         return results
#
#
# if __name__ == "__main__":
#     text = """
#     The president announced a new reform yesterday.
#     I think it's a good move.
#     The reform has never been approved by Congress.
#     Il est officiellement confirmé que la réforme aura lieu.
#     Je crois que cela est une mauvaise idée.
#     """
#
#     extractor = ClaimExtractor(lang="en")  # ou "fr" pour français
#     claims = extractor.extract_claims(text)
#
#     if claims:
#         for claim in claims:
#             print(claim)
#     else:
#         print("No claims detected.")













import re
import stanza
import emoji

class ClaimExtractor:
    def __init__(self, lang="en"):
        try:
            self.nlp = stanza.Pipeline(lang=lang, processors='tokenize,ner,pos', use_gpu=False)
            self.lang = lang
        except Exception as e:
            raise Exception(f"Stanza pipeline for '{lang}' could not be loaded: {e}")

    def clean_text(self, text):
        text = re.sub(r"http\S+|www\S+", "", text)           # URLs
        text = re.sub(r"@\w+", "", text)                     # Mentions
        text = re.sub(r"#(\w+)", r"\1", text)                # Garde le mot du hashtag
        text = emoji.demojize(text)                          # Emojis → texte
        text = re.sub(r"[^\w\sàâçéèêëîïôûùüÿñæœ.,!?-]", "", text, flags=re.UNICODE)
        text = re.sub(r"\s+", " ", text)                     # Espaces multiples
        return text.strip()

    def is_claim(self, sentence):
        sent_text = sentence.text.lower()
        opinion_starters = [
            "i think", "i believe", "in my opinion", "i feel",
            "je pense", "je crois", "à mon avis"
        ]
        if any(sent_text.startswith(p) for p in opinion_starters):
            return False, "Starts with opinion"

        if len(sentence.text.split()) < 5:
            return False, "Too short"

        has_verb = any(word.upos == "VERB" for word in sentence.words)
        if not has_verb:
            return False, "No verb found"

        has_entity = len(sentence.ents) > 0
        has_number = any(ent.type in [
            "DATE", "TIME", "MONEY", "PERCENT", "QUANTITY", "CARDINAL"
        ] for ent in sentence.ents)

        if has_entity or has_number:
            return True, "Has verb and entity/number"
        return False, "Missing entity/number"

    def classify_claim(self, text):
        text = text.lower()
        keywords = {
            "expressive_false": ["never", "pas du tout", "jamais", "aucun", "impossible", "not confirmed", "rumor", "rumeur"],
            "true": ["confirmed", "announced", "déclaré", "confirmé", "officiel", "official"],
            "expressive_true": ["probably", "likely", "peut-être", "possible", "possible que"]
        }
        for label, kw_list in keywords.items():
            if any(kw in text for kw in kw_list):
                return label
        return "neutral"

    def compute_confidence(self, sentence, label):
        score = 0.5
        if any(word.upos == "VERB" for word in sentence.words):
            score += 0.1
        if len(sentence.ents) > 0:
            score += 0.1
        if label != "neutral":
            score += 0.1
        if len(sentence.text.split()) >= 10:
            score += 0.1
        return min(score, 1.0)

    def extract_claims(self, text):
        results = []
        cleaned = self.clean_text(text)
        doc = self.nlp(cleaned)

        for sent in doc.sentences:
            is_c, reason = self.is_claim(sent)
            if is_c:
                label = self.classify_claim(sent.text)
                confidence = self.compute_confidence(sent, label)
                entities = [ent.text for ent in sent.ents]
                results.append({
                    "claim": sent.text,
                    "entities": entities,
                    "label": label,
                    "confidence": round(confidence, 2),
                    "reason": reason
                })
            else:
                pass
        return results
