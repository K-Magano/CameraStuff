import requests
import os
import supabase

def fetch_starwars_data(endpoint):
    url = f"https://swapi.dev/api/{endpoint}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

def insert_data (data):
    supabase_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN3enh6am54dGxmZWdydXlzZnFnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM2NzQ3MzksImV4cCI6MjAyOTI1MDczOX0.pAgYURUhi9d3GSJt7Qx01uHidEWX3CKSqIA94mrDJLM'
    supabase_url = 'https://swzxzjnxtlfegruysfqg.supabase.co'
    supabase_client = supabase.Client(supabase_url, supabase_api_key)
    supabase_client.table("people").insert(data)
  
# Fetch data about planets
planets_data = fetch_starwars_data("planets")
if planets_data:
    print("Planets data retrieved successfully!")
    print(planets_data)
else:
    print("Failed to fetch planets data.")

# Fetch data about characters (people)
people = fetch_starwars_data("people")
if people:
    print("People data retrieved successfully!")
#     print(people_data)
# else:
#     print("Failed to fetch people data.")

# people = fetch_starwars_data("people")

# if people:
    for person in people["results"]:
        data_to_insert = {
            "name": person["name"],
            "birth_year": person["birth_year"],
            "eye_color": person["eye_color"],
            "gender": person["gender"],
            "hair_color": person["hair_color"],
            "height": person["height"],
            "mass": person["mass"],
            "skin_color": person["skin_color"],
            "homeworld": person["homeworld"]
        }
        insert_data(data_to_insert)
    else:
        print("Failed to insert data")



