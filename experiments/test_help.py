import app.modules.help as help_module


result = help_module.show_help()


assert result["success"] is True

assert (
    "cpu"
    in result["message"]
)

assert (
    "ram"
    in result["message"]
)

assert (
    "open calculator"
    in result["message"]
)


print("HELP MODULE PASSED")