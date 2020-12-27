from notionHandler import NotionHandler
from scraper import BookScraper
import logging

if __name__ == '__main__':
    logging.info("Verbindung zu Notion wird hergestellt")
    notion_handler = NotionHandler()
    rows = notion_handler.get_library_data()

    logging.info("Verbindung zur Books API wird hergestellt")
    book_scraper = BookScraper()

    for row in rows:

        if row.get_property("title") == "" or row.get_property("authors") == "":
            logging.info("Eintrag wird verarbeitet")
            isbn = row.get_property("isbn")
            book_data = book_scraper.get_book_data(isbn)
            notion_handler.write_book(book_data, row)


    logging.info("Bearbeitung erledigt")
