# openai-api-basic-seungjoon

OpenAI API Basic by Seungjoon Lee, InFlearn

# Details

<details open> 
  <summary>Click to Contract/Expend</summary>

## Section 1. OpenAI API Basic

### 4. Text Completion API

- [OpenAI Platform](https://platform.openai.com/)
- [OpenAI API Doc - Text Completion](https://platform.openai.com/docs/guides/completion)
- [OpenAI Pricing](https://openai.com/pricing)

#### Upgrdae python and poetry versions up-to-date

```sh
brew update && brew upgrade pyenv
pyenv install 3.11.3
pyenv global 3.11.3
# restart the terminal
poetry self update

python --version
# Python 3.11.3
poetry --version
# Poetry (version 1.4.2)
```

#### project folder setup

```sh
mkdir 01-openapi-basic
cd 01-openapi-basic
poetry init
poetry add openai

```

```sh
# Chdck poetry config
poetry config --list
# virtualenvs.create = true
# virtualenvs.in-project = true
```

- Python: Select Interpreter
  - `{PATH}/01-openai-basic/.venv/bin/python3`

```sh
poetry shell
export OPENAI_API_KEY={MY_OPENAI_API_KEY} && python 01-text_completion.py
```

</details>
