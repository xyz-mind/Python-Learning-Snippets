"""
构建一个搜索代理。
pip install langchain-community langgraph langchain-openai tavily-python langgraph-checkpoint-sqlite    
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage


load_dotenv()

# 创建智能体
memory = MemorySaver()

# 创建模型实例
model = ChatOpenAI(
    model = "deepseek-chat",
    base_url = "https://api.deepseek.com"
)

# 构建搜索引擎工具
search = TavilySearchResults(max_results = 2)
tools = [search]

agent = create_react_agent(model=model,tools=tools,checkpointer=memory)


config = {"thread_id" : "abc123"}

for chunk in agent.stream({"messages" : [HumanMessage(content = "北京天气。")]},config=config):
    print(chunk)