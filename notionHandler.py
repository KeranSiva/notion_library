from notion.client import NotionClient
import logging


class NotionHandler:
    def __init__(self):
        self.client = ""

    def get_library_data(self):
        token = #TODO ADD YOUR LOGIN TOKEN HERE
        tracker_url = #TODO ADD YOUR COLLECTION URL HERE
        self.client = NotionClient(token_v2=token)
        collection_view = self.client.get_collection_view(tracker_url)
        _rows = collection_view.collection.get_rows()


        return _rows
    
    
    def write_book(self, book, row):
        logging.info("Eintrag wird geschrieben")
        try:
            row.set_property('title', book['title'])
        except:
            pass

        try:
            row.set_property('subtitle', book['subtitle'])
        except:
            pass

        try:
            row.set_property('authors', book['authors'])
        except:
            pass

        try:
            row.set_property('Year', book['publishedDate'])
        except:
            pass

        try:
            row.set_property('publisher', book['publisher'])
        except:
            pass

        try:
            row.set_property('pages', book['pageCount'])
        except:
            pass

        try:
            row.set_property('categories', book['categories'])
        except:
            pass

        try:
            row.set_property('summary', book['description'])
        except:
            pass