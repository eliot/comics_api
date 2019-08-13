# Scraping Notes

- scrape from:
    - Comixology
    - Fandom
    - Wikipedia

## Comixology

### Sitemap URLS

https://www.comixology.com/sitemap.xml
https://www.comixology.com/Sitemap/1/sitemap_0.xml
https://www.comixology.com/Sitemap/1/sitemap_0.xml

### Sample pages

`Issue` model:

https://www.comixology.com/Detective-Comics-1937-2011-27/digital-comic/10900

- last URL component (`10900` here) can be incremented to go to the next comic

### Problems with Comixology
Comixology sometimes groups comics together e.g. #28-29, which we don't want.
[Find a example URL.]

### How do we know if a page is a Issue detail page?
e.g. https://www.comixology.com/Guerillas-1/digital-comic/12

URL is a 200
- URL follows pattern comixology.com/.+/digital-comic/(\d+)\?.+

Regex: https://regex101.com/r/w9UPr9/1

### 404
Example: https://www.comixology.com/Atomic-Robo-Vol-1-1-of-6/digital-comic/1
status code is in fact a 404, probably enough on it's own.

Page also says "Oops" `//*[@id="page_content_container"]/div[2]/div/div/div/h1`

## Fandom

