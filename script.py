destinations=['Paris, France','Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

attractions=[[] for i in range(len(destinations))]

test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

destination_index=0
def get_destination_index(destination):
  for location in destinations:
    destination_index=destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  for i in range(len(destinations)):
    for j in range(len(traveler)):
      if destinations[i]==traveler[j]:
        traveler_destination=traveler[j]
        traveler_destination_index=get_destination_index(traveler_destination)
      else:
        traveler_destination="Destination not found!!! Please enter destination"
  return traveler_destination_index

test_destination_index=get_traveler_location(test_traveler)

print(test_destination_index)

def add_attraction(destination,attraction):
  try:
    destination_index=get_destination_index(destination)
    attractions_for_destination=[]
    attractions_for_destination.append(attraction)
    attractions[destination_index]=attractions_for_destination
    return None

  except ValueError:
    return None

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction('Paris, France', ["the Louvre", ["art", "museum"]])
add_attraction('Paris, France', ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction('Shanghai, China', ["Yu Garden", ["garden", "historcical site"]])
add_attraction('Shanghai, China', ["Yuz Museum", ["art", "museum"]])
add_attraction('Shanghai, China', ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction('Los Angeles, USA', ["LACMA", ["art", "museum"]])
add_attraction('São Paulo, Brazil', ["São Paulo Zoo", ["zoo"]])
add_attraction('São Paulo, Brazil', ["Pátio do Colégio", ["historical site"]])
add_attraction('Cairo, Egypt', ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction('Cairo, Egypt', ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  attractions_with_interest=[]
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  for i in range(len(attractions_in_city)):
    possible_attraction=attractions_in_city[i]
    attraction_tags=possible_attraction[1]
    for j in range(len(interests)):
      for k in range(len(attraction_tags)):
        if interests[j]==attraction_tags[k]:
          attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts=find_attractions('Los Angeles, USA',['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination,traveler_interests)
  interests_string="Hi "+ str(traveler[0])+", we think you'll like these places around "+ str(traveler_destination)+": "
  for i in traveler_attractions:
    interests_string=interests_string+"the "+ str(i) + " "
  interests_string+="."
  return interests_string

smills_france=get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)