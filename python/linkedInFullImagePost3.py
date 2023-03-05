import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
linkedIn_api_key = os.getenv('LINKEDIN_API_KEY')
linkedIn_author_id = os.getenv('LINKEDIN_AUTHOR_ID')

#science scribbles
bearerToken = 'Bearer ' + linkedIn_api_key

##############################################################################################################


#imagePath = open("Header_Full.jpg", "rb").read()

#caption = "This is our other logo"

##############################################################################################################
# CREATE IMAGE SHARE

mediaText = "test upload for HATCH2023"
description = "test upload for HATCH2023"

def uploadImageToLinkedIn(imageToUpload, textForPost):
    urlForImageShare = "https://api.linkedin.com/v2/assets?action=registerUpload"

    payload = json.dumps({
        "registerUploadRequest": {
            "recipes": [
                "urn:li:digitalmediaRecipe:feedshare-image"
            ],
            "owner": linkedIn_author_id,
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    })


    headers = {
    'Authorization': bearerToken,
    'X-Restli-Protocol-Version': '2.0.0',
    'LinkedIn-Version': '202302',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", urlForImageShare, headers=headers, data=payload)

    #print(response.text)
    #print(response.reason)
    #print(response.status_code)


    json_response = response.json()
    urlForImageUpload = json_response['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    headersForUpload = json_response['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['headers']
    assetForUpload = json_response['value']['asset']

    print(json_response)
    print('URL', urlForImageUpload)
    print('HEADERS', headersForUpload)
    print('ASSET', assetForUpload)


    ##############################################################################################################
    # UPLOAD THE IMAGE 
    headers = {"Authorization": bearerToken}

    #response = requests.put(uploadImageURL, data=image, headers=headers)
    #print(action.status_code)

    response = requests.request("POST", urlForImageUpload, headers=headers, data=imageToUpload)

    print(response.text)
    print(response.reason)
    print(response.status_code)

    ##############################################################################################################
    # CREATE THE POST

    postURL = "https://api.linkedin.com/v2/ugcPosts"

    payload = json.dumps({
        "author": linkedIn_author_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": textForPost
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": description
                        },
                        "media": assetForUpload,
                        "title": {
                            "text": mediaText
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    })

    headers = {
    'Authorization': bearerToken,
    'X-Restli-Protocol-Version': '2.0.0',
    'LinkedIn-Version': '202302',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", postURL, headers=headers, data=payload)

    print(response.text)
    print(response.reason)
    print(response.status_code)


    '''
    {"id":"urn:li:share:7036075519661993984"}
    Created
    201
    '''

#uploadImageToLinkedIn(imagePath, caption)
##############################################################################################################

