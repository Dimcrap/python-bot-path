import requests
import json
import secrets
import pprint

articles=None

def extractUsfulData(artcId):
    artc=None
    #print(type(articles))
    for article in articles:
        if article['article_id']==artcId:
            artc=article
            break
    if artc==None:
        print("Error! didn't find the article")

    articleDict={
        "title":artc ['title'],
        "link":artc ['link'],
        #descreaption
        "creator":artc ['creator'],
        "country":artc ['country'],
        "image":artc ['image_url'],
    }
    return articleDict    
    
def searchbyCategory(category):
    list=[]
    for article in articles:
        #print("articles cats:",article['category'])
        if category in article['category']:
            #print(f"{category} did exists in this article{article['article_id']}")
            list.append(article["article_id"])
    return list
    
def getAarticle(category):
    #print(category.lower())
    Rarticle=None
    catsList=searchbyCategory(category.lower())
    #print(catsList)
    if not catsList:
        print(f"failed to load aticles with '{category}' as category ")
    else:
        Rarticle=secrets.choice(catsList)
    return Rarticle
    
categories=['Domestic','Tourism','World','Environment','Health']
m_url="https://newsdata.io/api/1/latest?apikey=pub_fd65230a260d4cdeafc9fe6568a593fc&category=domestic,tourism,world,environment,health"
responde=requests.get(m_url)
data=None

if responde.status_code!=200:
    print("failed to get newsdata api")
else:
    data=responde.json()

articles=data['results']


print(r"""\                       __.....__                   .     .--.   _..._                          _..._         __.....__                      
||                  .-''         '.               .'|     |__| .'     '.   .--./)             .'     '.   .-''         '.         _     _    
||        .-,.--.  /     .-''"'-.  `.           .'  |     .--..   .-.   . /.''\\             .   .-.   . /     .-''"'-.  `. /\    \\   //    
||  __    |  .-. |/     /________\   \    __   <    |     |  ||  '   '  || |  | |            |  '   '  |/     /________\   \`\\  //\\ //     
||/'__ '. | |  | ||                  | .:--.'.  |   | ____|  ||  |   |  | \`-' /             |  |   |  ||                  |  \`//  \'/ _    
|:/`  '. '| |  | |\    .-------------'/ |   \ | |   | \ .'|  ||  |   |  | /("'`              |  |   |  |\    .-------------'   \|   |/.' |   
||     | || |  '-  \    '-.____...---.`" __ | | |   |/  . |  ||  |   |  | \ '---.            |  |   |  | \    '-.____...---.    '    .   | / 
||\    / '| |       `.             .'  .'.''| | |    /\  \|__||  |   |  |  /'""'.\           |  |   |  |  `.             .'        .'.'| |// 
|/\'..' / | |         `''-...... -'   / /   | |_|   |  \  \   |  |   |  | ||     ||          |  |   |  |    `''-...... -'        .'.'.-'  /  
'  `'-'`  |_|                         \ \._,\ '/'    \  \  \  |  |   |  | \'. __//           |  |   |  |                         .'   \_.'   
                                       `--'  `"'------'  '---''--'   '--'  `'---'            '--'   '--'                                     """)
input("press enter to start ...")

print(f"choose between these categories:\n1-{categories[0]}\n"
      f"2-{categories[1]}\n3-{categories[2]}\n4-{categories[3]}\n5-{categories[4]}")
select=input()
while select.isnumeric()==False or int(select)<1 or int(select)>5:
    print(f"unvalid input!\nchoose between these categories:\n1-{categories[0]}\n"
          f"2-{categories[1]}\n3-{categories[2]}\n4-{categories[3]}\n5-{categories[4]}")
    select=input()

outputarticle=getAarticle((categories[int(select)-1]))
if not outputarticle:
    print(f"no news available with {(categories[int(select)-1])}category")
else:
    pprint.PrettyPrinter(indent=True).pprint(extractUsfulData(outputarticle))
    
