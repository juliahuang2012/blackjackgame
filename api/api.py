import httpx
def getpokemon(name):
    response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    body = response.json
    content = response.json()
    return content

def getpokemonabilities(name):
    pokemon = getpokemon(name)
    abilities = pokemon["abilities"]
    result = []
    for ability in abilities:
        result.append(
            ability["ability"]["name"]
        )
    return result




#print(getpokemon("charizard"))
(input("Enter a pokemon"))
print(getpokemonabilities(input))