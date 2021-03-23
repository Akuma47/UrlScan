import requests
import time
import os
import sys
from bs4 import BeautifulSoup 



def scanner():
    arquivo = open(wordlist, 'r')


    for page in arquivo:
        req2 = requests.get(f"{url}{page.strip()}")


        def grabbing():
            content = req2.content
            site = BeautifulSoup(content, 'html.parser')


            lista = (site.text).split()

            numero = len(lista)
            i = 0
            
            while(i < numero):
                x = lista[i].find("Disallow")
                y = lista[i].find('Sitemap')


                i = i+1

                if x == -1:#caso ele não encontre a fase Disallow ele mostrara
                    pass
                elif y == -1:
                    print(f'\u001b[32m  > [Robots.txt] {lista[i+2]}\u001b[0m')
                else:
                    print(f'\u001b[32m  > [Robots.txt] {req.url}{lista[i]}\u001b[0m')
                    continue


        if req2.status_code == 200:
            print(f'\u001b[32m [{req2.status_code}] {req.url}{page}\u001b[0m')
            
            if page.strip() == "robots.txt":
                if req2.status_code == 200:
                    grabbing()
                    
        else:
            print(f'\u001b[31m [{req2.status_code}] {req.url}{page}\u001b[0m')
    



try:
    url = sys.argv[1]
    wordlist = sys.argv[2]
    req = requests.get(url)


    

    if req.status_code == 200:
        os.system('cls')
        
        print(f'\u001b[33m[+] Iniciando scanner em {req.url}\u001b[0m')
        time.sleep(2)

        scanner()
        

    else:
        print('Host não encontrado')
except:
    print('\u001b[31m [+] Impossivel realizar a conexão com o host.\u001b[0m')
    print('\u001b[34m [!] Lembrese de colocar uma url apos a inicialização do programa\u001b[0m')
    


