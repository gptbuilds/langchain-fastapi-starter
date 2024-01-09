from typing import Type
from pydantic import BaseModel, Field

from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class EmptyToolQuerySchema(BaseModel):
    firs_param: str = Field(description="The first parameter of the tool")
    second_param: int = Field(description="The second parameter of the tool")

class EmptyTool(BaseTool):
    name: str = "empty_tool"
    description: str = """A tool that runs async and can take multiple parameters"""
    args_schema: Type[EmptyToolQuerySchema] = EmptyToolQuerySchema

    async def _arun(
        self,
        first_param: str,
        second_param: int,
    ) -> dict:
        """This is an asynchronous tool it is made to test if you can call it."""
        return {"result": first_param, "other_result": second_param}

    async def _run(
        self,
        first_param: str,
        second_param: int,
    ) -> dict:
        """Not implemented"""
        raise NotImplementedError("Tool does not support sync")

