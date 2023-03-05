import json
import math
from pyexpat.errors import messages
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
open_api_key = os.getenv('OPEN_API_KEY')

# sorry, this is a bit messy, but it works
summary_char_limit = 5000


# Define the text to send to the API
openai.api_key = open_api_key

def generate_summary(article):
  char_count = len(article)
  chunks = math.ceil(char_count / summary_char_limit)
  return generate_Chad_Response(chunks, article)


# Define a function to generate a Chad Call
def generate_Chad_Response(chunks, article):
    summary = ""
    Total_Tokens = 0
    summary_char_limit_count = 0
# Loop over the chunks and generate Chad Response for each chunk
    for i in range(chunks):
    # Extract the relevant portion of the article for this chunk
        if(i == chunks ):
            chunk_article = article[summary_char_limit_count: ]
        else:
            chunk_article = article[summary_char_limit_count: summary_char_limit_count + summary_char_limit]

        summary_char_limit_count = summary_char_limit_count + summary_char_limit

    # Build summary from Chad
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.0,
        frequency_penalty=0.0,
        presence_penalty=-2.0,
        max_tokens=2045,
        #Chad Summary Prompt
        messages = [{"role": "system", "content": "You are a technical science writer that summarizes very accurately scientific articles provided by a user. You must summarize each article using no more than {summary_char_limit} characters.}"},
{"role": "user", "content": f"Please sumarize the provided scientific article in no more than {summary_char_limit} characters. Scientific Article: {chunk_article}"}
]) 
        '''
        messages= [
        {"role": "system", "content": ""},
        {"role": "user", "content": f"Does have {summary_char_limit} in the {chunk_article}"}
            ]
        '''
        summary = summary + response['choices'][0]['message']['content']
        Total_Tokens = Total_Tokens + response['usage']['total_tokens']
    return {
        "summary": summary,
        "totalTokens": Total_Tokens
    }

#########SOCIAL MEDIA CONTENT PROMPT#########
def generate_Chad_Social(article):
    Total_Tokens = 0
       
    # Build Social COntent from Chad
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    max_tokens=2045,
    #Chad Social Content Summary 
    messages = [
        {"role": "system", "content": "You are a professional creative social media content science writer that summarizes science articles so a highschool student can understand your social media posts.  You write concise and creative posts based on the user provided scientific article. You write 5 unique posts for the following social media platforms:Blog, Facebook, LInkedIn, Instagram, Twitter. You are really accurate in creating posts for each social media platform that matches the total character or word limitations specified here: 1) A blog post containing no more than 1,200 words. 2) a Facebook post containing no more than 200 words. 3) A LinkedIn post containing no more than 200 words. 4) A Instagram post containing no more than 2,150 characters. 5) A Twitter post that is no more than 200 characters.  The content generated for the Blog, Facebook, LinkedIn, Instagram and Twitter should all include 2 hashtags related to each post."},
        {"role": "user", "content": f"Please create 5 unique creative social media content posts and give it to me in a numbered list using the following scientific article as the source for your social media content: {article}"},
        {"role": "assistant", "content": "Here is your 5 unique social media posts for a Blog, Facebook, LinkedIn, Instagram, and Twitter all provided in a numbered list format using the scientific article you provided as the source used to create the social media posts. The list format is as follows: 1) Blog Post 2) Facebook Post 3) LinkedIn Post 4) Instagram Post 5) Twitter Post"}    
            ]) 
     
    
    Total_Tokens = Total_Tokens + response['usage']['total_tokens']
    # Replace new lines with spaces and remove double spaces
    input_str = response['choices'][0]['message']['content']
    input_str = input_str.strip()
    input_str = input_str.replace('\n', ' ')
    #print('input_str', input_str)

    
    #print('SPLIT', input_str.split('1)'))
    try:
        blogPostSection = input_str.split('Blog Post:')[1]
    except:
        blogPostSection = input_str.split('Blog post:')[1]
    try:
        blogPost = blogPostSection.split('Facebook Post:')[0]
    except:
        blogPost = blogPostSection.split('Facebook post:')[0]
    #print('blogPost', blogPost)
    blogPost = blogPost.strip()

    try:
        facebookPostSection = input_str.split('Facebook Post:')[1]
    except:
        facebookPostSection = input_str.split('Facebook post:')[1]
    try:
        facebookPost = facebookPostSection.split('LinkedIn Post:')[0]
    except:
        facebookPost = facebookPostSection.split('LinkedIn post:')[0]
    #print('facebookPost', facebookPost)
    facebookPost = facebookPost.strip()

    try:
        linkedinPostSection = input_str.split('LinkedIn Post:')[1]
    except:
        linkedinPostSection = input_str.split('LinkedIn post:')[1]
    try:
        linkedinPost = linkedinPostSection.split('Instagram Post:')[0]
    except:
        linkedinPost = linkedinPostSection.split('Instagram post:')[0]
    
    #print('linkedinPost', linkedinPost)
    linkedinPost = linkedinPost.strip()

    try:
        instagramPostSection = input_str.split('Instagram Post:')[1]
    except:
        instagramPostSection = input_str.split('Instagram post:')[1]
    try:
        instagramPost = instagramPostSection.split('Twitter Post:')[0]
    except:
        instagramPost = instagramPostSection.split('Twitter post:')[0]

    #print('instagramPost', instagramPost)
    instagramPost = instagramPost.strip()

    try:
        twitterPostSection = input_str.split('Twitter Post:')[1]
    except:
        twitterPostSection = input_str.split('Twitter post:')[1]
    
    twitterPost = twitterPostSection
    twitterPost = twitterPost.strip()
    #print('twitterPost', twitterPost)

    #formatted_str = ' '.join(input_str.split()).replace('  ', ' ')

