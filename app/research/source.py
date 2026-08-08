from urllib.parse import urlparse


def get_domain(url: str) -> str:

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def group_by_domain(results):

    groups = {}

    for result in results:

        domain = get_domain(result.url)

        if domain not in groups:
            groups[domain] = []

        groups[domain].append(result)

    return groups