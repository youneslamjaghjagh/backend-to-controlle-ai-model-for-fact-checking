# claim_analyzer.py

import spacy
from app.utils.text_processor import clean_text
from app.services.external_api_client import query_fact_check_api
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

class ClaimAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def extract_claims(self, text: str):
        cleaned = clean_text(text)
        doc = nlp(cleaned)
        claims = []

        for sent in doc.sents:
            if self.is_verifiable_claim(sent.text):
                entities = [ent.text for ent in sent.ents]
                claims.append({
                    "claim_text": sent.text,
                    "entities": entities
                })
        return claims

    def is_verifiable_claim(self, sentence: str):
        keywords = ["affirme", "prétend", "selon", "%", "cause", "rapporte", "a déclaré"]
        return any(keyword in sentence.lower() for keyword in keywords)

    def verify_claim(self, claim):
        api_response = query_fact_check_api(claim["claim_text"])

        if api_response and api_response.get("verdict"):
            verdict = api_response["verdict"]
            explanation = api_response.get("explanation", "")
            source = api_response.get("source", "unknown")
            confidence = api_response.get("confidence", 0.8)
        else:
            verdict = "UNVERIFIED"
            explanation = "No matching verification found."
            source = None
            confidence = 0.3

        return {
            "claim_text": claim["claim_text"],
            "verdict": verdict,
            "confidence": confidence,
            "source": source,
            "explanation": explanation,
            "entities": claim["entities"]
        }

    def analyze(self, text):
        claims = self.extract_claims(text)
        results = []
        for claim in claims:
            result = self.verify_claim(claim)
            results.append(result)
        return results
