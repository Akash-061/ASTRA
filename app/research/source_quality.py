from urllib.parse import urlparse


HIGH_QUALITY_DOMAINS = {
    "reuters.com",
    "bbc.com",
    "apnews.com",
    "theguardian.com",
    "nytimes.com",
    "washingtonpost.com",
}


GOVERNMENT_SUFFIXES = (
    ".gov",
    ".gov.in",
    ".nic.in",
)


INSTITUTIONAL_SUFFIXES = (
    ".edu",
    ".ac.in",
)


def normalize_domain(
    url: str,
) -> str:

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def calculate_source_quality(
    url: str,
) -> float:

    domain = normalize_domain(url)

    if not domain:
        return 0.0

    if domain in HIGH_QUALITY_DOMAINS:
        return 1.0

    if domain.endswith(
        GOVERNMENT_SUFFIXES
    ):
        return 0.95

    if domain.endswith(
        INSTITUTIONAL_SUFFIXES
    ):
        return 0.90

    return 0.50


def classify_source(
    url: str,
) -> str:

    score = calculate_source_quality(
        url
    )

    if score >= 0.90:
        return "high"

    if score >= 0.70:
        return "medium"

    return "unknown"