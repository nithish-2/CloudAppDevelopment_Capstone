import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("jBPu0G2aHNY0RATNq_c9r693XE4qM2ZF4SkbkfSDJHao")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://24b3737b-fec5-4b41-bd68-8f6b28b7429d-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
                db='reviews',
                selector={'dealership': {'$eq': int(dict['id'])}},
            ).get_result()
    try: 
        # result_by_filter=my_database.get_query_result(selector,raw_result=True) 
        result= {
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response} 
            }        
        return result
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
