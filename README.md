# twitter-scouter
## Description
Twitterを使ったエンジニア採用

![スクリーンショット 2019-04-20 12 47 19](https://user-images.githubusercontent.com/13377817/56452272-1b2b8c00-636b-11e9-8d50-8d87701a490e.png)
## Requirement
- Python3.6
  - pyenv + pipenv
- Django2.1.3

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
