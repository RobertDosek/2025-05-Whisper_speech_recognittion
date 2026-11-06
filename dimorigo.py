#silver_dim_crm_body_type
@dlt.table(name="silver_dim_crm_body_type",
             comment="Silver version of table dim_crm_body_type",
             table_properties= {
                                "quality":"silver",
                                "delta.minReaderVersion":"2",
                                "delta.minWriterVersion":"5",
                                "pipelines.autoOptimize.managed": "true"
             }
  )
def silver_dim_crm_body_type():
	return dlt.read("bronze_dim_crm_body_type")