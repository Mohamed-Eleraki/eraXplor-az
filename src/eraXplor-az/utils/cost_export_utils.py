import datetime
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient, models


def monthly_sub_cost_export(
    subscription_id: str, 
    start_date: str, 
    end_date: str,
) -> dict:
    credential = DefaultAzureCredential()
    cm_client = CostManagementClient(credential)
    
    start_date = datetime.datetime.strptime(start_date, "%Y,%m,%d")
    end_date = datetime.datetime.strptime(end_date, "%Y,%m,%d")
    scope = f"/subscriptions/{subscription_id}"
    
    cm_client_query = cm_client.query.usage(
        scope=scope,
        parameters=models.QueryDefinition(
            type='Usage',
            timeframe='Custom',
            time_period=models.QueryTimePeriod(
                from_property=start_date,
                to=end_date,
            ),
            dataset=models.QueryDataset(
                granularity='Daily',
                aggregation={
                    'totalcost': models.QueryAggregation(name='PreTaxCost', function='Sum')
                }
            )
        )
    )
    cm_client_query_result = cm_client_query.rows
    print(cm_client_query_result)
    
monthly_sub_cost_export("pass_sub_id_here", "2025,1,1", "2025,6,30")
# print(monthly_sub_cost_export)