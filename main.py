from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo',  # Можно использовать и другие типы. For example "face/clipart/video/ and ext"
        #color='blackandwhite',
        size='large',
        #license='noncommercial, commercial',
        #date=((2022, 1, 1), (2022, 2, 1))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    # max/min_size="" - доп параметр.
    # overwrite - перезапись уже имеющихся изображение внутри директории img.(по дефолту стоит False)
    crawler.crawl(
        keyword='Spange Bob',
        max_num=5,
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
    )


def main():
    google_img_downloader()


if __name__ == main():
    main()
