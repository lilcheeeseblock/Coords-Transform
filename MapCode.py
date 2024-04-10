import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Function to convert degrees, minutes, seconds to decimal degrees
def dms_to_dd(degrees, minutes, seconds):
    dd = degrees + minutes/60 + seconds/3600
    return dd

def use(lat_d, lat_m, lat_s, lon_d, lon_m, lon_s):
    # Coordinates of the point in degrees, minutes, seconds
    latitude_deg = lat_d
    latitude_min = lat_m
    latitude_sec = lat_s

    longitude_deg = lon_d
    longitude_min = lon_m
    longitude_sec = lon_s

    # Convert to decimal degrees
    latitude = dms_to_dd(latitude_deg, latitude_min, latitude_sec)
    longitude = dms_to_dd(longitude_deg, longitude_min, longitude_sec)

    # Create a Basemap instance
    map = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='l')

    # Draw coastlines, countries, and states
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()

    # Draw parallels and meridians with labels
    map.drawparallels(range(-90, 91, 10), labels=[1, 0, 0, 0])
    map.drawmeridians(range(-180, 181, 30), labels=[0, 0, 0, 1])

    # Plot the point
    x, y = map(longitude, latitude)
    map.scatter(x, y, color='red', s=80, marker='o', label='Point')

    # Add title and legend
    plt.title('World Map with Latitude and Longitude in Degrees, Minutes, Seconds')
    plt.legend()

    # Show the map
    plt.show()

