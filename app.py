from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")


app = Flask(__name__)

@app.route('/status', methods=['GET']) 
def get_status():
    return "Hello World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) # Erhalte den Port aus der Environment Variable, sonst benutze 8080 
    app.run(host='0.0.0.0', port=port) # Starte die App
