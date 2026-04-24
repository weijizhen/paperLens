from venues import CRAWLER_REGISTER

def main():
    for venue_name, crawler_class in CRAWLER_REGISTER.items():
        crawler = crawler_class()
        crawler.crawl()


if __name__ == '__main__':
    main()

