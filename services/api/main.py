from typing import Any
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import logging

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_structured_chat_agent

from toolset.empty_tool import EmptyTool

class MessageSchema(BaseModel):
    message: str

logging.basicConfig(filename='/home/app/logs/print.log', level=logging.INFO, format='%(asctime)s - %(message)s')

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

# This will be removed once we go live
@app.post("/test-agent")
async def test_agent(message_body: MessageSchema) -> dict[str, Any]:
    return await execute_test_agent(message_body.message)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

async def execute_test_agent(msg: str) -> dict[str, Any]:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-1106-preview")

    ## This is an empty tool that can take multiple parameters, see services/api/toolset/empty_tool.py
    empty_tool = EmptyTool()
    tools = [empty_tool]

    ## Probably synchronous code need to create our own prompts based on this one
    prompt = hub.pull("hwchase17/structured-chat-agent")
    agent = create_structured_chat_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    out = await agent_executor.ainvoke({"input": msg }) 

    return out

