from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    #get data from url
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    shiba = requests.get("https://shibe.online/api/shibes?count=3")

    apikey = ""
    response2 = requests.get("https://pokeapi.co/api/v2/pokemon/ditto"+ "?apikey=" + apikey)
    #transform too JSON format
    data = response.json() #hi
    name = ""
    shiba_data = shiba.json()
    image = data["sprites"]["front_default"]
    return render_template("index.html", poke_src=image, shiba_src = shiba_data)


if __name__ == "__main__":
    app.run()
