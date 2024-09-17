import streamlit as st
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
    "Compare the rapid evolution of AI to Taylor Swift's reinvention across her music eras. What's the '1989' of AI breakthroughs?",
    "Describe the feeling of deploying a Cloudflare Worker that fixes a major issue.",
    "Explain the importance of internet speed optimization using an analogy about running a marathon through the streets of San Francisco.",
    "What if Cloudflare was a superhero? Explain how its features (like DDoS protection) defend websites from villains like 'Lag' and 'Downtime.'",
    "How is training an AI model like prepping for a major pickleball tournament? Consistency, feedback, and improving with every match!",
    "Describe the thrill of biking up a steep San Francisco hill as an analogy for solving a critical, high-priority bug.",
    "Imagine a tennis match where each shot is a request to a server—describe the rally as Cloudflare Workers handle the volleys.",
    "What if Taylor Swift wrote a song about the highs and lows of AI development? What would the chorus be?",
    "Use the process of training for a marathon race to explain how large language models improve with more data—step by step, faster each time.",
    "Compare and contrast San Francisco's housing crisis with the complexity of maintaining backward compatibility in software updates.",
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

# Streamlit app
def main():
    # Set page config
    st.set_page_config(page_title="Tweet Generator", page_icon="🐦", layout="wide")

    # Custom CSS to set the background color and style the button container
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1DA1F2;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .white-container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 0 auto 2rem;  /* Added bottom margin */
        }
        .tweet-button {
            display: block;
            width: auto;  /* Changed from 100% to auto */
            padding: 0.5rem 1rem;  /* Reduced padding */
            background-color: #1DA1F2;
            color: white !important;
            font-size: 1rem;  /* Reduced font size */
            border: none;
            border-radius: 30px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            text-align: center;
            text-decoration: none;
            margin: 0 auto;  /* Center the button */
            display: block;  /* Ensure it's a block element */
        }
        .tweet-button:hover {
            background-color: #0d8bd8;
        }
        .tweet-header {
            color: #1DA1F2;
            text-align: center;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        .profile-section {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        .profile-pic {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background-color: #1DA1F2;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 10px;
            font-size: 24px;
        }
        .user-details {
            font-size: 14px;
            color: #14171A;
        }
        .user-details strong {
            display: block;
            font-size: 16px;
        }
        #MainMenu {visibility: hidden;}
        footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #5c2358;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 16px;
        }
        .stButton > button {
            background-color: white;
            color: #1DA1F2 !important;
            border: 2px solid #1DA1F2;
            padding: 0.5rem 1rem;  /* Reduced padding */
            font-size: 1rem;  /* Reduced font size */
            border-radius: 30px;
            cursor: pointer;
            transition: background-color 0.3s ease, color 0.3s ease;
            text-align: center;
            width: auto;  /* Changed from 100% to auto */
            font-weight: bold;
            margin: 0 auto;  /* Center the button */
            display: block;  /* Ensure it's a block element */
        }
        .stButton > button:hover {
            background-color: #1DA1F2;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create a container to center the content vertically
    with st.container():
        # Add some vertical space
        for _ in range(3):
            st.write("")

        # Use columns to center the content horizontally
        _, center_col, _ = st.columns([1, 2, 1])

        with center_col:
            st.markdown(
                """
                <div class="white-container">
                    <h1 class="tweet-header">Generate Tweet</h1>
                    <div class="profile-section">
                        <div class="profile-pic">👩🏻‍💻</div>
                        <div class="user-details">
                            <strong><a href="https://x.com/lizziepika">@lizziepika</a></strong>
                            <span>San Francisco, CA</span>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Add some vertical space
            st.write("")
            
            # Create the button outside the white-container
            if st.button("Tweet!", key="generate-tweet-btn"):
                with st.spinner("Generating and posting tweet..."):
                    new_tweet()
                st.success("Tweet posted successfully!")

    # Add the footer
    st.markdown(
        """
        <footer>
            Made with ❤️ in SF🌁 => <a href="https://github.com/elizabethsiegle/workers-ai-twitter-api-tweet/tree/main">👩🏻‍💻 on GitHub</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()