import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser'
    )
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help='Choose language: ru, en, ... (etc.)'
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")
        service = FirefoxService(driver_loc)
        opts = webdriver.FirefoxOptions()
        opts.binary_location = binary_loc
        opts.set_preference("dom.webdriver.enabled", False)
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(service=service, options=opts)
    else:
        raise pytest.UsageError(
            '--browser_name should be chrome or firefox'
        )
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def url_link():
    return 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
