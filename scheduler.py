import schedule
import time
import subprocess


def run(*args):
    return subprocess.check_call(list(args))


def run_script():
    run("python3", "checker.py")


schedule.every().day.at("09:00").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)
