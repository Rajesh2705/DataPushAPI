import requests
from celery import shared_task

@shared_task
def send_data_to_destinations(data, destinations):
    for destination in destinations:
        headers = {header['key']: header['value'] for header in destination['headers']}
        print(headers)
        url = destination['url']
        print(url)
        http_method = destination['http_method']
        try:
            if http_method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif http_method.upper() == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            elif http_method.upper() == 'GET':
                params = []
                for key, value in data.items():
                    params.append(f"{key}={value}")
                query_string = "&".join(params)
                url = f"{url}?{query_string}"
                response = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            pass
        # Process the response as needed