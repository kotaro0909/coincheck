# Memo
## 参考リンク
- [板情報・価格・注文・約定APIの利用](https://di-acc2.com/programming/python/4599/)
- [Pythonでサクッと仮想通貨データを取得する方法](https://lifetechia.com/crypto-data/)

## 備忘
- Python
  - [pandasでCSVファイルの書き込み・追記（to_csv）](https://note.nkmk.me/python-pandas-to-csv/)
  - [Python命名規則一覧](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)
  - [pandas.DataFrame.to_jsonの基本的な使い方](https://note.nkmk.me/python-pandas-to-json/)
  - [Pythonで関数オーバーロード](https://www.python.digibeatrix.com/functions-classes/python-function-overloading-methods/)
  - [Pythonでprintを卒業してログ出力をいい感じにする](https://qiita.com/FukuharaYohei/items/92795107032c8c0bfd19)
  - [【Python入門】Pythonのロギングと真剣に向き合う](https://www.true-fly.com/entry/2021/11/22/073000)
    - 日時でローテート 
      - [TimedRotatingFileHandler](https://docs.python.org/ja/3.13/library/logging.handlers.html#timedrotatingfilehandler) 
        - [Python ログローテーションの時間経過による設定方法](https://qiita.com/takei-s/items/766fdbea8d1fbc082653)
        - [Pythonによるログローテーションの実装](https://qiita.com/OkomeChike/items/143ef35b3e2a2672938d)
    - ファイルサイズでローテート
      - [Pythonでログファイルをローテーション出力する|デバッグが楽に。](https://kamedassou.com/python_out_log/)
      - [Pythonでログファイルをローテーションさせる方法](https://jimaru.blog/programming/python/log-rotation/)

- 取引はCCTXを使う
  - [CCTX Manual](https://github.com/ccxt/ccxt/wiki/manual)
  
- 過去データはYahoo Financeを使う
  - [【Python】仮想通貨・ビットコイン価格の過去データ取得方法2選｜ヒストリカルデータ分析に基づく自動売買実現に向けて](https://di-acc2.com/programming/python/15678/)
  - [yfinance documentation](https://ranaroussi.github.io/yfinance/)
  
- CoinCheckの操作
  - [Coin Checkl 取引所 API 概要](https://coincheck.com/ja/documents/exchange/api#about)
  - [【Python】コインチェックAPIの取得と自動売買の実践手順｜Coincheck仮想通貨・ビットコイン取引機能入門](https://di-acc2.com/programming/python/15316/)

## 環境
- DB:MariaDB / userid:root / password:root
  - [MariaDB公式](https://mariadb.com/docs/)
  - [【Python】MariaDB連携](https://zenn.dev/ringotabetai/articles/19369244a2318c)
  - [MySQLの照合順序とは？設定・変更方法と最適な選び方を徹底解説](https://www.dbtech.digibeatrix.com/mysql/server-config/mysql-collation-guide/)
  - [MariaDB(MySQL)の照合順序の話](https://blog.ver001.com/mariadb_collation/)
  - [MySQL で使える主な型一覧](https://qiita.com/gogonosmarty/items/6d6d770276f39326a2ce)
  - [PythonxMariaDB完全ガイド](https://www.dbtech.digibeatrix.com/integration-environment/programming-languages/python-mariadb-guide/)
