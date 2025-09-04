import json
import boto3
import csv

def lambda_handler(event, context):
    print('context is',context)
    print('event is ', event)
    print('--BUCKET AND FILE NAME ---')
    bucket_name = event['Records'][0]['s3']['bucket']['name'] 
    file_name = event['Records'][0]['s3']['object']['key']
    print('bucket name', bucket_name)
    print('file name', file_name)

# access file from s3
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    print('response is ', response)
    data = response['Body'].read().decode('utf-8').splitlines()
    # print('type',data)
    linesines = csv.reader(data)
    list_lines = list(linesines)
    # headers = next(linesines)
    # print('headers', headers)
    print('===================')
    dicnoary = {}
    for line in list_lines[1:]:
        country = line[0]
        gdp = line[-2]
        if country in dicnoary:
            dicnoary[country] += int(gdp)
        else:
            dicnoary[country] = int(gdp)

    # print(dicnoary)
    file_content = json.dumps(dicnoary)
    if file_name.lower().endswith('.csv'):
        s3.put_object(Bucket=bucket_name, Key='output/agg.json', Body = file_content)
        print('data loaded in S3 sucessfully!')
  

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
