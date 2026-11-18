
from flask import Flask
import mariadb
from config import DB_CONFIG

app = Flask(__name__)


def get_connection():
    return mariadb.connect(**DB_CONFIG)


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Kasvatetaan käyntimäärää yhdellä
        cursor.execute("""
            UPDATE counter
            SET visits = visits + 1
            WHERE id = 1
        """)

        conn.commit()

        # Haetaan uusi käyntimäärä
        cursor.execute("""
            SELECT visits FROM counter
            WHERE id = 1
        """)

        visits = cursor.fetchone()[0]

    finally:
        cursor.close()
        conn.close()

    return f"""
    <!DOCTYPE html>
    <html lang="fi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">

        <title>Viikko 2 - Python ja MariaDB</title>

        <style>
            body {{
                margin: 0;
                padding: 50px 20px;
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
            }}

            .container {{
                max-width: 700px;
                margin: auto;
                padding: 40px;
                background: #1e293b;
                border-radius: 20px;
            }}

            h1 {{
                color: #38bdf8;
            }}

            .counter {{
                font-size: 75px;
                color: #4ade80;
                font-weight: bold;
                margin: 30px;
            }}

            .info {{
                background: #334155;
                padding: 20px;
                border-radius: 12px;
                margin-top: 25px;
                line-height: 1.7;
            }}

            a {{
                color: #38bdf8;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Python-verkkosovellus</h1>

            <p>
                No mutta tervetuloa viikon 2 palvelimelle!
            </p>

            <h2>Sivun käyntimäärä</h2>

            <div class="counter">{visits}</div>

            <p>
                Jokainen sivun lataus kasvattaa laskuria.
            </p>

            <div class="info">

                <h2>Tekninen toteutus</h2>

                <p>
                    Sovellus on toteutettu Pythonilla
                    käyttäen Flask-sovelluskehystä.
                </p>

                <p>
                    Nginx toimii välityspalvelimena
                    ja Gunicorn suorittaa Python-sovellusta.
                </p>

                <h2>Tietokanta</h2>

                <p>
                    Kävijälaskurin tiedot tallennetaan
                    MariaDB-tietokantaan.
                    Jokainen sivulataus kasvattaa
                    tietokannan visits-arvoa yhdellä.
                </p>

                <h2>Uudelleenkäynnistystesti</h2>

                <p>
                    Virtuaalikone  käynnistettiin uudelleen 4.11.2026 onnistuneesti. Nginx, Mariadb ja Python-sovellus käynnistyivät automaattisesti oikein. Kävijälaskurin arvo säilyi. Testi onnistui!
                </p>
<h2>Viikon 1 verkkosivu</h2>

<p>
    <a href="/">
        Takaisin viikon 1 etusivulle
    </a>
</p>
                <h2>Tällainen tuli tällä kertaa</h2>

                <p>
                    <a href="https://github.com/SallaHei/viikko2_linux">
                        GitHub-repository
                    </a>
                </p>

            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
