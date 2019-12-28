from flask import Flask, request, Response
from flask_cors import CORS

from Business import IdeaBusiness

app = Flask(__name__)
CORS(app)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
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


if __name__ == '__main__':
    app.run()
