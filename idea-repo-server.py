from flask import Flask, request
from Business import IdeaBusiness

app = Flask(__name__)

ideaBusiness = IdeaBusiness.IdeaBusiness()


@app.route("/get-ideas", methods=["GET"])
def getIdeas():
    return ideaBusiness.GetIdeas()


@app.route("/add-idea", methods=["POST"])
def addIdea():
    title = request.form['title']
    description = request.form['description']
    wholeIdea = request.form['wholeIdea']
    ideaBusiness.SaveIdea({title, description, wholeIdea})
    pass


if __name__ == '__main__':
    app.run()
