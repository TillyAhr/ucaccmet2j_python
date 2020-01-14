import json

with open('precipitation.json', encoding='utf8') as file:
    precipitation_data = json.load(file)

total_precipitation = 0
january_precipitation = 0
february_precipitation = 0 

list_total_monthly_rainfall = [0]*12

# Consider only the dictionnaries about Seatle  
for dictionnary in precipitation_data:
    if dictionnary['station'] == 'GHCND:US1WAKG0038':

        date_str = dictionnary['date']
        month = int(date_str[5:7])
        print(month)
        rainfall = dictionnary['value']
        list_total_monthly_rainfall[month-1] += rainfall
        
        # Add each value to create total precipitation 
        total_precipitation += dictionnary['value']

print(list_total_monthly_rainfall)
print(total_precipitation)

with open('precipitation.json', 'w', encoding='utf8') as file:
    json.dump(list_total_monthly_rainfall, file)

   
                



