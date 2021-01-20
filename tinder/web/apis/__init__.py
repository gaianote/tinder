from flask import Blueprint, got_request_exception, request
from flask_restful import Api, Resource

from .client import ClientProxy
from .flow import Flow
from .map_remote import MapRemote
from .mock import MockRule

api = Blueprint("api", __name__, url_prefix="/api")

api_source = Api(api, errors=Exception)
api_source.add_resource(MapRemote, "/map")
api_source.add_resource(Flow, "/flow")
api_source.add_resource(MockRule, "/mock")
api_source.add_resource(ClientProxy, "/config/client/proxy")
