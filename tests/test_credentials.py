from bugmenot.core import get_credentials


def test_get_credentials():
    website = "https://login.oracle.com/mysso/signon.jsp"
    credentials_list = get_credentials(website)

    assert len(credentials_list) > 0
    credentials = credentials_list[0]
    assert "username" in credentials
    assert "password" in credentials
    assert "success_rate" in credentials
    assert "votes" in credentials
    assert "age" in credentials

    assert "@" in credentials.get("username")
    assert credentials.get("username")
