from llm import ask_llm



def route(question):


    result = ask_llm(
f"""
你是一个任务分类器。


判断用户问题应该使用哪种方式。


只能输出下面三个之一：

RAG

SEARCH

DIRECT



规则：

RAG:
适合：
- 学习概念
- 基础知识
- 已有知识库内容


SEARCH:
适合：
- 最新消息
- 当前数据
- 新闻
- 实时信息


DIRECT:
适合：
- 简单聊天
- 不需要资料的问题



用户问题：

{question}

"""
    )


    result = result.upper()


    if "RAG" in result:
        return "rag"


    if "SEARCH" in result:
        return "search"


    return "direct"