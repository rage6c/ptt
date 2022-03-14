import flask
from flask import Flask, request

from TestDto import TestDto
from utils.RequestTypeConvertor import RequestTypeConvertor

app = Flask(__name__)


@app.route("/test", methods=["POST"])
@RequestTypeConvertor.convert_to(TestDto)
def test(test_dto: TestDto):
    app.logger.info("------------------" + str(test_dto.a))
    return test_dto.to_json()


@app.before_request
def before():
    app.logger.info("Request URL:" + request.url + "; Body:" + str(request.data))


@app.after_request
def after(response):
    app.logger.info("Response: " + response.status + "; Body:"
                    + response.data.decode("utf-8").replace("\n", "").replace("\r", ""))
    return response


@app.errorhandler(500)
def handle_internal_error(ex):
    app.logger.error(ex)
    return flask.make_response("Server Error", 500)


@app.errorhandler(400)
def handle_bad_request(ex):
    app.logger.error(ex)
    return flask.make_response("Bad Request", 500)


app.run(host='0.0.0.0', port=8080, debug=True)
