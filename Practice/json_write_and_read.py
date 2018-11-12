import json

data = {}

data['people'] = []

data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt','w') as file:

    newstr = json.dumps(data, indent=4)
    # newstr = json.dumps(data,sort_keys=True, indent=4) -- # If you want to sort the keys in json the use 'sort_keys=True'
    file.write(newstr)



