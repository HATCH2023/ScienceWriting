from serpapi import GoogleSearch
import json, re
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
google_scholar_api_key = os.getenv('GOOGLE_SCHOLAR_API_KEY')

miniJSONList = []

publisherList = ['www.ncbi.nlm.nih.gov'] 
#'onlinelibrary.wiley.com', 'www.ncbi.nlm.nih.gov', 
#'www.sciencedirect.com', #wiliey is consistent, but not science direct

resultMax = 3

startIndexForSearch = 0

#keywordSearch = 'obesity genes'  #'obesity genes'

def searchScholarForKeywords(keywordToSearchFor, startingIndex = 0):
   
    params = {
    "engine": "google_scholar",
    "q": keywordToSearchFor + ' site:ncbi.nlm.nih.gov',
    "hl": "en",
    #"as_ylo": "2018",
    "api_key": google_scholar_api_key,
    "num": "20",
    "start": startingIndex
    }

    lastValidResultIndex = 0
    resultIndex = 0

    search = GoogleSearch(params)
    results = search.get_dict()

    #print('###########################', results)
    #json_results = results.json()
    #json_results = json.loads(search)
    json_results = results

    #print(json_results)

    ##############################################################################################################

    try:
        searchSuccess = json_results['search_metadata']['status']
        #searchSuccess = searchSuccess.replace(r'\u\d{4}', ' ')
        searchSuccess = re.sub(r'[^\x00-\x7F]+', ' ', searchSuccess)
    except:
        searchSuccess = ''
        pass
    #print('searchSuccess', searchSuccess)

    try:
        createdAtDateTime = json_results['search_metadata']['created_at']
        createdAtDateTime = re.sub(r'[^\x00-\x7F]+', ' ', createdAtDateTime)
    except:
        createdAtDateTime = ''
        pass
    #print('createdAtDateTime', createdAtDateTime)

    try:
        searchURL = json_results['search_metadata']['google_scholar_url']
        searchURL = re.sub(r'[^\x00-\x7F]+', ' ', searchURL)
    except:
        searchURL = ''
        pass
    #print('searchURL', searchURL)
    
    try:
        searchInfoOrganicState = json_results['search_information']['organic_results_state']
        searchInfoOrganicState = re.sub(r'[^\x00-\x7F]+', ' ', searchInfoOrganicState)
    except:
        searchInfoOrganicState = ''
        pass
    #print('searchInfoOrganicState', searchInfoOrganicState)

    try:
        searchInfoTotalResults = json_results['search_information']['total_results']
        searchInfoTotalResults = re.sub(r'[^\x00-\x7F]+', ' ', searchInfoTotalResults)
    except:
        searchInfoTotalResults = ''
        pass
    #print('searchInfoTotalResults', searchInfoTotalResults)
    
    try:
        searchInfoQueryDisplayed = json_results['search_information']['query_displayed']
        searchInfoQueryDisplayed = re.sub(r'[^\x00-\x7F]+', ' ', searchInfoQueryDisplayed)
    except:
        searchInfoQueryDisplayed = ''
        pass
    #print('searchInfoQueryDisplayed', searchInfoQueryDisplayed)
      
    try:
        searchInfoSpellingFixed = json_results['search_information']['spelling_fix']
        searchInfoSpellingFixed = re.sub(r'[^\x00-\x7F]+', ' ', searchInfoSpellingFixed)
    except:
        searchInfoSpellingFixed = ''
        pass
    #print('searchInfoSpellingFixed', searchInfoSpellingFixed)

    try:
        organicResults = json_results['organic_results']
    except:
        pass

    # print('organicResults', organicResults)

    for result in organicResults:

        try:
            resultLink = result['link']
        except:
            resultLink = ''
            pass
        
        if resultLink != '':

            resultLinkDomain = resultLink.split('/')[2]
            #print('resultLinkDomain', resultLinkDomain)
            #domain = 
            if resultLinkDomain in publisherList:

                #print(result)
                #result = organicResults[0]  #this is a list and should be looped through.  how should we sort them?

                try:
                    resultPosition = result['position']
                except:
                    resultPosition = ''
                    pass
                lastValidResultIndex = resultPosition
                
                #print('resultPosition', resultPosition)

                try:
                    resultTitle = result['title']
                    resultTitle = re.sub(r'[^\x00-\x7F]+', ' ', resultTitle)
                except:
                    resultTitle = ''
                    pass

                #print('resultTitle', resultTitle)


                #print('resultLink', resultLink) 

                try:
                    resultID = result['result_id']
                    resultID = re.sub(r'[^\x00-\x7F]+', ' ', resultID)
                except:
                    resultID = ''
                    pass
                #print('resultID', resultID)

                try: 
                    resultSnippet = result['snippet']
                    resultSnippet = re.sub(r'[^\x00-\x7F]+', ' ', resultSnippet)

                except:
                    resultSnippet = ''
                    pass
                #print('resultSnippet', resultSnippet)

                try:
                    resultPublicationInfoSummary = result['publication_info']['summary']
                    resultPublicationInfoSummary = re.sub(r'[^\x00-\x7F]+', ' ', resultPublicationInfoSummary)
                except:
                    resultPublicationInfoSummary = ''
                    pass

                #print('resultPublicationInfoSummary', resultPublicationInfoSummary)

                try:
                    resultAuthors = result['publication_info']['authors']
                    #resultAuthors = re.sub(r'[^\x00-\x7F]+', ' ', resultAuthors)
                    authorList = []
                    for author in resultAuthors:
                        authorName = author['name']
                        authorName = re.sub(r'[^\x00-\x7F]+', ' ', authorName)
                        authorLink = author['link']
                        authorSerpapi_scholar_link = author['serpapi_scholar_link']
                        authorID = author['author_id']
                        authorJSON = {
                            'name': authorName,
                            'link': authorLink,
                            'serpapi_scholar_link': authorSerpapi_scholar_link,
                            'author_id': authorID
                        }
                        authorList.append(authorJSON)

                        pass
                except:
                    resultAuthors = ''
                    authorList = []
                #print('resultAuthors', resultAuthors)

                try:
                    for resource in result['resources']:
                        resultResourceTitle = resource['title']
                        resultResourceTitle = re.sub(r'[^\x00-\x7F]+', ' ', resultResourceTitle)
                        resultResourceFileFormat = resource['file_format']
                        resultResourceFileFormat  = re.sub(r'[^\x00-\x7F]+', ' ', resultResourceFileFormat)
                        resultResourceLink = resource['link']
                        resultResourceLink = re.sub(r'[^\x00-\x7F]+', ' ', resultResourceLink)

                except:
                    resultResourceTitle = ''
                    resultResourceFileFormat = ''
                    resultResourceLink = ''

                #print('resultResourceTitle', resultResourceTitle)
                #print('resultResourceFileFormat', resultResourceFileFormat)
                #print('resultResourceLink', resultResourceLink)
                
                
                try:
                    resultCiteLink = result['inline_links']['serpapi_cite_link']
                except:
                    resultCiteLink = ''
                    pass
                #print('resultCiteLink', resultCiteLink)

                try:
                    resultRelatedLink = result['inline_links']['related_pages_link']
                except:
                    resultRelatedLink = ''
                    pass
                #print('resultRelatedLink', resultRelatedLink)

                try:
                    resultRelatedAPILink = result['inline_links']['serpapi_related_pages_link']
                except:
                    resultRelatedAPILink = ''
                    pass
                #print('resultRelatedAPILink', resultRelatedAPILink)

                try:
                    resultVersionsQuantity = result['inline_links']['versions']['total']
                except:
                    resultVersionsQuantity = ''
                #print('resultVersionsQuantity', resultVersionsQuantity)


                try:
                    resultVersionsLink = result['inline_links']['versions']['link']
                except:
                    resultVersionsLink = ''
                
                #print('resultVersionsLink', resultVersionsLink)

                miniJSON = {
                    'resultPosition': resultPosition,
                    'resultTitle': resultTitle,
                    'resultLink': resultLink,
                    'resultID': resultID,
                    'resultSnippet': resultSnippet,
                    'resultPublicationInfoSummary': resultPublicationInfoSummary,
                    'resultAuthors': authorList, #resultAuthors,
                    'resultResourceTitle': resultResourceTitle,
                    'resultResourceFileFormat': resultResourceFileFormat,
                    'resultResourceLink': resultResourceLink,
                    'resultCiteLink': resultCiteLink,
                    'resultRelatedLink': resultRelatedLink,
                    'resultRelatedAPILink': resultRelatedAPILink,
                    'resultVersionsQuantity': resultVersionsQuantity,
                    'resultVersionsLink': resultVersionsLink
                }
                #print('###########################################################')
                #print('miniJSON', miniJSON)
                #print('###########################################################')

                miniJSONList.append(miniJSON)

                resultIndex += 1
                #print('resultIndex', resultIndex)

                if len(miniJSONList) > resultMax - 1:
                    break
