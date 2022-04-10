from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY
class PostSwagger:
    def __init__(self, params, required, description, examples_={
                    "application/json": {
                        "gcode": 0,
                        "success": True,
                        "data" : "<res_data>"
                    }
                }):
        self.params = {}
        for p in params:
            self.params[p] = openapi.Schema(type=params[p])
        self.req = openapi.Schema(type=openapi.TYPE_OBJECT, properties=self.params,required=required)
        self.res = {
            "200": openapi.Response(
                description="성공",
                examples=examples_
            )
        }
        self.description = description

    def get_auto_schema(self):
        return swagger_auto_schema(
            operation_summary=self.description,
            request_body=self.req,
            responses=self.res
        )

class GetSwagger:
    def __init__(self, params, examples_, description):
        self.params = []
        for p in params:
            self.params.append(Parameter(p, IN_QUERY, type=params[p]))
        
        self.res = {
            "200" : openapi.Response(
                description="성공",
                examples=examples_
            )
        }
        self.description = description
    
    def get_auto_schema(self):
        return swagger_auto_schema(
            operation_summary=self.description, 
            manual_parameters=self.params,
            responses=self.res
        )