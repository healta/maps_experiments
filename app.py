from flask import Flask, render_template
import folium
import json

app = Flask(__name__)

mayors_dict = {"Vratsa": "GERB", "Alfatar": "GERB", "Antonovo":"DPS"}

party_dict = {"GERB": "blue", "DPS":"orange"}


def style_function(feature):
    city = feature["properties"]["name_2"]
    if city in mayors_dict:
        if mayors_dict[city] in party_dict:
            return {
                "fillColor": party_dict[mayors_dict[city]],
                "color": "black",
                "weight": 2,
                "fillOpacity": 0.5,
            }
    else:
        return {
            "fillColor": "gray",
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.5,
        }


@app.route("/")
def home():
    map = folium.Map(location=[42.43278, 25.64194])
    with open(
        r"E:\Programming\maps_experiments\stanford-jf267dx3808-geojson.json",
        "r",
        encoding="latin1",
    ) as json_file:
        geojson_data = json.load(json_file)
    folium.GeoJson(
        geojson_data, name="Shapefile Data", style_function=style_function
    ).add_to(map)
    map.save("map.html")
    for feature in geojson_data["features"]:
        print(feature["properties"]["name_2"])

    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
