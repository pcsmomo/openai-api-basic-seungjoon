import openai
import os

# Set your secret API key
# print(os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

# Start a completion
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="How to become famous youtuber",
    max_tokens=300
)

print(response)

# Output:
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\n1. Develop a Niche: Decide on a specific topic or theme that you want to focus on when making videos. Doing this will make it easier for viewers to recognize and remember your channel. It will also make it easier for you to be more consistent and focused when creating content.\n\n2. Improve Your Video Quality: Invest in a good camera, microphone, and lighting to improve the quality of your videos. You want your viewers to be able to easily see and hear your content. Your videos should be visually stimulating, so consider adding music, graphics, and other effects.\n\n3. Promote Your Channel: Utilize social media to help promote your channel. Network with other YouTubers, participate in blog or video comment sections, and create other channels for different topics or interests. You can also use SEO tactics, such as keyword research, to help increase your search engine rankings.\n\n4. Engage with Your Viewers: Take the time to respond to comments and messages your viewers send. This will show your viewers that you appreciate their support and help to create a sense of community.\n\n5. Experiment with Different Content: Try to mix up the content on your channel to keep your viewers engaged and interested. Consider making videos of different lengths and formats, and create announcements, live streams, and tutorial videos."
#     }
#   ],
#   "created": 1681025508,
#   "id": "cmpl-73JoaP9UzilwV7l94p6KW9IiCiUQn",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 275,
#     "prompt_tokens": 7,
#     "total_tokens": 282
#   }
# }
