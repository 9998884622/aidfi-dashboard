# Dummy Firebase Config
# Replace later with real Firebase

data_files = []
locations = {}

def upload_file(path, name):

    data_files.append(name)

def get_files():

    return data_files

def save_location(user, lat, lng):

    locations[user] = {
        "lat": lat,
        "lng": lng
    }

def get_locations():

    return locations