#                if (resultIndex > resultMax - 1):
 #                   break

    #print('DONE!')

    lastValidResultIndex = lastValidResultIndex + startingIndex
    formattedJSON = {
        'searchSuccess': searchSuccess,
        'createdAtDateTime': createdAtDateTime,
        'searchURL': searchURL,
        'searchInfoOrganicState': searchInfoOrganicState,
        'searchInfoTotalResults': searchInfoTotalResults,
        'searchInfoQueryDisplayed': searchInfoQueryDisplayed,
        'searchInfoSpellingFixed': searchInfoSpellingFixed,
        'resultList': miniJSONList,
        'lastValidResultIndex': lastValidResultIndex
    }
    
    return(formattedJSON)





#ultimateRestult = searchScholarForKeywords(keywordSearch, startIndexForSearch)

#print('###########################################################')


#print(ultimateRestult)

#prettyJSON = json.dumps(json.loads(ultimateRestult[0]), indent=4)
#print('lastValidResultIndex', ultimateRestult[1])


#prettyJSON = json.dumps(ultimateRestult, indent=4)

#print(prettyJSON)

#print('###########################################################')
#print('###########################################################')

#print('miniJSONList', miniJSONList)

#json_string = ultimateRestult

# Save JSON string as file
#with open("ultimateRestult.json", "w") as f:
#    json.dump(json_string, f)


#flipperJson_object = json.dumps(flipperJson_object, indent=4)

#with open("ultimateRestult.json", "w") as outfile:
#    outfile.write(prettyJSON)

