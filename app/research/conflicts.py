from pydantic import BaseModel


class Conflict(BaseModel):

    topic: str
    claims: list[str]
    sources: list[str]


def detect_conflicts(
    claims: list[tuple[str, str, str]],
) -> list[Conflict]:

    conflicts = []

    for i in range(len(claims)):

        topic_a, statement_a, source_a = claims[i]

        for j in range(i + 1, len(claims)):

            topic_b, statement_b, source_b = claims[j]

            if topic_a.lower() != topic_b.lower():
                continue

            if statement_a.lower() == statement_b.lower():
                continue

            conflicts.append(
                Conflict(
                    topic=topic_a,
                    claims=[
                        statement_a,
                        statement_b,
                    ],
                    sources=[
                        source_a,
                        source_b,
                    ],
                )
            )

    return conflicts