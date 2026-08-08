from app.research.matcher import (
    calculate_similarity,
    are_similar,
)


text_a = (
    "Chennai drainage network gaps "
    "were reduced."
)

text_b = (
    "The number of stormwater drainage "
    "gaps in Chennai has decreased."
)

text_c = (
    "The Chennai cricket team won "
    "the match yesterday."
)


similarity_ab = calculate_similarity(
    text_a,
    text_b,
)

similarity_ac = calculate_similarity(
    text_a,
    text_c,
)


print(
    f"Similarity A/B: "
    f"{similarity_ab:.3f}"
)

print(
    f"Similarity A/C: "
    f"{similarity_ac:.3f}"
)

print(
    f"A and B similar: "
    f"{are_similar(text_a, text_b)}"
)

print(
    f"A and C similar: "
    f"{are_similar(text_a, text_c)}"
)