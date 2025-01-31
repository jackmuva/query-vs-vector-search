import json
import pandas as pd


def clean_results(input_dict: dict, goldens_dict: dict) -> dict:
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
        for j in range(0, len(metrics)):
            metric_details = {}

            metric_details['threshold'] = metrics[j]['threshold']
            metric_details['success'] = metrics[j]['success']
            metric_details['score'] = metrics[j]['score']
            metric_details['reason'] = metrics[j]['reason']

            metric_record[metrics[j]['name']] = metric_details

        clean_record['metrics'] = metric_record
        clean_query_results[input_dict['test_results'][i]['name']] = clean_record
    return clean_query_results



def create_results_table(results: list, labels: list) -> pd.DataFrame:
    df_dict = {}
    df_dict['method'] = []
    df_dict['test_case'] = []
    df_dict['input'] = []
    df_dict['actual_output'] = []
    df_dict['expected_output'] = []
    df_dict['context'] = []
    df_dict['retrieval_context'] = []
    df_dict['source'] = []
    df_dict['answer_relevancy_score'] = []
    df_dict['answer_relevancy_reason'] = []
    df_dict['faithfulness_score'] = []
    df_dict['faithfulness_reason'] = []
    df_dict['contextual_relevancy_score'] = []
    df_dict['contextual_relevancy_reason'] = []

    for index, res in enumerate(results):
        for i in res.keys():
            df_dict['test_case'].append(i)
            df_dict['method'].append(labels[index])
            df_dict['input'].append(res[i]['input'])
            df_dict['actual_output'].append(res[i]['actual_output'])
            df_dict['expected_output'].append(res[i]['expected_output'])
            df_dict['context'].append(res[i]['context'])
            df_dict['retrieval_context'].append(res[i]['retrieval_context'])
            df_dict['source'].append(res[i]['source'])

            for j in res[i]['metrics'].keys():
                if j == 'Answer Relevancy':
                    df_dict['answer_relevancy_score'].append(res[i]['metrics'][j]['score'])
                    df_dict['answer_relevancy_reason'].append(res[i]['metrics'][j]['reason'])
                elif j == 'Faithfulness':
                    df_dict['faithfulness_score'].append(res[i]['metrics'][j]['score'])
                    df_dict['faithfulness_reason'].append(res[i]['metrics'][j]['reason'])
                elif j == 'Contextual Relevancy':
                    df_dict['contextual_relevancy_score'].append(res[i]['metrics'][j]['score'])
                    df_dict['contextual_relevancy_reason'].append(res[i]['metrics'][j]['reason'])
    return pd.DataFrame.from_dict(df_dict)

with open('../results/query_eval_v2.json') as f:
    query_dict = json.load(f)
with open('../results/vs_eval_v2.json') as f:
    vs_dict = json.load(f)

goldens_dict = pd.read_csv('../results/golden.csv').to_dict()
query_res = clean_results(query_dict, goldens_dict)
vs_res = clean_results(vs_dict, goldens_dict)
results_table = create_results_table([query_res, vs_res], ['query', 'vs'])
results_table.to_csv('../final-assets/agg_table.csv')
