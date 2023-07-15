from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def home():
    map = folium.Map(location = [42.43278, 25.64194])
    return map._repr_html_()

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=3000)