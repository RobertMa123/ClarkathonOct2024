# ClarkathonOct2024
Lead Paint
using Quick Dive is fairly straight forward. After running app.py, follow the url it provides to the site that it makes. In it, provide a hobby that you are interested in into the first field. Alternatively, you can simply click the suprise me box to get a random keyword. Then, provide a number of communities you would like to recieve from the social medias. Lastly, select the social medias you are interested in seeing communities from. They will be provided in a drop down menu below, and selecting one will provide you with a short description of the community and an embeded link to visit it.

## Inspiration
As people very involved in online communities, we have noticed they can be difficult to get into when starting from the outside. People with less experience exploring the internet may feel excluded or locked out from said communities. We wanted to lower the barrier to entry, and help the communities grow in size.

## What it does
Quick dive searches a series of popular social media sites for groups relating to provided keywords, and compiles them for the user to visit. To help the user make an informed decision, it reads the current trending posts and description to synthesize its own description of the community. Additionally, when reading the posts, if it detects any events being planned, it will mention those in a separate area to ensure the user notices it.

## How we built it
We chose social media sites with strong communities to pull from, and, using various search methods depending on the platform, scanned for groups that fit providable keywords. The backend is in python, and the front end is in html. In order to make the descriptions, once navigating to the page in question, we used scraping tools like beautiful soup to read in the trending posts and prompted Gemini to describe the community based on those posts and look for events being planned.

## Challenges we ran into
We attempted to use many different web scraping methods for different social media sites, most of which were dead ends. The time we spent researching them was lost. We also frequently had to sacrifice our work when we spent hours working on dead ends. 
Something frustrating was learning that many social media companies wanted us to pay to use their APIs. Other API’s required a registration/verification process that could not be completed within the time scope of this project.

## Accomplishments that we're proud of
We met all of our goals on time
We used good teamwork and got a lot done
Compiling a large input of information into an organized, concise, and accessible form
finding ways to get information from sites without their api’s (either paid or wouldn’t provide permissions within the timeframe)

## What we learned
We learned how to do web scraping, how to work with different social media sites’ APIs, how to set up a website that’s accessible and user-friendly, and how to use Google's API. 

## What's next for Quick Dive

Better/more searches: due to permission constraints, we’ve not been able to include as many platforms as we wished. We plan to expand the platform option list to instagram, discord, etc for a wider range of options for the user.
Location-based searching: We’ve discussed the idea of allowing users to connect more locally more than once during this project. Our future plans include using GPS services to show users events and locations related to the community they want to join (map showing music show locations, cat cafes for people interested in cats, etc).
Trending communities tab
Host the website


