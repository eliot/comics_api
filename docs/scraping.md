# Scraping Notes

- scrape from:
    - Comixology
    - Fandom
    - Wikipedia

## Comixology scraping

### Sitemap URLS

https://www.comixology.com/sitemap.xml
https://www.comixology.com/Sitemap/1/sitemap_0.xml
https://www.comixology.com/Sitemap/1/sitemap_0.xml

### Issue Item properties
* url
* issue_id
* title
* issue_number
* issue_number_end
* multi_issue
* series
* series_url
* price
* cover_url
* description
* publisher
* publisher_url
* writers
* writers_urls
* artists
* artists_urls
* colors
* colors_urls
* inks
* inks_urls
* pencils
* pencils_urls
* story_arc
* story_arc_url
* page_count
* release_date_print
* release_date_digital
* age_rating
* sold_by
* genre_names
* genre_urls
* genres
* collected_edition_url
* ratings_count
* star_rating


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

### 404 handling
Example: https://www.comixology.com/Atomic-Robo-Vol-1-1-of-6/digital-comic/1
status code is in fact a 404, probably enough on it's own.

Page also says "Oops" `//*[@id="page_content_container"]/div[2]/div/div/div/h1`

### Example: Multiple authors
Multiple authors: https://www.comixology.com/Sakura-Pakk-vs-Rumble-Pak-Bleed-MidSummers-Dream/digital-comic/52
Example of multiple inkers: https://www.comixology.com/X-Men-Chronicles-2/digital-comic/5000

### Example: No description disclaimer
The lack of disclaimer in the description caused my Xpath query to break.
https://www.comixology.com/X-Men-Chronicles-2/digital-comic/5000?r=1

### Example: Title does not contain '#'
Title does not contain '#' to signify issue number, which breaks this collected edition
https://www.comixology.com/The-Best-of-Archie-Comics-Deluxe-Edition/digital-comic/417673

### Example: price = FREE
https://www.comixology.com/Sakura-Pakk-vs-Rumble-Pak-Bleed-MidSummers-Dream/digital-comic/52

### Example: combined issue
E.g. Issue 28 and 29 are combined into one comixology "issue"

https://www.comixology.com/Detective-Comics-1937-2011-28-29/digital-comic/10901

### Example: Captain Blood: Odyssey #1 (of 5)
https://www.comixology.com/Captain-Blood-Odyssey-1-of-5/digital-comic/77


## Fandom scraping

## Image comics scraping (Image comics website)
useful fields:
- Age rating (different from Comixology)
- cover price
- Diamond ID [what is this?, Is this even useful?]
