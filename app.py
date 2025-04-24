import streamlit as st
from twitter_fetcher import buscar_tweets

st.title("Tweets em Tempo Real - FURIA 🔥")
query = st.text_input("#FURIA, FURIA lang:pt, FURIA OR #GoFURIA")

if query:

    tweets = buscar_tweets(query)
    for tweet in tweets:
        st.write(f"> {tweet.text}"