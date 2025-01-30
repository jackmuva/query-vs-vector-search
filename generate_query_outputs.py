import requests
import pandas as pd
import re

url = "http://localhost:3000"

data = {
    "email": "jack.mu@useparagon.com"
}

response = requests.post(url + "/api/auth/signJwt", json=data)
jwt = response.json()['jwt']


tools= {
    "SALESFORCE_SEARCH_RECORDS_CONTACT": {
      "type": "function",
      "function": {
        "name": "SALESFORCE_SEARCH_RECORDS_CONTACT",
        "description": "Triggered when a user wants to Search Contact in Salesforce",
        "parameters": {
          "type": "object",
          "properties": {
            "filterFormula": {
              "type": "string",
              "description": "Filter search"
            },
            "paginationParameters": {
              "type": "object",
              "description": "Pagination parameters for paginated results",
              "properties": {
                "pageCursor": {
                  "type": "string",
                  "description": "The cursor indicating the current page"
                }
              },
              "required": [],
              "additionalProperties": False
            }
          },
          "required": [],
          "additionalProperties": False
        }
      }
    },
    "SALESFORCE_GET_RECORD_BY_ID_ANY": {
      "type": "function",
      "function": {
        "name": "SALESFORCE_GET_RECORD_BY_ID_ANY",
        "description": "Triggered when a user wants to Get Any by Id an unknown object typein Salesforce",
        "parameters": {
          "type": "object",
          "properties": {
            "recordType": {
              "type": "string",
              "description": "Record Type"
            },
            "recordId": {
              "type": "string",
              "description": "Record ID"
            }
          },
          "required": [
            "recordType",
            "recordId"
          ],
          "additionalProperties": False
        }
      }
    },
    "SALESFORCE_GET_RECORD_BY_ID_CONTACT": {
      "type": "function",
      "function": {
        "name": "SALESFORCE_GET_RECORD_BY_ID_CONTACT",
        "description": "Triggered when a user wants to Get Contact by Id in Salesforce",
        "parameters": {
          "type": "object",
          "properties": {
            "recordId": {
              "type": "string",
              "description": "Record ID"
            }
          },
          "required": [
            "recordId"
          ],
          "additionalProperties": False
        }
      }
    },
    "SALESFORCE_SEARCH_RECORDS_ANY": {
      "type": "function",
      "function": {
        "name": "SALESFORCE_SEARCH_RECORDS_ANY",
        "description": "Triggered when a user wants to Search Any an unknown object typein Salesforce",
        "parameters": {
          "type": "object",
          "properties": {
            "recordType": {
              "type": "string",
              "description": "Record Type"
            },
            "filterFormula": {
              "type": "string",
              "description": "Filter Search"
            },
            "paginationParameters": {
              "type": "object",
              "description": "Pagination parameters for paginated results",
              "properties": {
                "pageCursor": {
                  "type": "string",
                  "description": "The cursor indicating the current page"
                }
              },
              "required": [],
              "additionalProperties": False
            }
          },
          "required": [
            "recordType"
          ],
          "additionalProperties": False
        }
      }
    },
    "SALESFORCE_WRITE_SOQL_QUERY": {
      "type": "function",
      "function": {
        "name": "SALESFORCE_WRITE_SOQL_QUERY",
        "description": "Triggered when a user wants to write an SOQL query",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "object",
              "description": "SOQL Query"
            }
          },
          "required": [
            "query"
          ],
          "additionalProperties": False
        }
      }
    },
    "NOTION_GET_PAGE_BY_ID": {
      "type": "function",
      "function": {
        "name": "NOTION_GET_PAGE_BY_ID",
        "description": "Triggered when a user wants to get a page by Id in Notion",
        "parameters": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "string",
              "description": "Page ID"
            }
          },
          "required": [
            "pageId"
          ],
          "additionalProperties": False
        }
      }
    },
        "NOTION_SEARCH_PAGES": {
      "type": "function",
      "function": {
        "name": "NOTION_SEARCH_PAGES",
        "description": "Triggered when a user wants to search pages in Notion",
        "parameters": {
          "type": "object",
          "properties": {
            "searchByTitleFilterSearch": {
              "type": "object",
              "description": "Search pages",
              "properties": {
                "query": {
                  "type": "string",
                  "description": "Search query"
                },
                "direction": {
                  "type": "string",
                  "description": "Sort direction"
                },
                "page_size": {
                  "type": "string",
                  "description": "Page size"
                },
                "filter.value": {
                  "type": "string",
                  "description": "Filter value"
                }
              },
              "required": [],
              "additionalProperties": False
            }
          },
          "required": [],
          "additionalProperties": False
        }
      }
    },
    "NOTION_GET_PAGE_CONTENT": {
      "type": "function",
      "function": {
        "name": "NOTION_GET_PAGE_CONTENT",
        "description": "Triggered when a user wants to get a page content in Notion",
        "parameters": {
          "type": "object",
          "properties": {
            "blockId": {
              "type": "string",
              "description": "Page ID"
            }
          },
          "required": [
            "blockId"
          ],
          "additionalProperties": False
        }
      }
    },
    "NOTION_GET_BLOCK_BY_ID": {
      "type": "function",
      "function": {
        "name": "NOTION_GET_BLOCK_BY_ID",
        "description": "Triggered when a user wants to get a block by Id in Notion",
        "parameters": {
          "type": "object",
          "properties": {
            "blockId": {
              "type": "string",
              "description": "Block ID"
            }
          },
          "required": [
            "blockId"
          ],
          "additionalProperties": False
        }
      }
    },
    "SLACK_LIST_MEMBERS": {
      "type": "function",
      "function": {
        "name": "SLACK_LIST_MEMBERS",
        "description": "Triggered when a user wants to get all members",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": [],
          "additionalProperties": False
        }
      }
    },
    "SLACK_LIST_CHANNELS": {
      "type": "function",
      "function": {
        "name": "SLACK_LIST_CHANNELS",
        "description": "Triggered when a user wants to get all channels",
        "parameters": {
          "type": "object",
          "properties": {},
          "required": [],
          "additionalProperties": False
        }
      }
    },
    "SLACK_GET_USER_BY_EMAIL": {
      "type": "function",
      "function": {
        "name": "SLACK_GET_USER_BY_EMAIL",
        "description": "Triggered when a user wants to Get User By Email",
        "parameters": {
          "type": "object",
          "properties": {
            "email": {
              "type": "string",
              "description": "Email"
            }
          },
          "required": [
            "email"
          ],
          "additionalProperties": False
        }
      }
    },
    "SLACK_SEARCH_MESSAGES": {
      "type": "function",
      "function": {
        "name": "SLACK_SEARCH_MESSAGES",
        "description": "Triggered when a user wants to search messages",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search Query"
            }
          },
          "required": [
            "query"
          ],
          "additionalProperties": False
        }
      }
    }
  }

