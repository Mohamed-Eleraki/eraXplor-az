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
    
    cm_client_query_results = []
        
    try:
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
        cm_client_query_rows = cm_client_query.rows
        for row in cm_client_query_rows:
            time_period = row[1]
            cost = row[0]
            currency = row[2]
            
            cm_client_query_results.append(
                {
                    "TIME_PERIOD": time_period,
                    "COST": f"{cost:.2f} {currency}",
                }
            )
            
        return cm_client_query_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

cm_client_query_results = monthly_sub_cost_export("sub_id_here", "2025,1,1", "2025,4,30")
print(cm_client_query_results)