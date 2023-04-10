from typing import List
import openai
import os
import random

openai.api_key = os.getenv("OPENAI_API_KEY")

ingredient_list = [
    "kimchi",
    "ham",
    "seedweed",
    "tuna",
    "beef",
    "bacon",
    "apple",
    "onion",
    "salmon",
    "ramen"
]


def pick_ingredient(picked_ingredient_list: List[str]):
    picked_ingredient = random.choice(ingredient_list)

    # if picked_ingredient is already in picked_ingredient_list:
    if picked_ingredient_list.count(picked_ingredient):
        picked_ingredient = pick_ingredient(picked_ingredient_list)

    return picked_ingredient


def get_ingredients(count: int = 3):
    picked_ingredient_list = []

    for _ in range(count):
        picked_ingredient = pick_ingredient(picked_ingredient_list)
        picked_ingredient_list.append(picked_ingredient)

    return picked_ingredient_list


lst = get_ingredients(3)
print(f"Given ingrdients: {','.join(lst)}")

# Ask OpenAI to generate a recipe
text_response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Given the following ingredients: {','.join(lst)} what can I cook? provide the instruction steps. Plus, provide the name of cooking title on the first line",
    max_tokens=300,
    temperature=0.7
)

output = text_response['choices'][0]['text'].strip('\n')
output_list = output.split("\n")
title = output_list[0]
instructions = '\n'.join(output_list[1:])
print(f"Title: {title}")
print(f"{instructions}")

# Generate an image
image_response = openai.Image.create(
    prompt=title,
    model="image-alpha-001",
    size="256x256",
    response_format="url"
)

# Print the URL of the generated image
print(image_response["data"][0]["url"])


print('\n== Text Response ==')
print(text_response)

print('\n== Image Response ==')
print(image_response)

# Given ingrdients: apple,beef,salmon


# Title: Apple Salmon Beef Bowl
# Instructions:
# 1. Cut the beef into small cubes and marinate with salt, pepper and garlic powder.
# 2. Heat oil in a pan over medium-high heat. Add the beef cubes and cook until browned. Set aside.
# 3. Cut the apple into wedges and add to the same pan. Cook until lightly browned.
# 4. Add the salmon fillet to the pan and cook until lightly browned and cooked through.
# 5. Add the cooked beef and apple to the pan with the salmon.
# 6. Mix together and cook for an additional 5 minutes.
# 7. Serve in a bowl. Enjoy!

# https://oaidalleapiprodscus.blob.core.windows.net/private/org-gLCtXyaA7aD0Tjof0bYJ8GkI/user-c9gctj0DJT5qKXMbdyZDrN2d/img-pnisPr5m3OidbzUGJdsnnPTS.png?st=2023-04-10T09%3A34%3A37Z&se=2023-04-10T11%3A34%3A37Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-10T09%3A23%3A51Z&ske=2023-04-11T09%3A23%3A51Z&sks=b&skv=2021-08-06&sig=KMgYCbfGjvyAwmvkJlPUe0vUiFuHqAHKejaNvwi0xqg%3D


# == Text Response ==
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nApple Salmon Beef Bowl\nInstructions:\n1. Cut the beef into small cubes and marinate with salt, pepper and garlic powder.\n2. Heat oil in a pan over medium-high heat. Add the beef cubes and cook until browned. Set aside.\n3. Cut the apple into wedges and add to the same pan. Cook until lightly browned.\n4. Add the salmon fillet to the pan and cook until lightly browned and cooked through.\n5. Add the cooked beef and apple to the pan with the salmon.\n6. Mix together and cook for an additional 5 minutes.\n7. Serve in a bowl. Enjoy!"
#     }
#   ],
#   "created": 1681122868,
#   "id": "cmpl-73j8uexePgEZaHHemsIqPNfO4NZS0",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 139,
#     "prompt_tokens": 34,
#     "total_tokens": 173
#   }
# }

# == Imgae Raw Response ==
# {
#   "created": 1681122877,
#   "data": [
#     {
#       "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-gLCtXyaA7aD0Tjof0bYJ8GkI/user-c9gctj0DJT5qKXMbdyZDrN2d/img-pnisPr5m3OidbzUGJdsnnPTS.png?st=2023-04-10T09%3A34%3A37Z&se=2023-04-10T11%3A34%3A37Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-10T09%3A23%3A51Z&ske=2023-04-11T09%3A23%3A51Z&sks=b&skv=2021-08-06&sig=KMgYCbfGjvyAwmvkJlPUe0vUiFuHqAHKejaNvwi0xqg%3D"
#     }
#   ]
# }
