from llm import ask_llm



def create_plan(question):


    plan = ask_llm(
f"""
你是Agent规划器。


把用户问题拆成执行步骤。


要求：

- 每一步一句话
- 不超过5步
- 输出编号列表


用户问题：

{question}

"""
    )


    return plan