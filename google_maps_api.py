import googlemaps
import pandas as pd
from datetime import datetime

# Initialize Google Maps Client
gmaps = googlemaps.Client(key=API_KEY)

# Coordinates of Back Bay Station, Boston
BACK_BAY_COORDINATES = (42.347304, -71.075619)  # Latitude, Longitude


# def get_condos_within_radius(center, radius_meters, place_type="condominium complex"):
#     """Find condominium complexes within a given radius using Places API."""
#     results = []
#     search_keywords = [
#         "condominium complex",
#         "condo",
#         "condominium",
#         "gated community",
#         "apartment complex",
#     ]
#
#     for keyword in search_keywords:
#         response = gmaps.places_nearby(
#             location=center, radius=radius_meters, keyword=keyword
#         )
#         results.extend(response.get("results", []))
#
#         # Handle pagination if needed
#         while "next_page_token" in response:
#             response = gmaps.places_nearby(
#                 location=center,
#                 radius=radius_meters,
#                 keyword=place_type,
#                 page_token=response["next_page_token"],
#             )
#             results.extend(response.get("results", []))
#
#     # # Perform nearby search
#     # response = gmaps.places_nearby(
#     #     location=center,
#     #     radius=radius_meters,
#     #     keyword=place_type
#     # )
#     # results.extend(response.get('results', []))
#
#     return results
#
#
# def get_commuter_stations(center, radius_meters=50000):
#     """Find commuter rail stations within a given radius."""
#     results = []
#
#     response = gmaps.places_nearby(
#         location=center, radius=radius_meters, keyword="commuter rail station"
#     )
#
#     results.extend(response.get("results", []))
#
#     # Handle pagination if needed
#     while "next_page_token" in response:
#         response = gmaps.places_nearby(
#             location=center,
#             radius=radius_meters,
#             keyword="commuter rail station",
#             page_token=response["next_page_token"],
#         )
#         results.extend(response.get("results", []))
#
#     return results
#     # return response.get('results', [])
#
#
# def filter_by_walking_distance(
#     condos, stations, min_walk_minutes=5, max_walk_minutes=10
# ):
#     """Filter condos that are 5 to 10 minutes walking from any commuter rail station."""
#     valid_condos = []
#     for condo in condos:
#         condo_location = (
#             condo["geometry"]["location"]["lat"],
#             condo["geometry"]["location"]["lng"],
#         )
#
#         for station in stations:
#             station_location = (
#                 station["geometry"]["location"]["lat"],
#                 station["geometry"]["location"]["lng"],
#             )
#
#             # Calculate walking distance using Distance Matrix API
#             response = gmaps.distance_matrix(
#                 origins=condo_location,
#                 destinations=station_location,
#                 mode="walking",
#                 departure_time=datetime.now(),
#             )
#
#             if response["rows"][0]["elements"][0]["status"] == "OK":
#                 duration_minutes = (
#                     response["rows"][0]["elements"][0]["duration"]["value"] / 60
#                 )  # Convert to minutes
#                 print(
#                     f"{condo['name']} to {station['name']}: {duration_minutes} minutes"
#                 )
#                 if min_walk_minutes <= duration_minutes <= max_walk_minutes:
#                     valid_condos.append(
#                         {
#                             "name": condo["name"],
#                             "address": condo.get("vicinity", ""),
#                             "walking_minutes": duration_minutes,
#                             "station_name": station["name"],
#                         }
#                     )
#
#     return valid_condos
#
#
# def main():
#     # Step 1: Find Condominiums within 30-min train radius (approx. 50 km radius for search)
#     condos = get_condos_within_radius(BACK_BAY_COORDINATES, radius_meters=50000)
#
#     # Step 2: Find Commuter Rail Stations
#     stations = get_commuter_stations(BACK_BAY_COORDINATES)
#
#     # Step 3: Filter Condos within 5-10 Minutes Walking from a Commuter Station
#     valid_condos = filter_by_walking_distance(condos, stations)
#
#     # Output results in DataFrame
#     df = pd.DataFrame(valid_condos)
#     print(df)
#
#     # Save results to a CSV
#     df.to_csv("condos_near_commuter_rail.csv", index=False)


