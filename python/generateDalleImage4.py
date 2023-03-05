import openai
import json
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key

#promptForDalle = "science stuff"

def generateDalleImage(promptForDalle):

    response = openai.Image.create(
        prompt = promptForDalle,
        n=2,
        size="1024x1024"
    )

    file1 = True

    #print(response['data'])
    
    #print('responseType', type(response))
    
    for urls in response['data']:
        print(urls['url'])
        filename = time.strftime('%Y-%m-%d_%H-%M-%S') + ".png"
        
        if (file1 == True):
            url1 = urls['url']
            filename1 = filename
            file1 = False
        else:
            url2 = urls['url']
            filename2 = filename

        print(filename)
        response = requests.get(urls['url'])
        with open(filename, "wb") as f:
            f.write(response.content)

    formattedJSON = {
        'url1': url1,
        'url2': url2,
        'image1': filename1,
        'image2': filename2
    }

    #print(formattedJSON)
    
    return(formattedJSON)
    
##########################################################################

#generateDalleImage(promptForDalle)