#silver_fact_crm_leads_calls
@dlt.table(name="silver_fact_crm_leads_calls",
             comment="Silver version of table fact_crm_leads_calls",
             table_properties= {
                                "quality":"silver",
                                "delta.minReaderVersion":"2",
                                "delta.minWriterVersion":"5",
                                "pipelines.autoOptimize.managed": "true"
             }
  )
def silver_fact_crm_leads_calls():
	return dlt.read("bronze_fact_crm_leads_calls")