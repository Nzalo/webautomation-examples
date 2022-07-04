from dotenv import load_dotenv
from helium import *
import time
import os
#import slack-bot

def automation_ex1():

    start_chrome(os.environ['WEBADDRESS'])
    click(os.environ['ABTEILUNG'])
    time.sleep(1)

    click('Ich habe den Hinweis gelesen')
    click('Ich bin mit der Speicherung und Verarbeitung meiner Daten einverstanden.')
    click('Weiter')
    time.sleep(1)

    write(os.environ['VORNAME'], into='Vorname')
    write(os.environ['NACHNAME'], into='Nachname')
    write(os.environ['EMAIL'], into='E-Mail')
    click('Weiter')
    time.sleep(1)

    select(ComboBox("0"), "1")
    click('Weiter')
    time.sleep(1)

    click('Termin suchen')
    time.sleep(1)

    click(os.environ['ABTEILUNG'])
    click('Weiter')
    time.sleep(1)

    # if date is earlier than 01.AUGUST then book
    click('Weiter')
    time.sleep(1)

    click('Termin verbindlich vereinbaren')
    time.sleep(1)

    time.sleep(5)
    kill_browser()

if __name__ == "__main__":
    load_dotenv('.env')
    #app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
    automation_ex1()