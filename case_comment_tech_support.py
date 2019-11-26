from simple_salesforce import Salesforce
import pandas as pd
import os
import sys
import requests
from requests.auth import HTTPBasicAuth
import config
import json
from sqlalchemy import create_engine, exc
import constants
import utils

query = '''SELECT CommentBody,CreatedById,CreatedDate,Id,IsDeleted,IsPublished,LastModifiedById,LastModifiedDate,ParentId,SystemModstamp FROM CaseComment where ParentId in (select Id from Case WHERE Case_Type__c='Technical Support Request'  '''

#SELECT Id FROM Contact WHERE LastName = 'foo' or Account.Name = 'bar'
#SELECT Account.Name, (SELECT Contact.Name FROM contacts) FROM Account WHERE Account.Id IN (SELECT Contact.accountId FROM Contact)
#JOIN CaseHistory ON CaseHistory.CaseId = Case.Id

date_time_field = utils.get_last_record_timestamp(constants.CASES.get('index'), constants.CASES.get('date_time_field'))

INFINERA_DB_URL = "mysql+cymysql://root:tang3456@infinera-prod.cnccf8ulxory.us-west-2.rds.amazonaws.com/infinera_staging"
ssl_args = {'ssl': {'ca': 'C:/Users/hema.fullerton/Desktop/eKryp/Infinera_ml/rds-combined-ca-bundle.pem'}}

engine = create_engine(INFINERA_DB_URL, connect_args=ssl_args, echo=False)

m=12
#while m<13:

try: 
            date_time_max= '2018-12-01T00:00:03Z'
            date_time_min= '2019-01-01T00:00:03Z'
            #date_time_max= '2018-'+str(m)+'-01T00:00:03Z'
            #date_time_min= '2018-'+str(m+1)+'-01T00:00:03Z'
            print('From ',date_time_max, ' To ',date_time_min)

            response = config.SF.query_all(query + 'and CreatedDate > {0} and CreatedDate < {1} )' .format(date_time_max, date_time_min))

            print('Got The Records!')

            is_updated = utils.check_response(response)

            if is_updated:
               sys.exit()

            df = pd.DataFrame(response['records'])
            df.drop(['attributes'], axis=1, inplace=True)

            print('Done Processing')

            table_name='case_comment_tech_support'
            print('size: ',len(df))
            print('case_comment_tech_support_2018 for ',str(m))
            df.to_csv('case_comment_tech_support_2018_'+str(m)+'.csv')
            print('All done!')

            
except Exception as e:
            print(e)

   # m=m+1
        



