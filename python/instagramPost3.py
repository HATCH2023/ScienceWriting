
from instagrapi import Client

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

instagram_username = os.getenv('INSTAGRAM_USERNAME')
instagram_password = os.getenv('INSTAGRAM_PASSWORD')


client = Client()

#filePath = 'logo.jpg'
#descriptionForPost = 'this is our logo!'

def uploadImageToInstagram(filename, description):
    client.login(instagram_username, instagram_password)

    media = client.photo_upload(
        path = filename,
        caption = description,
        #usertags = [Usertag(user=user, x=0.5, y=0.5)],
        #location=Location(name="Spain, Madrid", lat = 40, lng = 3),
        extra_data={
            "custom_accessibility_caption": "this is an alt text example"#,
                #"like_and_view_counts_disabled": False,
                #"disable_comments": False
            }
        )

#uploadImageToInstagram(filePath, descriptionForPost)