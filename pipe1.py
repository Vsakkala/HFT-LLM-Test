from transformers import pipeline

classifier = pipeline(task = "sentiment-analysis")

res = classifier("Love that")

print(res)