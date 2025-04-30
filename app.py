import streamlit as st
import tweepy
import datetime

# Chave da API v2 (Bearer Token)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAACxU0wEAAAAAR3sNwylor5OJKHK2VAgORcdxE5k%3DtZYHrZXSZl0kgbZafmTULK4nMb5EusQDq1Ec6z47IprXMRe9ow"

# Inicializa o client da API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Função para buscar tweets recentes
def buscar_tweets(query, max_results=5):
    ontem = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    response = client.search_recent_tweets(
        query=f"{query} lang:pt",
        start_time=ontem.isoformat("T") + "Z",
        max_results=max_results,
        tweet_fields=["created_at", "author_id", "lang"]
    )
    return response.data

# Interface streamlit
st.title("Busca de Tweets")
query = st.text_input("Digite o termo para busca", "#FURIA")

if st.button("Buscar Tweets"):
    tweets = buscar_tweets(query)
    if tweets:
        for tweet in tweets:
            st.write(f"🗣️ Tweet ID {tweet.id}: {tweet.text}")
    else:
        st.write("Nenhum tweet encontrado.")
