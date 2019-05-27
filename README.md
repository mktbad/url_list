# slack botの作成

## 投稿からurlを抽出し専用のチャンネルに投稿するbot
1. mkdir url_list
1. first commit
1. pyenv + virtualenvで専用のpython環境を作る※設定を書きだすのは.bash_profileにする
    [pyenv+anaconda](https://qiita.com/sk427/items/9f215931c8249ada75cd)
    [virtualenv](https://qiita.com/shigechioyo/items/198211e84f8e0e9a5c18)
1. flake8+autopip8導入 (+Language Server Protocolも導入したいなぁ)
    [pathogen.vim](https://laboradian.com/use-pathogen-vim/)
    [syntastic](https://qiita.com/foloinfo/items/662007fcf4f802a19f3a)
    [flake8](https://wonderwall.hatenablog.com/entry/2017/02/05/214004)
1. [このページ](https://www.virtual-surfer.com/entry/2018/04/04/190000)通りに作業を進めてslack botのtokenを取得(dotenvを使い公開で後悔しないようにする)
    [dotenv](https://yoshitaku-jp.hatenablog.com/entry/2018/03/31/396/)
1. [この辺のslackclientの機能](https://slack.dev/python-slackclient/real_time_messaging.html#connecting-to-the-rtm-api)を使って投稿された文章からURLを抽出して投稿させる
    [pip install slackclient==2.0.0](https://github.com/slackapi/python-slackclient)
1. [この連載](https://www.virtual-surfer.com/archive/category/Python)を参考にHerokuにデプロイして常時実行する
