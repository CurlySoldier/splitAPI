from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from HelloWorld import HelloWorld



# Add Swagger UI endpoint
template = {
    "swagger": "2.0",
    "info": {
        "title": "Split API",
        "description": "A simple API for splitting bills between friends",
        "contact": {
        "responsibleOrganization": "Split",
        "responsibleDeveloper": "Chad Chandrapaul",
        "email": "Chad.chandrapaul@gmail.com"
        },
}
}

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template)

@app.route('/swagger')
def swagger_ui():
        return swagger.swagger_static()

api.add_resource(HelloWorld, '/HelloWorld')

if __name__ == '__main__':
        app.run(debug=True)
