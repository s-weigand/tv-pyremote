"""V1 implementation."""
from typing import Dict

from flask import Flask
from flask_restx import Api, Resource, cors

from ..interactions import map_role


def init_api(app: Flask) -> None:
    """Initialize REST-API.

    Parameters
    ----------
    app : Flask
        Flask app instance, that the API should be added to.
    """
    api = Api(
        app,
        version="1.0",
        doc="/api/v1",
        title="TodoMVC API",
        description="A simple TodoMVC API",
    )

    ns = api.namespace(
        "api/v1/role",
        description="TODO operations",
        decorators=[cors.crossdomain(origin="http://localhost:1234")],
    )

    # todo = api.model(
    #     "Todo",
    #     {
    #         "id": fields.Integer(readonly=True, description="The task unique identifier"),
    #         "task": fields.String(required=True, description="The task details"),
    #     },
    # )

    # class TodoDAO(object):
    #     def __init__(self):
    #         self.counter = 0
    #         self.todos = []

    #     def get(self, id):
    #         """Retrieve Todos."""
    #         for todo in self.todos:
    #             if todo["id"] == id:
    #                 return todo
    #         api.abort(404, "Todo {} doesn't exist".format(id))

    #     def create(self, data):
    #         """Create todo.

    #         Parameters
    #         ----------
    #         data : Dict[str, Any]
    #             Sent data.

    #         Returns
    #         -------
    #         Dict[str, Any]
    #             [description]
    #         """
    #         todo = data
    #         todo["id"] = self.counter = self.counter + 1
    #         self.todos.append(todo)
    #         return todo

    #     def update(self, id, data):
    #         todo = self.get(id)
    #         todo.update(data)
    #         return todo

    #     def delete(self, id):
    #         todo = self.get(id)
    #         self.todos.remove(todo)

    # DAO = TodoDAO()
    # DAO.create({"task": "Build an API"})
    # DAO.create({"task": "?????"})
    # DAO.create({"task": "profit!"})

    @ns.route("/<role>")
    @ns.param("role", "keys to press")
    class TodoList(Resource):
        """Shows a list of all todos, and lets you POST to add new tasks."""

        @ns.doc("role")
        # @ns.marshal_list_with(todo)
        def get(self, role: str) -> Dict[str, str]:
            """Trigger task mapped to role.

            Parameters
            ----------
            role : str
                Role of the control which was clicked.

            Returns
            -------
            Dict[str, str]
                Status message
            """
            print(role)
            resp = map_role(role)
            print("resp=: ", resp)
            return resp
            # return {"role": role}

        # @ns.doc("create_todo")
        # @ns.expect(todo)
        # # @ns.marshal_with(todo, code=201)
        # def post(self, key_str):
        #     """Create a new task."""
        #     resp = press_keys(key_str)
        #     print("resp=: ", resp)
        #     return resp
        # return DAO.create(api.payload), 201

    # @ns.route("/<int:id>")
    # @ns.response(404, "Todo not found")
    # @ns.param("id", "The task identifier")
    # class Todo(Resource):
    #     """Show a single todo item and lets you delete them."""

    #     @ns.doc("get_todo")
    #     @ns.marshal_with(todo)
    #     def get(self, id):
    #         """Fetch a given resource."""
    #         return DAO.get(id)

    #     @ns.doc("delete_todo")
    #     @ns.response(204, "Todo deleted")
    #     def delete(self, id):
    #         """Delete a task given its identifier."""
    #         DAO.delete(id)
    #         return "", 204

    #     @ns.expect(todo)
    #     @ns.marshal_with(todo)
    #     def put(self, id):
    #         """Update a task given its identifier."""
    #         return DAO.update(id, api.payload)
