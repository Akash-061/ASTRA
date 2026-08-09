from app.core.router import resolve_capability


assert (
    resolve_capability("open")
    is not None
)

assert (
    resolve_capability("system")
    is not None
)

assert (
    resolve_capability("research")
    is not None
)

assert (
    resolve_capability("help")
    is not None
)

assert (
    resolve_capability("unknown")
    is None
)


print("ROUTER PASSED")