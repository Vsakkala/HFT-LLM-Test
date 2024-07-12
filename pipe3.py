from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "This is a course about Pytohjn list comprehension",
    candidate_labels =["education", "politics", "business"],
)

print(res)