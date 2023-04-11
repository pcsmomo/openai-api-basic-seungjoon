import openai
import os
from jinja2 import Environment, FileSystemLoader

blog_title = "Let's learn Python History"
prompt = f"""
Biography - My name is Noah. I am working as a web developer
Blog Title - {blog_title}
Tags - Python, Technology, Coding, Machine Learning
Write the blog based on the information above, starting with my bio introduction
"""

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
)
content = response['choices'][0]['text'].replace('\n', '<br />')

# Load the template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the content
html = template.render(content=content, title=blog_title)

# Write the HTML file
with open('blog.html', 'w') as f:
    f.write(html)

print('Done! Check the blog.html file')
