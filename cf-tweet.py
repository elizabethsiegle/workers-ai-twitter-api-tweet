from dotenv import load_dotenv
import tweepy
import random
import requests
import os

# Retrieve API keys, tokens from env vars
load_dotenv()
twitter_api_key = os.environ.get("TWITTER_API_KEY")
twitter_api_secret = os.environ.get("TWITTER_API_SECRET") 
twitter_access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")

# Initialize Tweepy client
twitter_client = tweepy.Client(
    consumer_key=twitter_api_key,
    consumer_secret=twitter_api_secret,
    access_token=twitter_access_token,
    access_token_secret=twitter_access_token_secret
)

# List of tweet prompts
tweet_prompts = [
    "Compare the rapid evolution of AI to Taylor Swift's reinvention across her music eras. What’s the '1989' of AI breakthroughs?",
    "Describe the feeling of deploying a Cloudflare Worker that fixes a major issue.",
    "Explain the importance of internet speed optimization using an analogy about running a marathon through the streets of San Francisco.",
    "What if Cloudflare was a superhero? Explain how its features (like DDoS protection) defend websites from villains like 'Lag' and 'Downtime.'",
    "How is training an AI model like prepping for a major pickleball tournament? Consistency, feedback, and improving with every match!",
    "Describe the thrill of biking up a steep San Francisco hill as an analogy for solving a critical, high-priority bug.",
    "Imagine a tennis match where each shot is a request to a server—describe the rally as Cloudflare Workers handle the volleys.",
    "What if Taylor Swift wrote a song about the highs and lows of AI development? What would the chorus be?",
    "Use the process of training for a marathon race to explain how large language models improve with more data—step by step, faster each time.",
    "Compare and contrast San Francisco’s housing crisis with the complexity of maintaining backward compatibility in software updates.",
    "Describe a software release day with Cloudflare protection as if it were Taylor Swift releasing an album—smooth, fast, and ready to handle the traffic.",
    "Compare the feeling of finishing a long-distance bike ride in San Francisco to the satisfaction of deploying a resilient Cloudflare Worker.",
    "Explain the complexity of serverless computing using an analogy from a doubles tennis match, where coordination is key.",
    "If Cloudflare Workers were to play pickleball, how would they outsmart latency and win every point?",
    "Describe AI algorithms using a metaphor about navigating San Francisco's complex housing market—always learning, always adapting.",
    "Explain a distributed denial-of-service (DDoS) attack using a humorous analogy involving tennis balls and Taylor Swift fans camping out for tickets.",
    "Use the exhilaration of hitting a perfect ace in tennis to describe launching a successful Cloudflare Worker into production.",
    "How does cloud infrastructure evolve, like Taylor Swift's music over the years? From acoustic beginnings to powerhouse tech.",
    "Imagine a conversation between Cloudflare and a large language model discussing how they're shaping the future of the internet—what would they say?"
]

def generate_tweet():
    response = requests.post(
    f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
        "messages": [
            {"role": "system", "content": "My Twitter account is @Lizziepika. I tweet about my work as a Cloudflare developer advocate, tennis, biking, running, San Francisco, and Taylor Swift. Come up with concise and interesting tweets that are bound to garner attention from related communities like the developer community."},
            {"role": "user", "content": f"Return only one tweet according to the following prompt and nothing else. {random.choice(tweet_prompts)}"}
        ]
        }
    )
    print(f"response {response.json()['result']['response']}")
    result = response.json()['result']['response']
    return result
  
def new_tweet():
  while True:
    try:
        new_tweet = generate_tweet()
        response = twitter_client.create_tweet(text =str(new_tweet))
        print(response.data["text"])
        break # exit loop if successful
    except tweepy.errors.Forbidden as e:
        print("403 Forbidden Err")
        pass
    except Exception as e:
        if "Your Tweet text is too long" in str(e):
            print("Tweet too long")
            pass
        else:
            raise e 

# Post a tweet
new_tweet()