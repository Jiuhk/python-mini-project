from Jobs import Question

questions_prompts = [
    "What types of animals are monkeys?\na) mammals\nb) amphibians\nc) reptiles\n\n",
    "What types of animals are penguins?\na) birds\nb) mammals\nc) insects\n\n",
    "What types of animals are whales?\na) fish\nb) amphibians\nc) mammals\n\n"
]

questions = [
    Question((questions_prompts[0]), "a"),
    Question((questions_prompts[1]), "a"),
    Question((questions_prompts[2]), "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)
