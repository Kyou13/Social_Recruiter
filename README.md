# social_recruiter
## 実行環境
- 言語：Python3.6
- Webフレームワーク:Django2.1
- webサーバ:Nginx + gunicorn
- AWS EC2 Ubuntu 16.04

## 画面
- ログイン
- Twitterユーザリストアップ
- 設定

## DB
- Engineer_DB
    - user_id
    - ユーザ名
    - 自己紹介
    - フォロー数
    - フォロワー数

- Follower_DB    
    - user_id

- Config_DB    
    - サービス利用者名
    - 会社名？
    - DM定型文
    - 検索ワード

## EC2環境で実行
gunicorn your_project.wsgi --bind=0.0.0.0:8000 -D

## TODO
- アカウント情報入力時、求人情報も
- フロントでのみID１から
- 位置情報カラムに追加
- follow follower いる？表示形式検討
- 高速化
  - とりあえずキャッシュサーバは使いたい(勉強のため)
- 常時SSL化
- 静的ファイル配置
- 類似度
  - COS類似度とか
  - 何で文字列を定量化するかは検討
  - 多分処理めちゃ重くなるから,Apache beam使いたい
- エラー画面
- お気に入りユーザ解除
- ユーザ検索クエリリセット

