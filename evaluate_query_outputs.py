from deepeval.dataset import EvaluationDataset
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval import evaluate
from dotenv import load_dotenv
import json

load_dotenv()

query_dataset = EvaluationDataset()

query_dataset.add_test_cases_from_csv_file(
    file_path="../document-base/query-outputs-v3.csv",
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

evaluation = evaluate(query_dataset,metrics=[answer_relevancy, faithfulness, contextual_relevancy], max_concurrent=1, ignore_errors=True, run_async=False, throttle_value=60, use_cache=True);
with open("../document-base/query_eval_v2.json", "w") as f:
     json.dump(evaluation.model_dump(), f)

# for index in range(5, len(query_dataset.test_cases)):
#     print(index)
#     try:
#         evaluation = evaluate([query_dataset.test_cases[index]], metrics=[answer_relevancy, faithfulness, contextual_relevancy], max_concurrent=1, ignore_errors=True, run_async=False);
#         with open("../document-base/query_eval.json", "a") as f:
#             json.dump(evaluation.model_dump(), f)
#     except:
#         print("[ERROR]: " + str(index))
#         continue
