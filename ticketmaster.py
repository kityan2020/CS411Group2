import requests
# define API endpoint and parameters
url = 'https://app.ticketmaster.com/discovery/v2/events.json'
api_key = 'qjdg4sTDUGRKNiGaLzjfxwoo3MoSBv0y'
#we can get these from user input and through location
artist_name = input('Artist: ')
location =  input('Location: ')

# make GET request to API endpoint with parameters and API key
response = requests.get(url, params={
    'apikey': api_key,
    'keyword': artist_name,
    'city': location
})
print(response.json())
if response.status_code == 200:
    events = response.json()
    if '_embedded' in events and 'events' in events['_embedded']:
        events = events['_embedded']['events']
        for event in events:
            print('Name:', event['name'])
            print('Date:', event['dates']['start']['localDate'])
            #print('Time:', event['dates']['start']['localTime'])
            print('Venue:', event['_embedded']['venues'][0]['name'])
            print('Location:', event['_embedded']['venues'][0]['city']['name'])
            print('------------------------------')
    else:
        print('No events found')
else:
    print('Error:Request failed with status code', response.status_code)