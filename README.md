# openai-api-basic-seungjoon

OpenAI API Basic by Seungjoon Lee, InFlearn

# Details

<details open> 
  <summary>Click to Contract/Expend</summary>

## Section 1. OpenAI API Basic

### 4. Text Completion API

- [OpenAI Platform](https://platform.openai.com/)
- [OpenAI API Playground](https://platform.openai.com/playground)
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

### 5. Completion API Parameters

- [OpenAI API Models](https://platform.openai.com/docs/models/overview)
  - GPT-4
  - GPT-3.5
    - text-davinci-003
    - code-davinci-002
  - GTP-3
    - text-curie-001
    - text-babbage-001
    - text-ada-001
  - ...
- [Complete Call Parameters](https://platform.openai.com/docs/api-reference/completions/create)
  - prompt
  - temperature: creativity
  - max_tokens
  - top_p: nucleus sampling, an alternative to sampling with temperature
  - frequency_penalty
  - presence_penalty
  - best_of
  - stop: let model know when to stop
    - text_complete: `\n`
    - code_complete: `;` or `#`

### 6. query with code-davinci-002

[Code completion has been deprecated as of March 2023](https://platform.openai.com/docs/guides/code/code-completion-deprecated)

```sh
openai.error.InvalidRequestError: The model: `code-davinci-002` does not exist
```

</details>
