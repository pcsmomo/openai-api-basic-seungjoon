import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Provide the korean history question including 4 possible choices " +
    "and provide the correct answer\n the answer format start with 'Answer:'",
    max_tokens=300,
    temperature=0.7
)

print(response)
print(response['choices'][0]['text'])


# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nQuestion: Who was the first king of the Joseon Dynasty?\nA. Sejong the Great\nB. Gojong of Goryeo\nC. Taejo of Joseon\nD. Gwangjong of Goryeo\n\nAnswer: C. Taejo of Joseon"
#     }
#   ],
#   "created": 1681118659,
#   "id": "cmpl-73i31B0TJP1txwQBRpBs1DBLf2HlE",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 64,
#     "prompt_tokens": 25,
#     "total_tokens": 89
#   }
# }


# 1st Result
# Question: Who was the first king of the Joseon Dynasty?
# A. Sejong the Great
# B. Gojong of Goryeo
# C. Taejo of Joseon
# D. Gwangjong of Goryeo

# Answer: C. Taejo of Joseon"


# 2nd Result
# Q: Who was the first ruler of the Goryeo Dynasty?
# A. Sejong the Great
# B. Gojong of Goryeo
# C. King Wang Geon
# D. King Taejo

# Answer: C. King Wang Geon
