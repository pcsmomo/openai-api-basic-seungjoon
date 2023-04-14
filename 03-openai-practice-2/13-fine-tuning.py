import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# before we train
prompt = f"What is Walmart revenue in 2022?"
response = openai.Completion.create(
    model="text-babbage-001",
    prompt=prompt,
    max_tokens=300,
)
print("before...")
print(response['choices'][0]['text'])

# Result
# Walmart's expected revenue for 2022 is $119.4 billion.

prompt = f"What is Walmart revenue in 2022?"
response = openai.Completion.create(
    model="babbage:ft-personal-2023-04-14-21-48-15",
    prompt=prompt,
    max_tokens=300,
)
print("after...")
print(response['choices'][0]['text'])

# Result
#  $466 Billion. Compares to $118 billion in 2016 and an increase of 35% since 2014.

# Why is Walmart's revenue growing? Lower prices in all markets since 2012. Growing online sales and more shoppers
# ordering online than ever before. Expanded presence in online grocery, in-store sales and via online and catalog as a factor.
# Method: Top 10/100 Leading Markets• USA: $866 billion• EMEA: $694 billion• China: $646 billion• India: $582 billion•
# POS: $347 billionOne of management's top drivers is the importance of offering low prices.
# This is clearly acknowledged in the CEO's forward-thinking and relentless focus on cost-less pricing.
# To ensure, prices wins, Walmart has worked very hard to buy-down prices from these retailers and still beat it.
# A leader in cost-free (direct) pricing, which cuts costs across the board.
# This is similar to Walmart's low prices in its home state of Arkansas.
# By 2017 cost-free in Arkansas, Walmart will save $1 billion.
# Also has the advantage of convenient trading, it doesn't hurt that Walmart has its distribution centers in locations where Amazon does not.
# Product Innovation: Diet Coke• 13M actively marketed diet coke to Pepsi drinkers.
# • New flavors in Diet Coke Rocket fuel bar business for years with intense marketing
# • Skergas, Dadanchick (then Mad&Cool) aggressive advertising on soda shop TV & Radio.
# • Walmart strategies to
