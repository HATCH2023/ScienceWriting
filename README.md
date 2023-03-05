# Science Writing


HERE IS OUR VIDEO:  
https://www.canva.com/design/DAFcQQ6hDC8/sJLK8e7Ay8Q2ynC_aCtJCg/view?utm_content=DAFcQQ6hDC8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


Inspiration
We were inspired by science communicators and wanted to help solve the challenges they face trying to maximize content generation. We are also extremely interested in learning Artificial Intelligence and automation, so this challenge met all marks.

What it does
Scriptor allows science writers to input keywords, which then kicks off an AI automation content generator. Scriptor returns Scientific Articles based on the keywords and provides a snippet of the article's content. The user then selects which article they want to generate content from. Next, Scriptor outputs a Press Release, Blog, AI-generated images, and posts for Facebook, LinkedIn, Instagram, and Twitter.
The user is able to edit the text for each content platform as well as select which image to upload. Once the user is done editing, they submit the content for approval from their supervisor. The supervisor can then further edit and approve the content for distribution. Distribution to the social media platforms is fully automated and can either be published immediately or scheduled for a future date and time.

How we built it
Scriptor's front-end was built using the Vue User Interface and the back-end is supported using Python. API integrations are made with OpenAI for their Text (GPT 3.5) and Image (DALL-E) generators. Additionally, APIs were integrated for searching Google Scholar for Scientific Articles and Facebook/LinkedIn/Instagram/Twitter posts.

Challenges we ran into
What's a hackathon without challenges? Here are some that we faced: Many Scientific Articles are behind paywalls, so it took a while to find some that were not. Additionally, importing those articles into our back-end was met with many obstacles since the layout of the articles differ by publisher. Since this was our first experience with AI, there was a bit of a learning curve learning how to use the integration, however, we had lots of fun in the process. Additionally, the current GPT AI models are not made to ingest large amount of data. Our scientific articles average thousands of words. We had to get extremely creative in order to ingest the article by breaking the article into chunks and taking action on the chunks, then recombining later. We had some trouble trying to set up a cloud infrastructure for our project. And after a while, we determined since cloud was not a requirement, that we would just run our app locally.

Accomplishments that we're proud of
We have a Product! We are so happy that Scriptor is working and is able to execute all of the main tasks we gave it. We celebrated every time we accomplished a 'to-do' task. "WooHoo!"

What we learned
We learned that integrating many different websites and distributing content to social media platforms is a little harder than we thought. We learned a lot of python. And we also learned that Artificial Intelligence is very awesome and fun to program with. We also spoke with a few professional science communicators and received their feedback on Scriptor. We gained a lot of perspective on their field and learned about ethics as well as certain writers bias.

What's next for Scriptor
We are putting together a Business Plan, but there are some finishing touches needed first. We would like to incorporate a few more features based on an overall User Interface and User Experience survey. We also plan to include more sources for article searches and figure our other ways to have inputs for the user in order to add additional parameters from which to generate their content. We would like to include Single-Sign-On (SSO) for Scriptor. Also, we'd like to enhance the editing process by automatically integrating with the Organization's Style Guide. There is potential to auto-generate podcasts and automated emails sent to scientists for further research. Scriptor will also be able to ingest videos from YouTube or other video sources, converting their audio to text in order for our automation engine to generate content.

Hackathon Goals:
IMPACT: Scriptor provides an endless amount of quality science communication for organizations. Scriptor solves the significant problem with organizations being able to increase output without increasing staff. It utilizes the latest technologies in AI and is applicable to not just the science field, but all organizations with public relations and Search Engine Optimization.

CREATIVITY: Scriptor is a new and unique product that addresses the current needs of the market. There is no product available which performs all of the complicated tasks with integrated AI and automation. This allows for organizations to increase output by several factors.

COMPLEXITY: The team pretty much started from scratch during the event. Some of the team have experience programming, but everyone learned a lot during the hackathon. We had no previous experience with AI integrations and now we do. It is a LOT of fun.

PRODUCT: Scriptor is user friendly and intuitive. We conducted UI/UX surveys and incorporated feedback into our application. Although our product is currently available as a demo for HATCH 2023, we plan to continue development, create a business plan, and push it to market.
