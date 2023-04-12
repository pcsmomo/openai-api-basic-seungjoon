import inspect
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def reverse_string(string: str) -> str:
    return string[::-1]


print(inspect.getsource(reverse_string))

prompt = f"Provide python docstring for the following function: \n ```{inspect.getsource(reverse_string)}```"
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=300,
)
print(response['choices'][0]['text'])


##########################################################
# result:
def reverse_string(string: str) -> str:
    """
    Returns the reverse of a given string.

    :param string: str -- The input string to be reversed
    :return: str -- The reversed string
    """
    return string[::-1]


print(help(reverse_string))
# Help on function reverse_string in module __main__:


# reverse_string(string: str) -> str
#     Returns the reverse of a given string.

#     :param string: str -- The input string to be reversed
#     :return: str -- The reversed string

print(reverse_string.__doc__)
# Returns the reverse of a given string.

# :param string: str -- The input string to be reversed
# :return: str -- The reversed string
