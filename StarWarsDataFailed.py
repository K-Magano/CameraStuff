import requests
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get Supabase URL and key from environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_starwars_data(endpoint):
   url = f'https://swapi.dev/api/{endpoint}/'
   response = requests.get(url)
   response.raise_for_status()  # Check for request success
   data = response.json()
   return data['results']

# Improved data insertion with error handling
def populate_planets_table():
    planets_data = get_starwars_data('planets')
    for planet in planets_data:
      try:
        response = supabase.table('planets').insert(planet)
        print(f"Planet inserted: {planet['name']}")
      except Exception as e:
        print(f"Error inserting planet {planet['name']}: {str(e)}")

def populate_people_table():
    people_data = get_starwars_data('people')
    for person in people_data:
      mass_kg = float(person['mass'])
      mass_pounds = round(mass_kg * 2.20462)
      person['mass_pounds'] = mass_pounds

      try:
        response = supabase.table('people').insert(person)
        print(f"Person inserted: {person['name']}")
      except Exception as e:
        print(f"Error inserting person {person['name']}: {str(e)}")

# Running the population functions
populate_planets_table()
populate_people_table()
