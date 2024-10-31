import requests
username = input("Username: ")
url = "https://codeforces.com/api/user.rating?handle="+username
response = requests.get(url)
#print(url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    id = data['result']
    maximum = id[0]['newRating']
    
    print("Number of contest Given:",len(id))
    for i in range(0, len(id)):
        if id[i]['newRating'] > maximum:
            maximum = id[i]['newRating']
    print("Highest Rating:",maximum)
    print("Current Rating:", id[len(id)-1]['newRating'])
else:
    print(f"Failed to retri eve data. Status code: {response.status_code}")
