from deepeval.test_case import LLMTestCase
from deepeval.dataset import EvaluationDataset
import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from dotenv import load_dotenv

load_dotenv()


first_test_case = LLMTestCase(input="What if these shoes don't fit?",
                              actual_output="I agree, its a pretty nice day today",
                              retrieval_context=["All customers are eligible for a 30 day full refund at no extra cost."]
)

dataset = EvaluationDataset(test_cases=[first_test_case])

# Loop through test cases using Pytest
@pytest.mark.parametrize(
    "test_case",
    dataset,
)

def test_customer_chatbot(test_case: LLMTestCase):
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
    assert_test(test_case, [answer_relevancy_metric])
