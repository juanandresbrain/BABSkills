# dbo.sfsgsts2

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_quarter | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_week | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| all_trans_cnt | int | 4 | 1 |  |  |  |
| sfs_trans_cnt | int | 4 | 1 |  |  |  |
| SFSGstID | int | 4 | 1 |  |  |  |
| CRM_MBRSHP_DT | datetime2 | 8 | 1 |  |  |  |
| VALID_CRM_MBRSHP_DT | datetime2 | 8 | 1 |  |  |  |
| SFS_GstVisitType | varchar | 8000 | 1 |  |  |  |
| New_SFSGstID | int | 4 | 1 |  |  |  |
| SFSValidEmail | varchar | 8000 | 1 |  |  |  |
| SFSValidEmail_GstID | int | 4 | 1 |  |  |  |
| NewSFSValidEmail_GstID | int | 4 | 1 |  |  |  |
