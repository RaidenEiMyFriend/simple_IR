# Simple search engine with python 3

Search engine using Vector Space Model. The data will be crawled from Vietnamese daily news such as [VnExpress](https://vnexpress.net/), [VietnamNet](http://vietnamnet.vn/), [Thanhnien](https://thanhnien.vn/) and [Laodong](https://laodong.vn/).


## Usage

- Run `index.py` script to perform indexing data. The indexed data will be created (if not exists) or updated and stored in `db/` directory.

    ```bash
    $ python index.py
    ```

- Run `search.py` script and pass a query string for it.

    ```bash
    $ python search.py "Your query string here"
    ```

    For example:

    ```bash
    $ python search.py "Trump Trieu Tien"
    https://vnexpress.net/tin-tuc/the-gioi/trump-noi-cuoc-gap-voi-kim-jong-un-van-co-the-dien-ra-vao-12-6-3754763.html - 0.32331036424704196
    https://vnexpress.net/tin-tuc/the-gioi/trump-huy-cuoc-gap-voi-lanh-dao-trieu-tien-3754245.html - 0.3158077661308892
    https://vnexpress.net/tin-tuc/the-gioi/trump-thuc-giuc-trung-quoc-that-chat-bien-gioi-voi-trieu-tien-3752746.html - 0.3017484484730665
    https://vnexpress.net/tin-tuc/the-gioi/abe-noi-se-gap-trump-truoc-cuoc-hop-thuong-dinh-my-trieu-3755808.html - 0.30059730510834515
    http://vietnamnet.vn/vn/the-gioi/binh-luan-quoc-te/nhung-nga-re-chop-nhoang-kho-luong-cua-thuong-dinh-trump-kim-453759.html - 0.2990576238183994
    https://vnexpress.net/tin-tuc/the-gioi/ngoai-truong-my-giai-thich-ly-do-cuoc-gap-trump-kim-bi-huy-3754252.html - 0.2807074203562179
    https://vnexpress.net/tin-tuc/the-gioi/han-quoc-hop-khan-sau-khi-trump-tuyen-bo-huy-gap-kim-jong-un-3754256.html - 0.24340889391647347
    https://vnexpress.net/tin-tuc/the-gioi/my-canh-bao-trieu-tien-co-the-chiu-chung-so-phan-nhu-libya-3753226.html - 0.24232103427164864
    ...
    ```

    > The above query results may be changed because indexed data can be updated. To get updated index, run `git pull origin windows` command.
- For app: Run `app.py` and click the url given in your terminal (something like http://127.0.0.1:5000)
