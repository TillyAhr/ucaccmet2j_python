import json

with open('precipitation.json', encoding='utf8') as file:
    precipitation_data = json.load(file)

total_precipitation = 0

# Consider only the dictionnaries about Seatle  
for dictionnary in precipitation_data:
    if dictionnary['station'] == 'GHCND:US1WAKG0038':

        
        
        
        # Add each value to create total precipitation 
        total_precipitation += dictionnary['value']
print(total_precipitation)


   
                



#        january_precipitation = [dictionnary['value']]
