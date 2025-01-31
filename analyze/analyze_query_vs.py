import json
import pandas as pd

with open('../results/query_eval_v2.json') as f:
    query_dict = json.load(f)
with open('../results/vs_eval_v2.json') as f:
    vs_dict = json.load(f)

goldens_dict = pd.read_csv('../results/golden.csv').to_dict()

def clean_results(input_dict: dict, goldens_dict=goldens_dict) -> dict:
    clean_query_results = {}

    for i in range(0, len(input_dict['test_results'])):
        clean_record = {}

        clean_record['success'] = input_dict['test_results'][i]['success']
        clean_record['input'] = input_dict['test_results'][i]['input']
        clean_record['actual_output'] = input_dict['test_results'][i]['actual_output']
        clean_record['expected_output'] = input_dict['test_results'][i]['expected_output']
        clean_record['context'] = input_dict['test_results'][i]['context']
        clean_record['retrieval_context'] = input_dict['test_results'][i]['retrieval_context']

        source = "Notion"
        if "sf" in goldens_dict['source_file'][i]:
            source = "Salesforce"
        elif "slack" in goldens_dict['source_file'][i]:
            source = "Slack"
        clean_record['source'] = source

        metrics = input_dict['test_results'][i]['metrics_data']
        metric_record = {}
        for i in range(0, len(metrics)):
            metric_details = {}

            metric_details['threshold'] = metrics[i]['threshold']
            metric_details['success'] = metrics[i]['success']
            metric_details['score'] = metrics[i]['score']
            metric_details['reason'] = metrics[i]['reason']

            metric_record[metrics[i]['name']] = metric_details

        clean_record['metrics'] = metric_record
        clean_query_results[input_dict['test_results'][i]['name']] = clean_record
    return clean_query_results

query_res = clean_results(query_dict)
vs_res = clean_results(vs_dict)
print(query_res)
