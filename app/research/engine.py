from app.research.query import build_research_query
from app.research.request import ResearchRequest
from app.research.search import search_web
from app.research.analyzer import extract_claims
from app.research.relevance import (
    is_contextually_relevant,
)
from app.research.verifier import verify_claims
from app.research.synthesis import synthesize_answer


def run_research(
    request: ResearchRequest,
):

    query = build_research_query(
        request
    )

    results = search_web(
        query
    )

    if not results:

        return {
            "success": False,
            "message": (
                "No research results found."
            ),
            "data": {
                "query": query,
            },
        }

    claims = extract_claims(
        results
    )

    if not claims:

        return {
            "success": False,
            "message": (
                "No useful claims found."
            ),
            "data": {
                "query": query,
                "sources": len(results),
            },
        }

    relevant_claims = []

    for claim in claims:

        if is_contextually_relevant(
            request,
            claim,
        ):

            relevant_claims.append(
                claim
            )

    if not relevant_claims:

        return {
            "success": False,
            "message": (
                "No relevant claims found."
            ),
            "data": {
                "query": query,
                "sources": len(results),
                "claims": len(claims),
            },
        }

    evidence_groups = verify_claims(
        relevant_claims
    )

    if not evidence_groups:

        return {
            "success": False,
            "message": (
                "No verified evidence found."
            ),
            "data": {
                "query": query,
                "claims": len(
                    relevant_claims
                ),
            },
        }

    answer = synthesize_answer(
        query,
        evidence_groups,
    )

    return {
        "success": True,
        "message": answer,
        "data": {
            "query": query,
            "sources": len(results),
            "claims": len(claims),
            "relevant_claims": len(
                relevant_claims
            ),
            "evidence_groups": (
                evidence_groups
            ),
        },
    }