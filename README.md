# twitter-scouter
## Description
Twitterを使ったエンジニア採用

## UI
### Top
![スクリーンショット 2019-04-20 12 47 19](https://user-images.githubusercontent.com/13377817/56452272-1b2b8c00-636b-11e9-8d50-8d87701a490e.png)
### Dashboard
![スクリーンショット 2019-04-24 16 36 47](https://user-images.githubusercontent.com/13377817/56641022-530a3a80-66af-11e9-9c1d-a17f775ec541.png)

## Requirement
- Python 3.7.3
  - pyenv + pipenv
- Django 2.1.3
- PostgreSQL

## Usage
- Install pyenv
```
% brew install pyenv
% echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
% echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
% echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
% exec $SHELL -l
```
- Install pipenv
```
% brew install pipenv
% echo 'eval "$(pipenv --completion)”' >> ~/.bash_profile
% exec $SHELL -l
```

```
# git clone this repositocy
% pipenv install --dev
% pipenv shell
% python main.py runserver
```

- setting all-auth
  - `localhost:8000/admin`
```
adminページ> 外部アカウントのsocial applications
 Providor → Twitter
 Name → Twitter
 Client id →　{Your Consumer Key (API Key)}
 Secret key → {Your Consumer Secret (API Secret)}
 Sites → Chosen sitesにexample.comを追加
```

- Database
  - ダンプファイルのリストア
```
% psql twitter_scouter < backup.dump
```



サーバ起動
```
% python manaeg.py runserver
```

