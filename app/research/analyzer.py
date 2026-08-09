import re

from app.research.models import SearchResult, Claim


def clean_text(text: str) -> str:

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_sentences(text: str) -> list[str]:

    text = clean_text(text)

    if not text:
        return []

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text,
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def is_useful_claim(sentence: str) -> bool:

    sentence = sentence.strip()

    if len(sentence) < 30:
        return False

    if len(sentence) > 500:
        return False

    lowered = sentence.lower()

    junk_patterns = [
        # Navigation / website UI
        "read more",
        "subscribe",
        "sign in",
        "login",
        "skip to content",
        "frontpage",
        "contact us",
        "google play",
        "accessibility links",

        # Social / sharing
        "share on",
        "twitter",
        "facebook",
        "whatsapp",
        "reddit",

        # Promotional content
        "looking for more",
        "grab our latest issue",
        "buy now",
        "shop now",
        "click here",
        "download our app",
        "follow us",
        "support us",

        # Newsletter / contact
        "email us",
        "sign up",
        "newsletter",

        # Generic article metadata
        "most popular",
        "related topics",
        "related stories",
        "latest news",
        "published -",
        "updated -",
        "article image for",
        "reported by:",
        "express news service",

        # Podcast / media navigation
        "listen to every episode",
        "transcript",
        "sponsor-free",
    ]

    for pattern in junk_patterns:

        if pattern in lowered:
            return False

    # Remove obvious fragments produced by scraped pages.
    if sentence.startswith("..."):
        return False

    if sentence.startswith("[...]"):
        return False

    # URLs are usually page metadata rather than claims.
    if "http://" in lowered or "https://" in lowered:
        return False

    # Email addresses are not useful research claims.
    if re.search(
        r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b",
        sentence,
    ):
        return False

    # Hashtag-heavy / navigation-like text.
    if sentence.count("#") >= 2:
        return False

    return True


def extract_claims(
    results: list[SearchResult],
) -> list[Claim]:

    claims = []

    for result in results:

        sentences = split_sentences(
            result.snippet
        )

        for sentence in sentences:

            if not is_useful_claim(sentence):
                continue

            claim = Claim(
                statement=sentence,
                sources=[result.url],
                source_title=result.title,
                source_url=result.url,
                confidence=0.0,
            )   

            claims.append(claim)

    return claims