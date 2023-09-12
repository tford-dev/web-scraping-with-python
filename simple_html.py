from bs4 import BeautifulSoup;

SIMPLE_HTML = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kardashian Names</title>
    </head>
    <body>
        <h1>List of Kardashian Names</h1>
        <p>I don't talk</p>
        <p>I don't walk</p>
        <p>I don't leave</p>
        <p class='subtitle'>But I don't stay</p>
        <ul>
            <li>Kim Kardashian</li>
            <li>Kourtney Kardashian</li>
            <li>Khloé Kardashian</li>
            <li>Kendall Jenner</li>
            <li>Kylie Jenner</li>
        </ul>
    </body>
    </html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser');

def find_title():
    h1_tag = simple_soup.find('h1').string;
    print(h1_tag);

first_li_string = simple_soup.find('li').string

def find_list_items():
    list_items = simple_soup.find_all('li');
    list_contents = [item.string for item in list_items]; #without comprehension, loop has <li> tags
    print(list_contents);

def find_subtitle():
    paragraph = simple_soup.find('p', {'class':'subtitle'})
    print(paragraph.string);

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p');
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])];
    print(other_paragraph[1].string);


find_title();
find_list_items();
find_subtitle();
find_other_paragraph();