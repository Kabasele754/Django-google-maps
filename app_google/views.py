from django.shortcuts import render
from googlemaps import Client

from app_google.models import Restaurant
from decouple import config

KEY = config('KEY')

def find_restaurants(request):
    restaurants = []
    if request.method == 'POST':
        address = request.POST.get('address')
        gmaps = Client(key=KEY)
        geocode_result = gmaps.geocode(address)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        places_result = gmaps.places_nearby(location=(lat,lng), radius=5)
        print(places_result['results'])
        for place in places_result['results']:
            ve = place['vicinity'][9:]
            # the name of place and vicinity
            name =place['name'] + place['vicinity'][8:]
            print(name)
            print(place['vicinity'][9:] == address[9:])
            if place['vicinity']== address:
                Restaurant.objects.create(
                    name=place['vicinity'],
                    lat=lat,
                    lng=lng
                )
            restaurants.append({
                'name': place['name'],
                'lat': place['geometry']['location']['lat'],
                'lng': place['geometry']['location']['lng']
            })

        # print("name restaurant", places_result['results'])

        # print(geocode_result[0])
        #print(geocode_result)
        # print(geocode_result[0]['formatted_address'])
        for component in geocode_result[0]['address_components']:
            #print('establishment'==component['types'])

            #print('establishment' in component['types'])
            if 'locality' in component['types']:
                ville = component['long_name']
            elif 'sublocality' in component['types']:
                quartier = component['long_name']
                print("Voir addresse", quartier)
            elif 'route' in component['types']:
                avenue = component['long_name']



        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        restaurant = Restaurant.objects.create(
            name=name,
            lat=latitude,
            lng=longitude

        )

        return render(request, 'google_maps/index.html', {'restaurants': restaurants, 'key':KEY})
    else:
        return render(request, 'google_maps/index.html', {'restaurants': restaurants, 'key':KEY})

