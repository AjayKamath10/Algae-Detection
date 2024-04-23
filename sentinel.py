import requests
import json

def fetch_sentinel_image(latitude, longitude, date):
    # Define the API endpoint
    url = "https://services.sentinel-hub.com/api/v1/process"
    
    api_key = "BdzRi6xzcQHEAJ2K2r5wqINlk7rSznMT"
    # Define the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Define the request body
    # This example requests a true color image from Sentinel-2 L2A
    # You can adjust the parameters as needed
    body = {
        "input": {
            "bounds": {
                "geometry": {
                    "type": "Point",
                    "coordinates": [longitude, latitude]
                },
                "properties": {
                    "crs": "EPSG:4326" #WGS 84 coordinate system, which is a standard for representing geographical coordinates on the Earth's surface
                }
            },
            "data": [
                {
                    "type": "S2L2A", #Sentinel-2 L2A data
                    "dataFilter": {
                        "timeRange": {
                            "from": date,
                            "to": date
                        }
                    }
                }
            ]
        },
        "output": {
            "width": 512,
            "height": 512,
            "responses": [
                {
                    "identifier": "default",
                    "format": {
                        "type": "image/png"
                    }
                }
            ]
        }
    }
    
    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(body))
    
    # Check if the request was successful
    if response.status_code == 200:
        # The response contains a URL to the image
        image_url = response.json()['outputs'][0]['url']
        return image_url
    else:
        print(f"Error: {response.status_code}")
        return None