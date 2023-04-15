import openai
import os
import numpy as np
import pandas as pd
from common.token_helper import num_tokens_from_string

openai.api_key = os.getenv("OPENAI_API_KEY")


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']


# download csv file from my google drive
# https://drive.google.com/file/d/1zCKtgJrqGG8BRCHtQ72JYeiJEvKei3Ab/view?usp=sharing
df = pd.read_csv("14-embedded_fortune_1k_revenue.csv")
print(df.head())

query = "what was Amazon revenues"
# query = "what was Netflix total employees"

# https://platform.openai.com/docs/guides/embeddings/second-generation-models
tokenizer = "cl100k_base"

# total token
total_token = num_tokens_from_string(
    string=query, encoding_name=tokenizer)
print(f"total_token: {total_token}")
# total_token: 4

total_price_est = total_token / 1000 * 0.0004
print(f"total_price_est: ${total_price_est}")
# total_price_est: $0.0000016


query_vector = get_embedding(text=query)
# print(query_vector)

# Check the score of the first row
print(cosine_similarity(
    np.array(np.matrix(df['ada_embedding'][0])).ravel(), query_vector))
# 0.7604243298473069

df['cosine_similarity'] = df['ada_embedding'].apply(
    lambda v: cosine_similarity(np.array(np.matrix(v)).ravel(), query_vector))

print(df['cosine_similarity'])
# 0      0.760424
# 1      0.855542
# 2      0.769538
# 3      0.739172
# 4      0.721871
#          ...
# 995    0.745717
# 996    0.737279
# 997    0.763816
# 998    0.748198
# 999    0.746091

most_similar_index = np.argmax(df['cosine_similarity'])
print(f"Most similar sentence:: {df['info'][most_similar_index]}")
# Most similar sentence:: Amazon has $469,822 revenues, $1,658,807.30 market value and 1,608,000 employees

# To avoid model hallucination
embeded_prompt = f"""answer only if you are 100% certain
Reference: {df['info'][most_similar_index]}

Question: {query}
Answer: """

print("------------------------------")
print(embeded_prompt)
print("------------------------------")
# """
# Most similar sentence:: Amazon has $469,822 revenues, $1,658,807.30 market value and 1,608,000 employees
# ------------------------------
# answer only if you are 100% certain
# Reference: Amazon has $469,822 revenues, $1,658,807.30 market value and 1,608,000 employees

# Question: what was Amazon revenues
# Answer:
# ------------------------------
# """


response = openai.Completion.create(
    model="text-davinci-003",
    prompt=embeded_prompt,
    max_tokens=300,
)
print(f"openai answer: {response['choices'][0]['text']}")
#  $469,822
