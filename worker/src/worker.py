import json
from http import HTTPStatus

from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from utils import get_light


def create_app():
    app = Flask(__name__)

    swaggerui_blueprint = get_swaggerui_blueprint(
        "/swagger",
        "/api/",
        config={"app_name": "Worker"},
    )

    app.register_blueprint(swaggerui_blueprint)

    @app.route("/api/")
    def api():
        swag = swagger(app)
        swag["info"]["version"] = "1.0"
        swag["info"]["title"] = "Logs manager"
        return jsonify(swag)

    @app.route("/", methods=["GET"])
    def health():
        """
        Проверка работоспособности API
        ---
        :return:
        """
        return "", HTTPStatus.OK

    @app.route('/', methods=['POST'])
    def get_humidity():
        import datetime
        return json.dumps([get_light(datetime.datetime.now()), get_humidity()])

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
