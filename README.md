# slack botの作成
[このサイト](https://www.virtual-surfer.com/entry/2018/04/04/190000)の手順を参考に作成

## 投稿からurlを抽出し専用のチャンネルに投稿するbot
1. mkdir url_list
1. first commit
1. pyenv + virtualenvで専用のpython環境を作る
※設定を書きだすのは.bash_profileにする
+ 参考
[pyenv+anaconda](https://qiita.com/sk427/items/9f215931c8249ada75cd)
[virtualenv](https://qiita.com/shigechioyo/items/198211e84f8e0e9a5c18)
1. flake8+autopip8導入 (+Language Server Protocolも導入したいなぁ)
+ 参考
[pathogen.vim](https://laboradian.com/use-pathogen-vim/)
[syntastic](https://qiita.com/foloinfo/items/662007fcf4f802a19f3a)
[flake8](https://wonderwall.hatenablog.com/entry/2017/02/05/214004)

1. サイト通りに作業を進める(dotenvを使い公開で後悔しないようにする)
+ 参考
[GitHubに乗せたくない情報](https://yoshitaku-jp.hatenablog.com/entry/2018/03/31/396/)