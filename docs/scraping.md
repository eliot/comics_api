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

## Fandom

