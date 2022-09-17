from question_answer import Question

question_prompts = [
    "What color are apples\n(a) Red/Green\n(b) Purple/Gold\n(c) Blue/Orange\n(d) Yellow/Brown\n\n",
    "What color are Bananas\n(a) Teal\n(b) Brown\n(c) Yellow\n(d) White\n\n",
    "What color are Strawberries\n(a) Red\n(b) Brown\n(c) Pink\n(d) White\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt) 
        if answer == question.answer:
            score += 1
    print("You got: ",score, "/", len(questions))

run_test(questions)