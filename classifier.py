import dill
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification", model="facebook/bart-large-mnli"
)

# save the model
try:
    dill.dump(pipeline, open("zero-shot-classifier", "wb"))
except Exception as e:
    print(str(e))

