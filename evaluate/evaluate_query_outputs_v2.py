from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ContextualRelevancyMetric
from deepeval import evaluate
from dotenv import load_dotenv
import json
import pandas as pd

load_dotenv()

output_dict = pd.read_csv('../results/query-outputs-v3.csv').to_dict()

test_cases = []

for index in output_dict['input'].keys():
    test_case = LLMTestCase(
        input=output_dict['input'][index],
        actual_output=output_dict['actual_output'][index],
        expected_output=output_dict['expected_output'][index],
        context=[str(output_dict['context'][index])],
        retrieval_context=[str(output_dict['retrieval_context'][index])],
    ) 
    test_cases.append(test_case)

answer_relevancy = AnswerRelevancyMetric(threshold=0.5)
faithfulness = FaithfulnessMetric(threshold=0.5)
contextual_relevancy = ContextualRelevancyMetric(threshold=0.5)

evaluation = evaluate(test_cases, [answer_relevancy, faithfulness, contextual_relevancy],max_concurrent=1, ignore_errors=True, run_async=False, throttle_value=10, use_cache=True) 
with open("../results/query_eval_v2.json", "w") as f:
     json.dump(evaluation.model_dump(), f)
