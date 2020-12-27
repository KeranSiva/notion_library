import json
import requests


class BookScraper:
    def __init__(self):
        self.response = ""
        self.book_status = False
        self.book = ""

    def get_book_data(self, isbn):
        book = {}
        source_google = self.check_google(isbn)

        if source_google == True:
            book = self.call_google(isbn)
        else:
            source_open_library = self.check_open_library(isbn)
            if source_open_library == True:
                book = self.call_open_library(isbn)

        return book

    def check_google(self, isbn):
        google_status = False
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            if content["totalItems"] == 0:
                google_status = False
            elif content["totalItems"] == 1:
                google_status = True
                self.book = content["items"][0]["volumeInfo"]

        return google_status

    def check_open_library(self, isbn):
        open_library_status = False
        response = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:" + isbn + "&jscmd=details&format=json")
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            if len(content) == 0:
                open_library_status = False
            elif len(content) == 1:
                open_library_status = True
                self.book = content["ISBN:"+isbn]["details"]

        return open_library_status

    def call_google(self, isbn):
            book = {}
            try:
                book['title'] = self.book['title']
            except KeyError:
                pass

            try:
                book['subtitle'] = self.book['subtitle']
            except KeyError:
                pass

            # TODO: Split Authors
            try:
                listToStr = ';'.join(map(str, self.book['authors']))
                book['authors'] = listToStr
            except KeyError:
                pass

            try:
                book['publishedDate'] = self.book['publishedDate']
            except KeyError:
                pass

            try:
                book['publisher'] = self.book['publisher']
            except KeyError:
                pass

            try:
                book['description'] = self.book['description']
            except KeyError:
                pass

            try:
                book['pageCount'] = str(self.book['pageCount'])
            except KeyError:
                pass

            try:
                book['categories'] = self.book['categories']
            except KeyError:
                pass

            return book

    def call_open_library(self, isbn):
        book = {}
        try:
            book['title'] = self.book['title']
        except KeyError:
            pass

        try:
            book['subtitle'] = self.book['subtitle']
        except KeyError:
            pass

        # TODO: Split Authors
        try:
            book['authors'] = self.book['authors'][0]['name']
        except KeyError:
            pass

        try:
            book['publishedDate'] = self.book['publish_date']
        except KeyError:
            pass

        try:
            book['publisher'] = self.book['publishers'][0]
        except KeyError:
            pass

        try:
            book['description'] = self.book['description']
        except KeyError:
            pass

        try:
            book['pageCount'] = str(self.book['number_of_pages'])
        except KeyError:
            pass

        try:
            book['categories'] = self.book['categories']
        except KeyError:
            pass

        return book