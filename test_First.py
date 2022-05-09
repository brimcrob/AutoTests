import pytest




@pytest.mark.smoke
def test_login():
    print("Log in to the Application")


@pytest.mark.regression
def test_add_product():
    print('add product')


@pytest.mark.smoke
def test_logout():
    print('log out')
