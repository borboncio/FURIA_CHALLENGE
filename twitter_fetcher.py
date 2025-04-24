import tweepy
#from config import BEARER_TOKEN

def buscar_tweets(query, max_resultados=10):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    print(f"Buscando tweets com o termo: {query}")  # Debug
    try:
        resposta = client.search_recent_tweets(query=query, max_results=max_resultados)
        if not resposta.data:
            print("Nenhum tweet encontrado.")
        else:
            for i, tweet in enumerate(resposta.data, 1):
                print(f"{i}. {tweet.text}")
    except tweepy.errors.TooManyRequests as e:
        print("Erro: Muitas requisições. Tente novamente mais tarde.")
    except Exception as e:
        print(f"Erro na requisição: {e}")

def testar_conexao():
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    try:
        user = client.get_me()
        print(f"Conectado com sucesso! Usuário: {user.data['username']}")
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")


# Teste
if __name__ == "__main__":
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACxU0wEAAAAA0tCmEFGM135qL%2FEI8JQSIKZsCTI%3D8switvpFR1puMOxNBPK9VDhEBe2QrI4k3hemTZ0xgkqwu7RTUF'
    testar_conexao()
    termo = "#FURIA"
    buscar_tweets(termo)