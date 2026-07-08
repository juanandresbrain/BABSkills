# dbo.MSmerge_articleresolver

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| article_resolver | nvarchar | 510 | 0 |  |  |  |
| resolver_clsid | nvarchar | 100 | 0 |  |  |  |
| is_dotnet_assembly | bit | 1 | 1 |  |  |  |
| dotnet_assembly_name | nvarchar | 510 | 1 |  |  |  |
| dotnet_class_name | nvarchar | 510 | 1 |  |  |  |
