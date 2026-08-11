import app.modules.apps as apps


original_apps = apps.APPS
original_startfile = apps.os.startfile


apps.APPS = {
    "testapp": "C:\\fake\\testapp.lnk"
}


apps.os.startfile = lambda path: None


result = apps.open_application(
    "open testapp"
)


assert result["success"] is True

assert (
    result["message"]
    == "Opening Testapp..."
)

assert (
    result["application"]
    == "testapp"
)


apps.APPS = original_apps
apps.os.startfile = original_startfile


print("APPS MODULE PASSED")