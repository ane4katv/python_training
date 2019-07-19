import pytest
from application import Application


# def is_alert_present(wd):
#     try:
#         wd.switch_to_alert().text
#         return True
#     except:
#         return False


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_run_test(app):
   app.open_page()
   app.login()
   app.logout()
