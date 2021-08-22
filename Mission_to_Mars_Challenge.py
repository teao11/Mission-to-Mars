l#!/usr/bin/env python
# coding: utf-8

# # Original Code

# In[530]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[531]:


# Set your executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[532]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[533]:


# Set the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[534]:


# Scrape the div block wth class content_title
slide_elem.find('div', class_='content_title')


# In[535]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[536]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[537]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[538]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[539]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[540]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[541]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Data from Table

# In[542]:


# Read HTML into a DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[543]:


# End browser session
browser.quit() 


# # Pasted code from the challenge

# In[544]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[545]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[546]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[547]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[548]:


slide_elem.find('div', class_='content_title')


# In[549]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[550]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[551]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[552]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[553]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[554]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[555]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[556]:


### Mars Facts


# In[557]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[558]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[559]:


df.to_html()


# In[560]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# In[561]:


### Hemispheres


# In[562]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[563]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[564]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Convert the browser to HTML object and then soup object
html = browser.html
hemisphere_soup = soup(html, 'html.parser')


# Find all of the relevant images
image_links = hemisphere_soup.find_all('div', class_='description')

# Loop through the images tags
for link in image_links:

    # Click the link
    img_href = link.find('a').get('href')
    img_url = f"{url}{img_href}"
    browser.visit(img_url)
    
    # New Soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Find container and URL
    container = img_soup.find('div', class_='downloads')
    full_image_url = container.find('a').get("href")
    complete_url = f"{url}{full_image_url}"
    
    # Find the Title
    container = img_soup.find('div', class_='cover')
    title = container.find("h2").text
    
    hemisphere_image_urls.append({
        'img_url': complete_url,
        'title': title
    })


# In[565]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[566]:


# 5. Quit the browser
browser.quit()

