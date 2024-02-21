from colorama import init, Fore
import os
import time
import json
import re
import discord
import asyncio
import aiohttp
import urllib.request
from urllib.request import Request, urlopen

# coloramaの初期化
init(autoreset=True)

# here is end and more thing
def cleartheline():
    os.system('cls')

def is_valid_webhook_link(webhook_link):
    pattern = r"https://discord.com/api/webhooks/.+"
    if re.match(pattern, webhook_link):
        return True
    else:
        return False

def addwebhooknew():
    print(f"{Fore.MAGENTA}𝕡𝕝𝕖𝕒𝕤𝕖 𝕚𝕟𝕡𝕦𝕥 𝕨𝕖𝕓𝕙𝕠𝕠𝕜 𝕝𝕚𝕟𝕜...\n")
    wblinkn = input(f"{Fore.MAGENTA}")
    if is_valid_webhook_link(wblinkn):
        save_webhook(wblinkn)
    else:
        print(f"{Fore.MAGENTA}𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕨𝕖𝕓𝕙𝕠𝕠𝕜 𝕝𝕚𝕟𝕜 𝕗𝕠𝕣𝕞𝕒𝕥. ℙ𝕝𝕖𝕒𝕤𝕖 𝕖𝕟𝕥𝕖𝕣 𝕒 𝕧𝕒𝕝𝕚𝕕 𝕨𝕖𝕓𝕙𝕠𝕠𝕜 𝕝𝕚𝕟𝕜.")
        addwebhooknew()
    end()

