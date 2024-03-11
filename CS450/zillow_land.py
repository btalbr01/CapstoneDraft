#Imports for web scraping and pandas DataFrames
import requests
import pandas as pd

#Output from a website that converts curl commands to Python from the scraped website
cookies = {
    'zguid': '24|%240315aaad-95c6-414d-bd1e-1de6f3465f41',
    'zjs_anonymous_id': '%220315aaad-95c6-414d-bd1e-1de6f3465f41%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%22271b59a0-608d-4fa4-8ad5-f648f5ccf718%22',
    '_ga': 'GA1.2.1343471.1709652208',
    '_pxvid': '51e8fee4-db04-11ee-bbb7-c6d91f170a41',
    '_gcl_au': '1.1.825464755.1709652212',
    '_pin_unauth': 'dWlkPVpXVXpOek13TUdZdFpUazJNUzAwWkRreUxUaGxOV1F0WW1GbE1qVTNaVGc1WWpGbA',
    '__pdst': 'b238344703374409892a97855954d2ab',
    '_fbp': 'fb.1.1709652213088.232235615',
    '_gac_UA-21174015-56': '1.1709658528.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE',
    '_gcl_aw': 'GCL.1709658534.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE',
    '_gid': 'GA1.2.384826633.1709777948',
    '_clck': 'kkds9a%7C2%7Cfjx%7C0%7C1525',
    'zgsession': '1|1c93602c-1455-4695-926c-0120169676fb',
    'JSESSIONID': '495C01BC0EC1BD695CD5C9FF87C59A6F',
    'DoubleClickSession': 'true',
    'g_state': '{"i_p":1710003679570,"i_l":1}',
    'tfpsi': '1aeabf51-9cea-425e-a204-ae08099f3429',
    '__gads': 'ID=ab6ab78f906b6bb6:T=1709652222:RT=1709996481:S=ALNI_Mb6rXnjHijhQBbZt2GM8ZtszFS0rQ',
    '__gpi': 'UID=00000dcf74664daf:T=1709652222:RT=1709996481:S=ALNI_MYKR6I6-lDb5bmRBTp7rvJlMLQyTg',
    '__eoi': 'ID=78a45794c5d02e2e:T=1709652222:RT=1709996481:S=AA-Afjbr6n0Qql_XH2Lcg3StOTvC',
    'pxcts': 'ef3afb64-de25-11ee-8be6-0fd22f55a2f8',
    '_hp2_id.1215457233': '%7B%22userId%22%3A%225423646040404048%22%2C%22pageviewId%22%3A%228397065885375307%22%2C%22sessionId%22%3A%221828038325749735%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    '_hp2_ses_props.1215457233': '%7B%22r%22%3A%22https%3A%2F%2Fwww.zillow.com%2Fmonticello-ky%2F%3FsearchQueryState%3D%257B%2522pagination%2522%253A%257B%257D%252C%2522isMapVisible%2522%253Atrue%252C%2522mapBounds%2522%253A%257B%2522west%2522%253A-84.90001340820312%252C%2522east%2522%253A-84.68852659179687%252C%2522south%2522%253A36.74679565717883%252C%2522north%2522%253A36.87433591690353%257D%252C%2522regionSelection%2522%253A%255B%257B%2522regionId%2522%253A46590%252C%2522regionType%2522%253A6%257D%255D%252C%2522filterState%2522%253A%257B%2522sort%2522%253A%257B%2522value%2522%253A%2522globalrelevanceex%2522%257D%252C%2522price%2522%253A%257B%2522min%2522%253A500000%252C%2522max%2522%253Anull%257D%252C%2522mp%2522%253A%257B%2522min%2522%253A2488%252C%2522max%2522%253Anull%257D%257D%252C%2522isEntirePlaceForRent%2522%253Atrue%252C%2522isRoomForRent%2522%253Afalse%252C%2522isListVisible%2522%253Atrue%252C%2522mapZoom%2522%253A12%257D%22%2C%22ts%22%3A1709996500515%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D',
    '_gat': '1',
    '_pxff_cc': 'U2FtZVNpdGU9TGF4Ow==',
    '_pxff_cfp': '1',
    '_pxff_bsco': '1',
    'AWSALB': '7qY8uJ2UcdcxdNnQaIAEslOQ5YVVT8HpU4xuUpCrplZNusnyb4z+j7IwuwZ920MIzqfDJ79QVb1amis2bwtrSHqJWioVqC0aObYnxK6MWiVuS0jQtakQz8bZzh1J',
    'AWSALBCORS': '7qY8uJ2UcdcxdNnQaIAEslOQ5YVVT8HpU4xuUpCrplZNusnyb4z+j7IwuwZ920MIzqfDJ79QVb1amis2bwtrSHqJWioVqC0aObYnxK6MWiVuS0jQtakQz8bZzh1J',
    '_px3': '058e6e3102b9452f9167ce918860c58322b784715f3f9013b1feb3797fb57a0e:7mrAXkhmR+LWql2GNrU/Dvzop7cOQ2EdWKscuP0mBsT/RE4y7lNuiSLeTQE2ez+tYS+9bS1uRnGTWxG92no3Ew==:1000:abHLqEW/FEndbNlBtVri+ACzHy9h5ntaNU6U8abIrDbQGSdmye61VSA+G2TN5J1N6+W+XnJWKt/ntTMXA9f9WN1pHFzBehkVJFg1JrkOD3ZWppW+OwBGsDCLia0p7UUTzaBRVY081Of9ExXPXW5jC35XjjqWoMS/29rLLz9wzRS17ocWg9bLKV547iRyMoD9X+TWt1pmpB8m1cnTDmeYug+/1JGjLX2PVzYv0XaX3Jo=',
    'search': '6|1712588571184%7Crect%3D37.04780932906671%2C-84.3907543671875%2C36.53753242023184%2C-85.2367016328125%26rid%3D76402%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26type%3Dland%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0976402%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    'x-amz-continuous-deployment-state': 'AYABeEnaZE71yWjVhi2dgjgC3HoAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADMYk5CJvh8o6KgqpRAAwCz+t%2F206O9L4dajj28JqX+1iKjDQ62UtRwrpG3kkCIU7bAyAHAiV5Blf9XRKrto3AgAAAAAMAAQAAAAAAAAAAAAAAAAAAHurPxTiz6otaJ8eBhl3juf%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxCSHzvg+Zu0MMcoYQ28wr9gHQgDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCP',
    '_uetsid': 'bd374130ddcd11eeacadbf31f560c2a5',
    '_uetvid': '53b9ab20db0411eeb84d73342c1e20e6',
    '_clsk': '1l0z1nd%7C1709996573480%7C12%7C0%7Cs.clarity.ms%2Fcollect',
}

