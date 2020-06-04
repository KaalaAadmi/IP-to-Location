import ipinfo
import folium

#access_token = '5861c7f1f13c4a' arnav264@gmail.com
access_token = 'a60aad357c0b53' #bhattacharyaarnav264@gmail.com
handler = ipinfo.getHandler(access_token)
name = input("Enter the Target's Name: ")
ip = input("Enter the IP Address: ")
details = handler.getDetails(ip)
values = details.all

# Storing and Printing Information
service_provider = values['org']
region = values['region']
country = values['country_name']
time_zone = values['timezone']
print("\nService Provider: %s \nRegion: %s \nCountry: %s \nTime Zone: %s" % (service_provider, region, country, time_zone))

# Showing the location on a MAP 
fg = folium.FeatureGroup("My Map")
fg.add_child(folium.Marker(location=[values['latitude'], values['longitude']], popup="Target's Location"))
map = folium.Map(location=[values['latitude'], values['longitude']], zoom_start=15)
map.add_child(fg)

# Saving the Map
map.save(name+".html")
print("\nCheck the HTML page for the map.")

# from requests import get

# ip = get('https://api.ipify.org').text
# print('My public IP address is: {}'.format(ip))