goldens_df = pd.read_csv("../document-base/query-outputs-v2.csv")
goldens_dict = goldens_df.to_dict()

for i in goldens_dict[list(goldens_dict.keys())[0]].keys():
    if str(goldens_dict['actual_output'][i]) != 'nan':
        continue

    prefix = "From Notion, "
    if 'sf' in goldens_dict['source_file'][i]:
        prefix = "From Salesforce, "
    elif 'slack' in goldens_dict['source_file'][i]:
        prefix = "From my Slack, "
    
    prompt = prefix + goldens_dict['input'][i]
    print(prompt)
    actual_response = ""
    actual_context = ""
    messages = [{"content": prompt,
                "role": "user",
                 }]
    body = {"messages": messages, "tools": tools}
    response = requests.post(url + "/api/chat", json=body, headers={"Authorization": "Bearer " + jwt}, stream=True)
    if response.status_code==200:
        with response:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:
                    try:
                        if chunk.decode('utf-8')[:2] == "0:":
                            actual_response += str(chunk.decode('utf-8')[2:]).replace('"', '').replace("\n", " ")
                        else:
                            raw = chunk.decode('utf-8')
                            pattern = r'"toolOutput":(.*)'
                            match = re.search(pattern, raw, re.DOTALL)
                            if match:
                                extracted_text = match.group(1)
                                print(extracted_text)
                                actual_context += extracted_text.replace('"', '').replace("\n", " ")

                    except:
                        continue
    goldens_dict['actual_output'][i] = actual_response
    goldens_dict['retrieval_context'][i] = actual_context 
    output_df = pd.DataFrame.from_dict(goldens_dict)
    output_df.to_csv("../document-base/query-outputs-v2.csv")