headers = {
    'authority': 'www.zillow.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'zguid=24|%240315aaad-95c6-414d-bd1e-1de6f3465f41; zjs_anonymous_id=%220315aaad-95c6-414d-bd1e-1de6f3465f41%22; zjs_user_id=null; zg_anonymous_id=%22271b59a0-608d-4fa4-8ad5-f648f5ccf718%22; _ga=GA1.2.1343471.1709652208; _pxvid=51e8fee4-db04-11ee-bbb7-c6d91f170a41; _gcl_au=1.1.825464755.1709652212; _pin_unauth=dWlkPVpXVXpOek13TUdZdFpUazJNUzAwWkRreUxUaGxOV1F0WW1GbE1qVTNaVGc1WWpGbA; __pdst=b238344703374409892a97855954d2ab; _fbp=fb.1.1709652213088.232235615; _gac_UA-21174015-56=1.1709658528.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE; _gcl_aw=GCL.1709658534.CjwKCAiAopuvBhBCEiwAm8jaMUiYCwCrEd4-Yzj2agBgR1HXx9RTJ0HloCRQjLoVhqjHveBYdUEZFRoCGVMQAvD_BwE; _gid=GA1.2.384826633.1709777948; _clck=kkds9a%7C2%7Cfjx%7C0%7C1525; zgsession=1|1c93602c-1455-4695-926c-0120169676fb; JSESSIONID=495C01BC0EC1BD695CD5C9FF87C59A6F; DoubleClickSession=true; g_state={"i_p":1710003679570,"i_l":1}; tfpsi=1aeabf51-9cea-425e-a204-ae08099f3429; __gads=ID=ab6ab78f906b6bb6:T=1709652222:RT=1709996481:S=ALNI_Mb6rXnjHijhQBbZt2GM8ZtszFS0rQ; __gpi=UID=00000dcf74664daf:T=1709652222:RT=1709996481:S=ALNI_MYKR6I6-lDb5bmRBTp7rvJlMLQyTg; __eoi=ID=78a45794c5d02e2e:T=1709652222:RT=1709996481:S=AA-Afjbr6n0Qql_XH2Lcg3StOTvC; pxcts=ef3afb64-de25-11ee-8be6-0fd22f55a2f8; _hp2_id.1215457233=%7B%22userId%22%3A%225423646040404048%22%2C%22pageviewId%22%3A%228397065885375307%22%2C%22sessionId%22%3A%221828038325749735%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.zillow.com%2Fmonticello-ky%2F%3FsearchQueryState%3D%257B%2522pagination%2522%253A%257B%257D%252C%2522isMapVisible%2522%253Atrue%252C%2522mapBounds%2522%253A%257B%2522west%2522%253A-84.90001340820312%252C%2522east%2522%253A-84.68852659179687%252C%2522south%2522%253A36.74679565717883%252C%2522north%2522%253A36.87433591690353%257D%252C%2522regionSelection%2522%253A%255B%257B%2522regionId%2522%253A46590%252C%2522regionType%2522%253A6%257D%255D%252C%2522filterState%2522%253A%257B%2522sort%2522%253A%257B%2522value%2522%253A%2522globalrelevanceex%2522%257D%252C%2522price%2522%253A%257B%2522min%2522%253A500000%252C%2522max%2522%253Anull%257D%252C%2522mp%2522%253A%257B%2522min%2522%253A2488%252C%2522max%2522%253Anull%257D%257D%252C%2522isEntirePlaceForRent%2522%253Atrue%252C%2522isRoomForRent%2522%253Afalse%252C%2522isListVisible%2522%253Atrue%252C%2522mapZoom%2522%253A12%257D%22%2C%22ts%22%3A1709996500515%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _gat=1; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; AWSALB=7qY8uJ2UcdcxdNnQaIAEslOQ5YVVT8HpU4xuUpCrplZNusnyb4z+j7IwuwZ920MIzqfDJ79QVb1amis2bwtrSHqJWioVqC0aObYnxK6MWiVuS0jQtakQz8bZzh1J; AWSALBCORS=7qY8uJ2UcdcxdNnQaIAEslOQ5YVVT8HpU4xuUpCrplZNusnyb4z+j7IwuwZ920MIzqfDJ79QVb1amis2bwtrSHqJWioVqC0aObYnxK6MWiVuS0jQtakQz8bZzh1J; _px3=058e6e3102b9452f9167ce918860c58322b784715f3f9013b1feb3797fb57a0e:7mrAXkhmR+LWql2GNrU/Dvzop7cOQ2EdWKscuP0mBsT/RE4y7lNuiSLeTQE2ez+tYS+9bS1uRnGTWxG92no3Ew==:1000:abHLqEW/FEndbNlBtVri+ACzHy9h5ntaNU6U8abIrDbQGSdmye61VSA+G2TN5J1N6+W+XnJWKt/ntTMXA9f9WN1pHFzBehkVJFg1JrkOD3ZWppW+OwBGsDCLia0p7UUTzaBRVY081Of9ExXPXW5jC35XjjqWoMS/29rLLz9wzRS17ocWg9bLKV547iRyMoD9X+TWt1pmpB8m1cnTDmeYug+/1JGjLX2PVzYv0XaX3Jo=; search=6|1712588571184%7Crect%3D37.04780932906671%2C-84.3907543671875%2C36.53753242023184%2C-85.2367016328125%26rid%3D76402%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26type%3Dland%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0976402%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; x-amz-continuous-deployment-state=AYABeEnaZE71yWjVhi2dgjgC3HoAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADMYk5CJvh8o6KgqpRAAwCz+t%2F206O9L4dajj28JqX+1iKjDQ62UtRwrpG3kkCIU7bAyAHAiV5Blf9XRKrto3AgAAAAAMAAQAAAAAAAAAAAAAAAAAAHurPxTiz6otaJ8eBhl3juf%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxCSHzvg+Zu0MMcoYQ28wr9gHQgDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCPDqwdAGLNueCP; _uetsid=bd374130ddcd11eeacadbf31f560c2a5; _uetvid=53b9ab20db0411eeb84d73342c1e20e6; _clsk=1l0z1nd%7C1709996573480%7C12%7C0%7Cs.clarity.ms%2Fcollect',
    'origin': 'https://www.zillow.com',
    'referer': 'https://www.zillow.com/monticello-ky-42633/land/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-85.2367016328125%2C%22east%22%3A-84.3907543671875%2C%22south%22%3A36.53753242023184%2C%22north%22%3A37.04780932906671%7D%2C%22usersSearchTerm%22%3A%2242633%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A76402%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22max%22%3Anull%7D%2C%22mp%22%3A%7B%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

json_data = {
    'searchQueryState': {
        'pagination': {},
        'isMapVisible': False,
        'mapBounds': {
            'west': -85.2367016328125,
            'east': -84.3907543671875,
            'south': 36.53753242023184,
            'north': 37.04780932906671,
        },
        'usersSearchTerm': '42633',
        'regionSelection': [
            {
                'regionId': 76402,
                'regionType': 7,
            },
        ],
        'filterState': {
            'sortSelection': {
                'value': 'globalrelevanceex',
            },
            'price': {
                'min': None,
                'max': None,
            },
            'monthlyPayment': {
                'min': None,
                'max': None,
            },
            'isSingleFamily': {
                'value': False,
            },
            'isTownhouse': {
                'value': False,
            },
            'isMultiFamily': {
                'value': False,
            },
            'isCondo': {
                'value': False,
            },
            'isAllHomes': {
                'value': True,
            },
            'isApartment': {
                'value': False,
            },
            'isManufactured': {
                'value': False,
            },
            'isApartmentOrCondo': {
                'value': False,
            },
        },
        'isListVisible': True,
    },
    'wants': {
        'cat1': [
            'listResults',
        ],
        'cat2': [
            'total',
        ],
    },
    'requestId': 3,
    'isDebugRequest': False,
}

response = requests.put('https://www.zillow.com/async-create-search-page-state', cookies=cookies, headers=headers, json=json_data)

results_json = response.json()

result_items = results_json['cat1']['searchResults']['listResults']

#Arrays for the relevant columns to be made
address = []
price = []
area = []
url = []
propertyType = []
measurement = []

#For loop to fill each array
for result in result_items:
 address.append(result['addressStreet'])
 price.append(result['unformattedPrice'])
 area.append(result['hdpData']['homeInfo']['lotAreaValue'])
 url.append(result['detailUrl'])
 propertyType.append(result['hdpData']['homeInfo']['homeType'])
 #Column to specify unit of measurment
 measurement.append("acres")

#Creating a DataFrame 
 zillow_land_df = pd.DataFrame({'Address':address, 'Price':price, 'Area':area, 'Measurement':measurement,'Property Type':propertyType, 'URL':url})

#Saving the DataFrame to a .csv
zillow_land_df.to_csv('zillow_land.csv', index=False)