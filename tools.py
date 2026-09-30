from rag import rag_search


def search_tool(query):
    """
    模拟搜索工具
    """
    
    return [
        f"搜索结果：关于{query}的相关信息暂时没有联网数据"
    ]



def rag_tool(query):
    """
    知识库工具
    """

    result = rag_search(query)

    return result



def calculator(expression):
    """
    计算工具
    """

    try:

        result = eval(expression)

        return f"计算结果:{result}"

    except:

        return "计算失败"



# 工具列表

tools = {

    "rag": rag_tool,

    "search": search_tool,

    "calculator": calculator

}