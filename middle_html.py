import re;
from bs4 import BeautifulSoup;

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser');

def find_item_name(attr):
    locator = 'article.product_pod h3 a'; #h3 and a are nested in article tag...css locator
    item_link = soup.select_one(locator);
    item_name = item_link.attrs[attr];
    print(item_name);

def find_float_my_version():
    paragraphs = soup.find_all('p');
    paragraph_list = [p for p in paragraphs if 'price_color' in p.attrs.get('class', [])];
    original_str = paragraph_list[0].string;
    result_str = float(original_str.replace('£', ''));
    print(result_str);


def find_float_video():
    locator = 'article.product_pod p.price_color';
    item_price = soup.select_one(locator).string
    pattern = '£([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_price)
    print(matcher.group(0)); #£51.77
    print(float(matcher.group(1))); #51.77

#The class in the tag in the p tag indicates the rating
def find_item_rating():
    locator = 'article.product_pod p.star-rating';
    star_rating_tag = soup.select_one(locator);
    classes = star_rating_tag.attrs['class'] #outputs 2 classes
    rating_classes = [r for r in classes if r != 'star-rating'];
    print(rating_classes[0]);


find_item_name('title');
find_item_name('href');
find_float_my_version();
find_float_video();
find_item_rating();