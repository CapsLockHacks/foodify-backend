with open('lipton.jpg', 'rb') as f:
    response = api.image_request(f, 'lipton.jpg', {
        'image_request[locale]': 'en-US',
    })

status = api.image_response(response['token'])
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    pass
status = api.wait(response['token'], timeout=30)


from nutritionix import Nutritionix
nix = Nutritionix(app_id="76986486", api_key="28882f3d105c4c9e3222a05eeafd049a")

result = nix.search('pizza').json()