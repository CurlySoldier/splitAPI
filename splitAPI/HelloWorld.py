from flask_restful import Resource

class HelloWorld(Resource):
        """
        Represents a simple hello world endpoint.
        """

        def get(self):
                """
                A simple hello world endpoint
                ---
                responses:
                        200:
                                description: Hello world message
                        500:
                                description: Undocumented error
                """
                return {'message': 'Hello, World!'}
        
        def post(self):
                """
                A simple hello world endpoint
                ---
                responses:
                        200:
                                description: Hello world message
                        500:
                                description: Undocumented error
                """
                return {'message': 'Hello, World!'}