def save_webhook(webhook_link):
    try:
        with open("webhook.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    if len(data) == 1:
        print(f"{Fore.MAGENTA}𝕐𝕠𝕦 𝕙𝕒𝕧𝕖 𝕒𝕝𝕣𝕖𝕒𝕕𝕪 𝕒𝕕𝕕𝕖𝕕 𝕒 𝕨𝕖𝕓𝕙𝕠𝕠𝕜. 𝔻𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝕥𝕠 𝕔𝕙𝕒𝕟𝕘𝕖 𝕥𝕙𝕖 𝕨𝕖𝕓𝕙𝕠𝕠𝕜 𝕌ℝ𝕃? 𝕪/𝕟")
        change = input()
        if change.lower() == "y":
            data = [webhook_link]
            with open("webhook.json", "w") as file:
                json.dump(data, file)
            print(f"{Fore.MAGENTA}𝕎𝕖𝕓𝕙𝕠𝕠𝕜 𝕌ℝ𝕃 𝕙𝕒𝕤 𝕓𝕖𝕖𝕟 𝕔𝕙𝕒𝕟𝕘𝕖𝕕 𝕤𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪.")
            return
        else:
            print(f"{Fore.MAGENTA}𝕆𝕡𝕖𝕣𝕒𝕥𝕚𝕠𝕟 𝕔𝕒𝕟𝕔𝕖𝕝𝕝𝕖𝕕.")
            return

    data.append(webhook_link)

    with open("webhook.json", "w") as file:
        json.dump(data, file)

    print(f"{Fore.MAGENTA}𝕎𝕖𝕓𝕙𝕠𝕠𝕜 𝕝𝕚𝕟𝕜 𝕙𝕒𝕤 𝕓𝕖𝕖𝕟 𝕤𝕒𝕧𝕖𝕕 𝕤𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪.")

def get_webhook_url_from_json(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            if isinstance(data, list) and data:  # リストであり、かつ空でない場合
                return data[0]  # リストの最初の要素を返す
            else:
                print(f"{Fore.MAGENTA}𝕨𝕖𝕓𝕙𝕠𝕠𝕜.𝕛𝕤𝕠𝕟 𝕚𝕤 𝕖𝕞𝕡𝕥𝕪")
                print(f"{Fore.MAGENTA}𝕓𝕒𝕔𝕜 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
                cleartheline()
                main()
    except FileNotFoundError:
        print(f"{Fore.MAGENTA}𝕔𝕒𝕟'𝕥 𝕗𝕚𝕟𝕕 𝕨𝕖𝕓𝕙𝕠𝕠𝕜.𝕛𝕤𝕠𝕟")
        print(f"{Fore.MAGENTA}𝕓𝕒𝕔𝕜 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
        cleartheline()
        main()
    except json.JSONDecodeError:
        print(f"{Fore.MAGENTA}𝕨𝕖𝕓𝕙𝕠𝕠𝕜.𝕛𝕤𝕠𝕟 𝕚𝕤 𝕚𝕟𝕧𝕒𝕝𝕚𝕕")
        print(f"{Fore.MAGENTA}𝕓𝕒𝕔𝕜 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
        cleartheline()
        main()


def post_discord(message: str, webhook_url: str):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    data = {"content": message}
    request = Request(
        webhook_url,
        data=json.dumps(data).encode(),
        headers=headers,
    )

    try:
        with urlopen(request) as res:
            assert res.getcode() == 204
            print("𝕋𝕖𝕤𝕥𝕚𝕟𝕘 𝕀𝕤 ℂ𝕠𝕞𝕡𝕝𝕖𝕥𝕖𝕕!!")
            end()
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print(f"{Fore.MAGENTA}𝕖𝕣𝕣𝕠𝕣 𝕚𝕟 𝕦𝕣𝕝. 𝕔𝕙𝕖𝕔𝕜 𝕦𝕣𝕝 𝕚𝕤 𝕧𝕒𝕝𝕚𝕕")
            print(f"{Fore.MAGENTA}𝕓𝕒𝕔𝕜 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
            cleartheline()
            main()
        else:
            print(f"{Fore.MAGENTA}𝕖𝕣𝕣𝕠𝕣 𝕙𝕒𝕡𝕡𝕖𝕟𝕕: {e}")
            print(f"{Fore.MAGENTA}𝕓𝕒𝕔𝕜 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
            cleartheline()
            main()


def end():
    print(f"{Fore.MAGENTA}𝔻𝕠 𝕪𝕠𝕦 𝕨𝕒𝕟𝕥 𝔹𝕒𝕔𝕜 𝕥𝕠 𝕊𝕥𝕒𝕣𝕥 𝕞𝕖𝕟𝕦? 𝕪/𝕟")
    rmain = input(f"{Fore.MAGENTA}")
    if rmain == "y":
        cleartheline()
        main()
    elif rmain == "n":
        exit()
    else:
        print(f"{Fore.MAGENTA}𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕒𝕟𝕤𝕨𝕖𝕣")
        end()

# end and more thing is end


ascii_art = (
    " ____  _    _   _ ____    _   _ _   _____ ____      _    \n"
    " |  _ \\| |  | | | / ___|  | | | | | |_   _|  _ \\    / \\   \n"
    " | |_) | |  | | | \\___ \\  | | | | |   | | | |_) |  / _ \\  \n"
    " |  __/| |__| |_| |___) | | |_| | |___| | |  _ <  / ___ \\ \n"
    " |_|   |_____\\___/|____/   \\___/|_____|_| |_| \\_\\/_/   \\_\\ \n"
)

inputconfig = (
    "𝟙. 𝔸𝕕𝕕 𝔻𝕚𝕤𝕔𝕠𝕣𝕕 𝕎𝕖𝕓𝕙𝕠𝕠𝕜 𝕝𝕚𝕟𝕜𝕤 \n"
    "𝟚. ℂ𝕙𝕖𝕔𝕜 𝕎𝕖𝕓𝕙𝕠𝕠𝕜 𝕄𝕠𝕧𝕚𝕟𝕘 \n"
    "𝟛. 𝕀ℙ 𝕃𝕆𝔾𝔾𝔼ℝ(𝔾ℝ𝔸𝔹𝕀𝔽𝕐) \n"
    "𝟜. ℝ𝕆𝔹𝕃𝕆𝕏 𝕃𝕆𝔾𝔾𝔼ℝ \n"
    "𝟝. ℙℍ𝕆𝕋𝕆 𝕃𝕆𝔾𝔾𝔼ℝ \n"
    "𝟞. 𝔼𝕩𝕚𝕥 ℙ𝕣𝕠𝕘𝕣𝕒𝕞 \n"
)

purple_ascii_art = Fore.MAGENTA + ascii_art
inputconfigfp = Fore.MAGENTA +  inputconfig

def main():
    print(purple_ascii_art)
    print(f"{Fore.MAGENTA}𝕄𝔸𝔻𝔼 𝔹𝕐 𝕘𝕖𝕟 & 𝕤𝕦𝕡𝕡𝕒𝕞𝕒𝕟\n")
    print("\n")
    print(inputconfigfp)
    print(f"{Fore.MAGENTA}𝔼𝕟𝕥𝕖𝕣 𝕪𝕠𝕦𝕣 𝕟𝕦𝕞𝕓𝕖𝕣:")
    mode = input(f"{Fore.MAGENTA}")
    if mode == "1":
        cleartheline()
        addwebhooknew()
    elif mode == "2":
        webhook_url = get_webhook_url_from_json("webhook.json")
        if webhook_url:
            post_discord('🆃🅴🆂🆃🅴🅳❗ - ℙ𝕃𝕌𝕊 𝕌𝕃𝕋ℝ𝔸', webhook_url)
        else:
            print(f"{Fore.MAGENTA}𝕎𝕖 𝕔𝕒𝕟𝕥 𝕘𝕖𝕥 𝕎𝕖𝕓𝕙𝕠𝕠𝕜 𝕌ℝ𝕃")
            cleartheline()
            main()
    elif mode == "3":
        print("selected 3")
    elif mode == "4":
        print("selected 4")
    elif mode == "5":
        print("selected 5")
    elif mode == "6":
        print(f"{Fore.MAGENTA}𝕖𝕩𝕚𝕥 𝕒𝕗𝕥𝕖𝕣 𝟙 𝕤𝕖𝕔")
        time.sleep(1)
        exit() 
    else:
       print(f"{Fore.MAGENTA}𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕒𝕟𝕤𝕨𝕖𝕣")
       main()

main()