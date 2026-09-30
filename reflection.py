from llm import ask_llm



def check_answer(question, answer):


    result = ask_llm(
f"""
你是答案质量评估器。


请给答案评分：

0-10分


评价：

1. 是否回答问题
2. 是否准确
3. 是否完整



问题：

{question}



答案：

{answer}



只输出数字。

"""
    )


    try:

        score = int(result.strip())

    except:

        score = 5


    return score