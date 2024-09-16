# TweetBot using Cloudflare Workers AI and Twitter API in Python

![Example of Generated Tweet image](https://github.com/elizabethsiegle/workers-ai-twitter-api-tweet/blob/main/lizziepika-generated-tweet.png?raw=true)

This application generates and posts tweets using Cloudflare Workers AI (specifically the Llama-3.1 model) and the Twitter (X) API to craft engaging and funny tweets according to pre-set prompts.

### Features
- AI-Powered Tweet Generation: Utilizes Cloudflare Workers AI (Llama-3.1) to create tweets based on predefined prompts.
- Twitter API Integration: Posts generated tweets directly to your Twitter account using [Tweepy](https://www.tweepy.org/).
- Customizable Tweet Prompts: You can easily modify the tweet prompts to fit your desired topics.

Prerequisites
Before you begin, ensure you have the following:

1. <strong>Cloudflare API Keys</strong>

- You need an `ACCOUNT_ID` and `AUTH_TOKEN` to use Cloudflare Workers AI.
- Visit the [Cloudflare Workers documentation](https://developers.cloudflare.com/workers/) to set up an account and get API keys.

2. <strong>Twitter API Keys</strong>
Obtain the following keys from the [Twitter Developer Portal](https://developer.twitter.com/en/apps):
- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`
Set up a developer account with Twitter (X) and create a project/app to obtain these keys.

3. <strong>.env File</strong>: Store all your keys in an `.env` file to ensure they are securely loaded into your environment. Example:

```bash
TWITTER_API_KEY=your-twitter-api-key
TWITTER_API_SECRET=your-twitter-api-secret
TWITTER_ACCESS_TOKEN=your-twitter-access-token
TWITTER_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
CLOUDFLARE_ACCOUNT_ID=your-cloudflare-account-id
CLOUDFLARE_AUTH_TOKEN=your-cloudflare-auth-token
```
### Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/elizabethsiegle/workers-ai-twitter-api-tweet.git
cd workers-ai-twitter-api-tweet
```
2. Install the required Python packages:
```bash
pip install tweepy python-dotenv requests
```
3. Set up your `.env` file with your Twitter and Cloudflare API keys as mentioned above.
4. Run the script:
```python
python3 cf-tweet.py
```

### How It Works
1. The app fetches a random tweet prompt from a list.
2. It sends the selected prompt to Cloudflare Workers AI (Llama-3.1), which generates a tweet.
3. The generated tweet is then posted on Twitter using Tweepy.
4. Error Handling: The app retries if any errors occur, such as exceeding the tweet character limit or encountering API restrictions.

### API Documentation
- Cloudflare Workers AI: [Cloudflare Workers AI Docs](https://developers.cloudflare.com/workers-ai/models/)
- Twitter (X) API: [Twitter API Docs](https://developer.x.com/en/docs)