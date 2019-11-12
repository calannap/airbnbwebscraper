import json


class InfoModel:
    def __init__(self, title, image_urls, description, amenities):
        self.title = title
        self.amenities = amenities
        self.image_urls = image_urls
        self.description = description

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
