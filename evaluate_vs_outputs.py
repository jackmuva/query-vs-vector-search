from deepeval.dataset import EvaluationDataset
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval import evaluate
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()

vs_dataset = EvaluationDataset()

vs_dataset.add_test_cases_from_csv_file(
    file_path="../document-base/vector-search-outputs.csv",
    input_col_name="input",
    actual_output_col_name="actual_output",
    expected_output_col_name="expected_output",
    context_col_name="context",
    context_col_delimiter= ",",
    retrieval_context_col_name="retrieval_context",
    retrieval_context_col_delimiter= ","
)

answer_relevancy = AnswerRelevancyMetric(threshold=0.5)
faithfulness = FaithfulnessMetric(threshold=0.5)
contextual_relevancy = ContextualRelevancyMetric(threshold=0.5)

index = 0
for test in vs_dataset.test_cases:
    print(index)
    try:
        evaluation = evaluate([test], metrics=[answer_relevancy, faithfulness, contextual_relevancy], max_concurrent=1);
        with open("../document-base/vs_eval.json", "a") as f:
            json.dump(evaluation.model_dump(), f)
    except:
        print("[ERROR]: " + str(index))
        continue
