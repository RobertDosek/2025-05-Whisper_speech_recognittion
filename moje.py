#silver_fact_crm_web_stock_mkt
@dlt.table(name="silver_fact_crm_web_stock_mkt",
             comment="Silver version of table fact_crm_web_stock_mkt",
             table_properties= {
                                "quality":"silver",
                                "delta.minReaderVersion":"2",
                                "delta.minWriterVersion":"5",
                                "pipelines.autoOptimize.managed": "true"
             }
  )
def silver_fact_crm_body_type():
	return dlt.read("bronze_fact_crm_body_type")