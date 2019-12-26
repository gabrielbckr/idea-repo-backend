from flask import Flask, request, Response, jsonify, json
from Business import IdeaBusiness

app = Flask(__name__)

ideaBusiness = IdeaBusiness.IdeaBusiness()


@app.route("/get-ideas", methods=["GET"])
def getIdeas():
    responseContent = ideaBusiness.GetIdeas()
    return Response(responseContent, mimetype='application/json')


@app.route("/add-idea", methods=["POST"])
def addIdea():
    data = request.get_json()
    ideaBusiness.SaveIdea(data["title"], data["contact"], data["description"], data["wholeIdea"])
    return "200"


@app.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = '*'
    return response


if __name__ == '__main__':
    app.run()
