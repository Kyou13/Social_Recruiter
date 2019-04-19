# twitter-scouter
## Description
Twitterを使ったエンジニア採用

## Requirement
- Python3.6
  - pyenv + pipenv
- Django2.1.3

## Usage
- Install pyenv
```
% brew install pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
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
