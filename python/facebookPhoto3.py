import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

facebook_access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
facebook_page_id = os.getenv('FACEBOOK_PAGE_ID')
#captionForPhotos = 'second logo'
#fileToUpload = '2.jpg'

def uploadImageToFacebook(filepath, captionForPhotos):

    # Set the URL for the graph API endpoint
    url = 'https://graph.facebook.com/{}/photos'.format(facebook_page_id)

    # Set the parameters for the request
    params = {
        'access_token': facebook_access_token,
        'message': captionForPhotos,
        'published': True
    }

    # Set the file paths of the images to be uploaded
    # filepath = '1.jpg'

    # Open the image files and make the requests
    #for filepath in filepaths:
    with open(filepath, 'rb') as f:
        response = requests.post(url, params=params, files={'source': f})
        print(response.text)

    # Check the status code of the response
    if response.status_code == 200:
        print('Photo uploaded successfully')
    else:
        print('Photo upload failed. Status code:', response.status_code)


#uploadImageToFacebook(fileToUpload, captionForPhotos)

