# USCIS Case Status Checker

A python script to automatically check your [case status on USCIS](https://egov.uscis.gov/casestatus/landing.do).

## Usage

- Install [Selenium](https://selenium-python.readthedocs.io/) if not already installed.
- Install Chrome's [web driver](https://chromedriver.chromium.org/downloads) that is specific to your Chrome browser's version and provide the path to the web driver in `checker.py`.
- Add your USCIS receipt number in `checker.py`.
- Edit `scheduler.py` to run at certain time intervals.
- Run `scheduler.py`.
