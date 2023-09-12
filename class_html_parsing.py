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

class ParsedItemLocator:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    def __init__(self, page):
        self.page = BeautifulSoup(page, 'html.parser');

    
    def name(self, attr):
        locator = ParsedItemLocator.NAME_LOCATOR #h3 and a are nested in article tag...css locator
        item_link = self.page.select_one(locator);
        item_name = item_link.attrs[attr];
        return item_name;
    
    def find_float_my_version(self):
        paragraphs = self.page.find_all('p');
        paragraph_list = [p for p in paragraphs if 'price_color' in p.attrs.get('class', [])];
        original_str = paragraph_list[0].string;
        result_str = float(original_str.replace('£', ''));
        return result_str;
  
    def find_float_video(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.page.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        print(matcher.group(0)); #£51.77
        return float(matcher.group(1)); #51.77

    #The class in the tag in the p tag indicates the rating
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR;
        star_rating_tag = self.page.select_one(locator);
        classes = star_rating_tag.attrs['class'] #outputs 2 classes
        rating_classes = [r for r in classes if r != 'star-rating'];
        return rating_classes[0]


parser = ParsedItem(ITEM_HTML);
print(parser.name('title'));
print(parser.name('href'));
print(parser.find_float_my_version());
print(parser.find_float_video());
print(parser.rating());