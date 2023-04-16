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

# using .env
poetry self add poetry-dotenv-plugin
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

### 7. Prompt Engineer

#### Reverse Prompt Engineering

- [Blog - Reverse Prompt Engineering for Fun and (no) Profit](https://www.latent.space/p/reverse-prompt-eng)
- [Jail Break - find a weak point](https://www.jailbreakchat.com/)

#### Best practice

[OpenAI API - Text completion - Prompt design](https://platform.openai.com/docs/guides/completion/prompt-design)

- Be clear and specific
- Use natural language
  - for model to capture nuances and subtitles of human language
- Include relavant keywords or initial response
- Experiment with different prompt structures
  - question-based or statement or partial sentence
- Fine-tune the prompt
  - adjust wording
  - adding or removing keywords
  - try different sentence structure

### 9. Blog Writer

- [bluehost - affordable hosting site](https://www.bluehost.com/)
- [Blog design template](https://www.bootdey.com/snippets/view/Blog-Detail-App#html)

```sh
poetry add jinja2

# ./04-blog-writer
export OPENAI_API_KEY={MY_OPENAI_API_KEY} && python blog-writer.py
```

## Section 3. OpenAI API Practice 2

### 10. Sentiment Analysis with Reddit API

```sh
poetry install
poetry self add poetry-dotenv-plugin
# poetry add dotenv # cannot install it: not supporting PEP 517 builds.
poetry add praw
```

- [Create Reddit API Key](https://www.reddit.com/prefs/apps)
  - Create an app
    - name: sentiment-test
    - Type: script

### 11. Auto Docstring

#### Docstring example

- one-line docstrings
- multi-line docstrings
- reStructuredText(reST) docstrings

### 12. Translate News

[News API](https://newsapi.org)

### 13. Fine Tuning

- Any proprietary data can be possible to train the GPT models
- Fine tuning has already the base model, so it saves resources.

- [OpenAI API - Fine Tuning](https://platform.openai.com/docs/guides/fine-tuning)
- [tiktoken - Calculate token number](https://github.com/openai/tiktoken)
  - then we could estimate the cost

#### Data prep tool

##### Calculate token

```sh
poetry add tiktoken
```

##### prepare jsonl file

- File format: CSV, TSV, XLSX, JSON or JSONL
  - JSONL is preferred

```sh
poetry add pandas

openai tools fine_tunes.prepare_data -f 13-fine-tuning-data.json
# Analyzing...

# - Your JSON file appears to be in a JSONL format. Your file will be converted to JSONL format
# - Your file contains 2 prompt-completion pairs. In general, we recommend having at least a few hundred examples. We've found that performance tends to linearly increase for every doubling of the number of examples
# - All prompts end with suffix ` revenue in 2022?`. This suffix seems very long. Consider replacing with a shorter suffix, such as ` ->`
# - All prompts start with prefix `What is `
# - All completions end with suffix ` billion`
# - The completion should start with a whitespace character (` `). This tends to produce better results due to the tokenization we use. See https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset for more details

# Based on the analysis we will perform the following actions:
# - [Necessary] Your format `JSON` will be converted to `JSONL`
# - [Recommended] Add a whitespace character to the beginning of the completion [Y/n]: Y


# Your data will be written to a new JSONL file. Proceed [Y/n]: Y

# Wrote modified file to `13-fine-tuning-data_prepared.jsonl`
# Feel free to take a look!

# Now use that file when fine-tuning:
# > openai api fine_tunes.create -t "13-fine-tuning-data_prepared.jsonl"

# After you’ve fine-tuned a model, remember that your prompt has to end with the indicator string ` revenue in 2022?` for the model to start generating completions, rather than continuing with the prompt. Make sure to include `stop=[" billion"]` so that the generated texts ends at the expected place.
# Once your model starts training, it'll approximately take 2.47 minutes to train a `curie` model, and less for `ada` and `babbage`. Queue will approximately take half an hour per job ahead of you.
```

#### Create fine tuned model based on

```sh
# openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
openai api fine_tunes.create -t 13-02-fine-tuning-data_prepared.jsonl -m babbage
# Upload progress: 100%|████████████████████████████████████████████████| 149/149 [00:00<00:00, 115kit/s]
# Uploaded file from 13-02-fine-tuning-data_prepared.jsonl: file-ffC5ivwRCSZtxFCuOM5pD1eU
# Created fine-tune: ft-ZFYwZVBlLizaqJVHDJ3KWCMY
# Streaming events until fine-tuning is complete...

# (Ctrl-C will interrupt the stream, but not cancel the fine-tune)
# [2023-04-15 07:47:20] Created fine-tune: ft-ZFYwZVBlLizaqJVHDJ3KWCMY
# [2023-04-15 07:47:32] Fine-tune costs $0.00
# [2023-04-15 07:47:32] Fine-tune enqueued. Queue number: 0
# [2023-04-15 07:47:33] Fine-tune started
# [2023-04-15 07:47:53] Completed epoch 1/4
# [2023-04-15 07:47:53] Completed epoch 2/4
# [2023-04-15 07:47:54] Completed epoch 3/4
# [2023-04-15 07:47:54] Completed epoch 4/4
# [2023-04-15 07:48:15] Uploaded model: babbage:ft-personal-2023-04-14-21-48-15
# [2023-04-15 07:48:16] Uploaded result file: file-YgcV1vrbi2LYf6cABR5z1y7o
# [2023-04-15 07:48:16] Fine-tune succeeded

# Job complete! Status: succeeded 🎉
# Try out your fine-tuned model:

# openai api completions.create -m babbage:ft-personal-2023-04-14-21-48-15 -p <YOUR_PROMPT>
```

> It takes some time. If you want to check the progress

```sh
# openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
openai api fine_tunes.follow -i ft-ZFYwZVBlLizaqJVHDJ3KWCMY
```

#### use OpenAI API with my fine tuned model

```sh
python 13-fine-tuning.py
```

### 14. Use Text Embedding and Find Document Similarity

[OpenAI API - Embeddings](https://platform.openai.com/docs/guides/embeddings)

#### Model Hallucination

- Model hallucination referes to **a phenomenon where an AI language model, like ChatGPT, generates output that seems plausible but is not accurate, factual, or relavant to the input it has received.**
- Causes can be
  - incomplete, biases or incorrect traning dataset
  - over-generalized from the training dataset
  - the model attempts to generate uncertain response
- Solution
  - add "answer only if you are 100% centain"

#### Step 1: generate embedded file

[14-fortune_1000_revenue_2022.csv](./03-openai-practice-2/data/14-fortune_1000_revenue_2022.csv)

```sh
python 14-01-text-embedding.py
# it will add two columns, "info" and "ada_embedding" to the csv file.
```

#### Step 2: find the most similar info and ask to chat gpt

```sh
python 14-02-document-similarity.py
```

### 15. ChatGPT API - Chat completion

#### ChatGPT API Role

- sytstem: assign the specific situation and response style
- user: you
- assistant: ChatGPT

#### Models

- [OpenAI API Models](https://platform.openai.com/docs/models/overview)

</details>
