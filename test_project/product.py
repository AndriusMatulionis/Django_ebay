import uuid

ATTRIBUTES = {
        'item': ('h3', {'class': 's-item__title'}),
        'condition': ('span', {'class': 'SECONDARY_INFO'}),
        'price': ('span', {'class': 's-item__price'}),
        'location': ('span', {'class': 's-item__location s-item__itemLocation'}),
        'seller': ('span', {'class': 's-item__etrs-text'}),
        'url': ('a', {'class': 's-item__link'}),
    }

class Product:
    def __init__(self, scraped_block=None):
        self.price = getattr(scraped_block.find(ATTRIBUTES['price'][0], attrs=ATTRIBUTES['price'][1]), 'text', None)
        self.item = getattr(scraped_block.find(ATTRIBUTES['item'][0], attrs=ATTRIBUTES['item'][1]), 'text', None)
        self.condition = getattr(scraped_block.find(ATTRIBUTES['condition'][0], attrs=ATTRIBUTES['condition'][1]), 'text', None)
        self.location = getattr(scraped_block.find(ATTRIBUTES['location'][0], attrs=ATTRIBUTES['location'][1]), 'text', None)
        self.seller = getattr(scraped_block.find(ATTRIBUTES['seller'][0], attrs=ATTRIBUTES['seller'][1]), 'text', None)
        self.url = scraped_block.find('a').get('href')
        self.scraped_block = scraped_block
