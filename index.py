import requests

def BingDorker():
    dorklist = input('Dork list : ')
    file = open(dorklist, 'r').read().split("\n")
    
    pagescrape = input('Page : ')

    count = 1

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}

    for index in file:
        if index == '':
            continue
        for i in range(0, int(pagescrape)):
            domains = []
            
            bing = "https://www.bing.com/search?q=" + index +"&first=" + str(i)
            count +=10
            page = requests.get(bing, headers=headers).text
            find = page.split('<li class="b_algo"><h2><a href="')

            for k in range(0, 10):
                try:
                    domains.append(find[k+1].split('"')[0])
                    print ('[+]',(find[k+1].split('"')[0]))
                    
                except:
                    pass
                
            for res in domains:
                open('bing_result.txt', 'a').close()
                res = res.split('/')
                with open('bing_result.txt', 'a') as b:
                    b.writelines((res[0]+'//'+res[2])+'\n')

def GoogleDorker():
    dorklist = input('Dork list : ')
    file = open(dorklist, 'r').read().split("\n")
    
    pagescrape = input('Page : ')

    count = 1

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}
    
    
    for index in file:
        if index == "":
            continue
        for i in range(0, int(pagescrape)):
            domains = []

            google = "https://www.google.com/search?q=" + index +"&start=" + str(i)
            count +=10
            try:    
                page = requests.get(google, headers=headers).text
            except:
                pass
            find = page.split('<div class="yuRUbf"><a href="')

            for k in range(0, 10):
                try:
                    domains.append(find[k+1].split('"')[0])
                    print ('[+]',(find[k+1].split('"')[0]))
                except:
                    pass
            
            for res in domains:
                open('google_result.txt', 'a').close()
                res = res.split('/')
                with open('google_result.txt', 'a') as b:
                    b.writelines((res[0]+'//'+res[2])+'\n')

def remove():
    inp = input('Result list : ')
    temp = []
    file = open(inp, 'r+')
    temp.extend(file.read().split('\n'))
    temp = list(set(temp))
    file.truncate(0)
    for i in temp:
        open(inp, 'a').close()
        with open(inp, 'a') as b:
            b.writelines((i) + '\n')

def main():
    print(' 1. Google Dorker')
    print(' 2. Bing Dorker')
    print(' 3. Remove Duplicate')
    inp = int(input(" Pilih : "))
    if inp == 1:
        GoogleDorker()
    elif inp == 2:
        BingDorker()
    elif inp == 3:
        remove()
    else:
        print('nomor hanya 1-3')

if __name__ == "__main__":
    main()