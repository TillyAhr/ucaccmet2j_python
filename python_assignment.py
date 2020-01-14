import json

with open('precipitation.json', encoding='utf8') as file:
    precipitation_data = json.load(file)

total_precipitation = 0
relative_month_precipitation = []

list_total_monthly_rainfall = [0]*12

# Consider only the dictionnaries about Seatle  
for dictionnary in precipitation_data:
    if dictionnary['station'] == 'GHCND:US1WAKG0038':

        date_str = dictionnary['date']
        month_number = int(date_str[5:7])
        print(month_number)
        rainfall = dictionnary['value']
        list_total_monthly_rainfall[month_number-1] += rainfall
        
        # Add each value to create total precipitation 
        total_precipitation += dictionnary['value']

for month in list_total_monthly_rainfall:
    relative_month_precipitation.append(month/total_precipitation) 

print(list_total_monthly_rainfall)
print(total_precipitation)

output_variable = {
	"Seatle": {
		"station": "GHCND:US1WAKG0038", 
		"state": "WA", 
		"list_total_monthly_rainfall": list_total_monthly_rainfall, 
		"relativeMonthlyPrecipitation": relative_month_precipitation, 
		"total_precipitation": total_precipitation
	},}

with open('output_assignment.json', 'w', encoding='utf8') as file:
    json.dump(output_variable, file, indent=4)

   
                