# Load the formatted string as JSON
    #json_obj = json.loads(formatted_str)
    #print(json_obj)
# Return the formatted JSON objectfor item in json_da   ta:

    socialArray = [
    {
    'platform': 'Blog',
    'post': blogPost
    },
    {
    'platform': 'Facebook',
    'post': facebookPost
    },
    {
    'platform': 'LinkedIn',
    'post': linkedinPost
    },
    {
    'platform': 'Instagram',
    'post': instagramPost
    },
    {
    'platform': 'Twitter',
    'post': twitterPost
    }]
    
    #print(socialArray)
    
    return socialArray #json.loads(socialArray) #input_str)

#########DALL-E AI PROMPT#########
def generate_Chad_Dalle(article):
    Total_Tokens = 0
    
# Loop over the chunks and generate Chad Response for each chunk
   
    # Build Dall-e Prompt from Chad
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    max_tokens=2045,
    #Chad Dalle Summary Prompt
    messages = [
        {"role": "system", "content": "You are an artist that can create a detailed textual description of scenes or objects based on a user provided scientific article. "},
        {"role": "user", "content": f"What would be a good Dall-e AI prompt to create an image using the AI Dall-e model for the following article: {article}"},
        {"role": "assistant", "content": "Here is a very short and creative Dall-e prompt that the user can use to create a Dall-e image using the openai Dall-e model:"}

                ]) 
    
    Total_Tokens = Total_Tokens + response['usage']['total_tokens']
    response=response['choices'][0]['message']['content']
    # return response, Total_Tokens       
    return response

#Social Media Content Prompt
'''
       messages = [{"role": "system", "content": "You are a professional creative science writer that summarizes science articles so a highschool student can understand it.  You summarize creative posts based on the user provided scientific article for several different social media platforms. The following are the social media platforms and the size of the post that you will write content for:that you will write content for: 1) A blog post containing no more than 1,250 words. 2) a Facebook post containing no more than 250 words. 3) A LinkedIn post containing no more than 250 words. 4) A Instagram post containing no more than 2,200 characters. 5) A Twitter post that is no more than 280 characters.  The content generated for the Blog, Facebook, LinkedIn, Instagram and Twitter should all include hashtags related to each post."},
{"role": "user", "content": f"Please create creative social media content post and display it in a JSON format using the following scientific article:for each of the following social media platform you create in a JSON format. Provide in the JSON a Blog post, Facebook post, Can you create all the requested social media content post for the following science article: {chunk_article}"}
]) 
'''

#DALL-E AI prompt
'''
messages = [{"role": "system", "content": "You are a technical science writer that summarizes very accurately scientific articles provided by a user. You must summarize each article using no more than {summary_char_limit} characters.}"},
{"role": "user", "content": f"Can you provide a JSON response to include two entries. One entry is a summary of the provided scientific article that is no more than {summary_char_limit} characters and a second entry in the JSON output is a DALL-E AI prompt that is a detailed textual description of a scene or an object based on the scientific article provided. Here's the scientific article: {chunk_article}"}
]) 
'''
