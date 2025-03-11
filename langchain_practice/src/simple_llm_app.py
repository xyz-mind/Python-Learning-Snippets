"""实现一个简单的翻译应用程序。"""
import asyncio # 实现异步调用
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv() # 获取API密钥

# 初始化LLM
model = ChatDeepSeek(model = "deepseek-chat")

# 定义提示词模板
prompt = ChatPromptTemplate.from_template(
    "你可以对一下内容进行贴切的翻译：{text}"
)

# 格式化输出
parser = StrOutputParser()

# 定义链条
chain = (
    prompt | model | parser
)


# response = chain.invoke({"text" : "Hello,the AI World!"})
# print(response)

# 实现异步流式调用
async def translate_text(text):
     async for chunk in chain.astream({"text" : text}):
        print(chunk,end = "",flush = True)
    
    
asyncio.run(translate_text("Hello,the AI World!"))