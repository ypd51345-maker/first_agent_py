from rag import rag_search
from calculator import calculator
from llm import generate_answer, reflection_llm



def agent(question):

    print("\n========== Agent启动 ==========")


    retry_count = 0


    current_question = question



    while True:


        print("\nThought:")


        if "+" in current_question or "-" in current_question or "*" in current_question:

            print("我需要使用 calculator 工具")

            action = "calculator"


        else:

            print("我需要使用 rag 工具")

            action = "rag"



        print("\nAction:")
        print(action)



        print("\n执行工具...\n")



        if action == "rag":


            observation = rag_search(
                current_question
            )


        else:


            expression = current_question.replace(
                "计算",
                ""
            ).strip()


            observation = calculator(
                expression
            )



        print("\nObservation:")
        print(observation)


        print("\nReflection:")

        if action == "calculator":
            reflection = True
        else:
            reflection = reflection_llm(
            question,
            observation
    )
       



        if reflection:


            print(
                "YES：LLM判断检索结果可以回答问题"
            )


            break



        else:


            print(
                "NO：LLM判断检索结果无法回答问题"
            )



            # 最多重新检索一次

            if retry_count < 1 and action == "rag":


                retry_count += 1


                print(
                    "\nReflection触发重新检索..."
                )


                current_question = (
                    question
                    + " 相关概念 核心定义 主要内容"
                )


                print(
                    "重新查询:",
                    current_question
                )


                continue



            else:


                print(
                    "\n==========最终答案=========="
                )


                answer = (
                    "抱歉，知识库中的信息不足以回答这个问题。"
                )


                print(answer)


                return answer




    print(
        "\n==========最终答案=========="
    )


    if action == "calculator":
        answer = f"计算结果是：{observation}"
    else:
        answer = generate_answer(
        question,
        observation
    )

    print(answer)

    return answer





if __name__ == "__main__":



    while True:


        question = input(
            "\n请输入问题:"
        )


        if question == "exit":

            break



        agent(question)