def search_with_commuter_list_v2():
    # List of commuter rail stations
    stations = [
        "South Station",
        "Newmarket",
        "Uphams Corner",
        "Four Corners/Geneva",
        "Talbot Avenue",
        "Morton Street",
        "Fairmount",
        "Readville",
        "North Station",
        "Porter",
        "Belmont",
        "Waverley",
        "Waltham",
        "Brandeis/Roberts",
        "Kendall Green",
        "Lincoln",
        "Concord",
        "West Concord",
        "South Acton",
        "Littleton/495",
        "Ayer",
        "Shirley",
        "North Leominster",
        "Fitchburg",
        "South Station",
        "Back Bay",
        "Lansdowne",
        "Boston Landing",
        "Newtonville",
        "West Newton",
        "Auburndale",
        "Wellesley Farms",
        "Wellesley Hills",
        "Wellesley Square",
        "Natick Center",
        "West Natick",
        "Framingham",
        "Ashland",
        "Southborough",
        "Westborough",
        "Grafton",
        "Worcester/Union Station",
        "South Station",
        "Back Bay",
        "Ruggles",
        "Hyde Park",
        "Readville",
        "Endicott",
        "Dedham Corporate Center",
        "Islington",
        "Norwood Depot",
        "Norwood Central",
        "Windsor Gardens",
        "Walpole",
        "Norfolk",
        "Franklin/Dean College",
        "Forge Park/495",
        "Walpole",
        "South Station",
        "JFK/UMass",
        "Quincy Center",
        "East Weymouth",
        "West Hingham",
        "Nantasket Junction",
        "Cohasset",
        "North Scituate",
        "Greenbush",
        "North Station",
        "Malden Center",
        "Wyoming Hill",
        "Melrose/Cedar Park",
        "Melrose Highlands",
        "Greenwood",
        "Wakefield",
        "Reading",
        "North Wilmington",
        "Ballardvale",
        "Andover",
        "Lawrence",
        "Bradford",
        "Haverhill",
        "South Station",
        "JFK/UMass",
        "Quincy Center",
        "Braintree",
        "Weymouth Landing/East Braintree",
        "East Weymouth",
        "West Hingham",
        "Nantasket Junction",
        "Cohasset",
        "North Scituate",
        "Greenbush",
        "Shared with Middleborough/Lakeville Line:",
        "Halifax",
        "Kingston",
        "North Station",
        "West Medford",
        "Wedgemere",
        "Winchester Center",
        "Mishawum",
        "Anderson/Woburn",
        "Wilmington",
        "North Billerica",
        "Lowell",
        "South Station",
        "JFK/UMass",
        "Quincy Center",
        "Braintree",
        "Holbrook/Randolph",
        "Montello",
        "Brockton",
        "Campello",
        "Bridgewater",
        "Middleborough/Lakeville",
        "South Station",
        "Back Bay",
        "Ruggles",
        "Forest Hills",
        "Roslindale Village",
        "Bellevue",
        "West Roxbury",
        "Highland",
        "Needham Junction",
        "Needham Center",
        "Needham Heights",
        "North Station",
        "Chelsea",
        "River Works",
        "Lynn",
        "Swampscott",
        "Salem",
        "Beverly Depot",
        "Rockport Branch:",
        "Montserrat",
        "Prides Crossing",
        "Beverly Farms",
        "Manchester-by-the-Sea",
        "Gloucester",
        "West Gloucester",
        "Rockport",
        "Newburyport Branch:",
        "North Beverly",
        "Hamilton/Wenham",
        "Ipswich",
        "Rowley",
        "Newburyport",
        "South Station",
        "Back Bay",
        "Ruggles",
        "Hyde Park",
        "Route 128",
        "Canton Junction",
        "Providence Branch:",
        "Sharon",
        "Mansfield",
        "Attleboro",
        "South Attleboro (Temporarily Closed)",
        "Stoughton Branch:",
        "Canton Center",
        "Stoughton",
        "South Station",
        "Back Bay",
        "Dedham Corporate Center",
        "Norwood Depot",
        "Norwood Central",
        "Walpole",
        "Foxboro",
    ]

    # Step 1: Find stations within 40 mins by train from Back Bay
    stations_within_40_mins = []
    departure_time = datetime.now().replace(
        hour=8, minute=0, second=0, microsecond=0
    )  # Today at 8 AM
    for station in stations:
        result = gmaps.distance_matrix(
            origins="Back Bay Station, Boston, MA",
            destinations=station,
            mode="transit",
            transit_mode="train",
            departure_time=departure_time,
            units="imperial",
        )
        duration = (
            result["rows"][0]["elements"][0].get("duration", {}).get("value", None)
        )  # Duration in seconds
        if duration and 15 * 60 <= duration <= 40 * 60:  # 15 and 40 mins in seconds
            stations_within_40_mins.append(station)

    # Step 2: Search nearby condos/apartments within 5-10 mins walk
    results = []
    keywords = [
        "condominium complex",
        "condo",
        "condominium",
        "gated community",
        "apartment complex",
    ]
    keywords_daycare = ["daycare", "Montessori"]
    for station in stations_within_40_mins:
        location = gmaps.geocode(station)[0]["geometry"]["location"]
        lat, lng = location["lat"], location["lng"]
        places_results = []

        try:
            for keyword in keywords:
                places = gmaps.places_nearby(
                    location=(lat, lng),
                    radius=800,  # Approx. 5-10 mins walk ~ 800m
                    keyword=keyword,
                    type="establishment",
                )

                places_results.extend(places.get("results", []))

                # Handle pagination if needed
                while "next_page_token" in places:
                    places = gmaps.places_nearby(
                        location=(lat, lng),
                        radius=800,  # Approx. 5-10 mins walk ~ 800m
                        keyword=keyword,
                        type="establishment",
                        page_token=places["next_page_token"],
                    )
                    places_results.extend(places.get("results", []))

                for place in places_results:
                    condo_address = place['vicinity']

                    distance_result = gmaps.distance_matrix(
                        origins=station,
                        destinations=place["vicinity"],
                        mode="walking",
                        units="imperial",
                    )
                    distance_data = distance_result["rows"][0]["elements"][0]
                    # walking_distance_miles = distance_data.get('distance', {}).get('text', None)  # Example: '0.5 mi'
                    walking_duration_mins = distance_data.get("duration", {}).get(
                        "text", None
                    )  # Example: '6 mins'

                    # Step 3: Search nearby daycare/Montessori within 10 mins walk from condo
                    condo_location = place["geometry"]["location"]
                    daycare_found = False

                    for daycare_keyword in keywords_daycare:
                        daycares = gmaps.places_nearby(
                            location=(condo_location["lat"], condo_location["lng"]),
                            radius=800,  # Approx. 10 mins walk ~ 800m
                            keyword=daycare_keyword,
                            type="establishment",
                        )

                        for daycare in daycares.get("results", []):
                            # Calculate walking distance & duration from condo to daycare
                            distance_to_daycare = gmaps.distance_matrix(
                                origins=condo_address,
                                destinations=daycare["vicinity"],
                                mode="walking",
                                units="imperial",
                            )["rows"][0]["elements"][0]

                            daycare_distance_miles = distance_to_daycare.get(
                                "distance", {}
                            ).get("text", None)
                            daycare_duration_mins = distance_to_daycare.get(
                                "duration", {}
                            ).get("text", None)

                            # Save results
                            results.append(
                                {
                                    "station": station,
                                    "condo_name": place["name"],
                                    "condo_address": condo_address,
                                    # "walking_distance_to_station_miles": walking_distance_miles,
                                    "walking_duration_to_station_mins": walking_duration_mins,
                                    "daycare_name": daycare["name"],
                                    "daycare_address": daycare["vicinity"],
                                    # "walking_distance_to_daycare_miles": daycare_distance_miles,
                                    "walking_duration_to_daycare_mins": daycare_duration_mins,
                                }
                            )

                            daycare_found = True
                            break  # Only take the first daycare found

                    if not daycare_found:
                        results.append(
                            {
                                "station": station,
                                "condo_name": place["name"],
                                "condo_address": condo_address,
                                # "walking_distance_to_station_miles": walking_distance_miles,
                                "walking_duration_to_station_mins": walking_duration_mins,
                                "daycare_name": None,
                                "daycare_address": None,
                                # "walking_distance_to_daycare_miles": None,
                                "walking_duration_to_daycare_mins": None,
                            }
                        )

        except Exception as e:
            print(f"Error: {station} {place['name']} {e} ")
            continue

    # Step 3: Save results to CSV
    df = pd.DataFrame(results)
    df = df.drop_duplicates(
        subset=["condo_address"], keep="first"
    )  # <- Prevent duplicates by address
    df.to_csv("condos_near_daycare_with_distance.csv", index=False)
    print(df.head())


if __name__ == "__main__":
    # main()
    search_with_commuter_list_v2()


    # store this in the github repo
    # school ratings above 7 or 8
    # wheel chair friendly
    # day care near 10 mins walk
    # add a column for each of the above so that we can filter based on that
    # given the list of all commuter rails stations
    # get the list of all stations which are 40 mins from the back bay station in boston by train
    # search around each of those stations for 'condominium complex', 'condo', 'condominium','gated community','apartment complex' seperately
    # filter those which are 5-10 mins walking distance from the station
