import app.modules.system as system


original_get_system_info = (
    system.get_system_info
)


system.get_system_info = lambda: {
    "cpu": 25.5,
    "ram": 60.2,
    "time": "12:30 PM",
}


cpu_result = system.handle_system_command(
    "cpu"
)

assert cpu_result["success"] is True

assert (
    cpu_result["message"]
    == "CPU Usage: 25.5%"
)

assert (
    cpu_result["data"]["cpu"]
    == 25.5
)


ram_result = system.handle_system_command(
    "ram"
)

assert (
    ram_result["message"]
    == "RAM Usage: 60.2%"
)


time_result = system.handle_system_command(
    "time"
)

assert (
    time_result["message"]
    == "Current Time: 12:30 PM"
)


unknown_result = (
    system.handle_system_command(
        "battery"
    )
)

assert unknown_result["success"] is False


system.get_system_info = (
    original_get_system_info
)


print("SYSTEM MODULE PASSED")