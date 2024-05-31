import requests
import json
from colorama import Fore, Style

# Fungsi untuk registrasi waitlist
def regisRoy(email, walletadd):
    url = "https://api.roybits.com/add-form"

    payload = {
        "email": f"{email}",
        "wallet_address": f"{walletadd}"
    }
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en,en-US;q=0.9,id;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.roybits.com',
        'priority': 'u=1, i',
        'referer': 'https://www.roybits.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        return response.json(), response.status_code
    elif response.status_code == 400:
        return response.json()['message'], response.status_code
    else:
        return response.json(), response.status_code

def main():
    print("     ┎────────────────────────────────────────┓        ")
    print("     ┃    AUTO REGISTRASI ROYBITS WAITLIST    ┃        ")
    print("     ┗────────────────────────────────────────┚        ")
    try:
        # Buka address.txt
        with open('address.txt', 'r') as af:
            address = af.readlines() # read tiap line
            try:
                # Buka email.txt
                with open('email.txt', 'r') as ef:
                    email = ef.readlines() # read tiap line

                    for i in range(len(address)):
                        # print(address[i], email[i])

                        print(Fore.YELLOW + "\n[\] Sedang melakukan registrasi email dan address ke-% s" % (i+1) + Style.RESET_ALL)

                        if i <= len(email):
                            # Registrasi dimulai
                            respon, respon_kode = regisRoy(email[i], address[i])
                            # print(respon, respon_kode)

                            if respon_kode == 201:
                                print(Fore.GREEN + "[+] Berhasil registrasi dengan id % s" % respon['id'] + Style.RESET_ALL)
                                # Save ke results.txt
                                with open('results.txt', 'a+') as rf:
                                    rf.write(f"{email[i].strip()},{address[i].strip()},{respon['id']}\n")
                                rf.close()
                                
                                print(Fore.GREEN + "[+] Berhasil simpan email, address, dan id ke results.txt" + Style.RESET_ALL)
                            elif respon_kode == 400:
                                print(Fore.RED + "[!] Email dan/atau wallet address telah terdaftar" + Style.RESET_ALL)
                                continue
                            else: 
                                print(Fore.RED +"[!] % s - Error" % respon_kode + Style.RESET_ALL)
                                continue
                        else:
                            break
                    ef.close()
            # Jika tidak ada file email.txt
            except FileNotFoundError:
                ef = open('email.txt', 'w')
                ef.writelines("email1@email.com\nemail1@email.com")
                ef.close
                print(Fore.RED +"[!] Silakan lengkapi email.txt terlebih dahulu" + Style.RESET_ALL)
            af.close()
    # Jika tidak ada file address.txt
    except FileNotFoundError:
        af = open('address.txt', 'w')
        af.writelines("solanaaddress1xxxxxxx\nsolanaaddress2xxxxxxx")
        af.close()
        try:
            ef = open('email.txt', 'r')
            ef.close
        # Jika tidak ada file email.txt
        except FileNotFoundError:
            ef = open('email.txt', 'w')
            ef.writelines("email1@email.com\nemail1@email.com")
            ef.close
        print(Fore.RED + "[!] Silakan isi address.txt dan email.txt terlebih dahulu" + Style.RESET_ALL)

if __name__ == "__main__":
    main()