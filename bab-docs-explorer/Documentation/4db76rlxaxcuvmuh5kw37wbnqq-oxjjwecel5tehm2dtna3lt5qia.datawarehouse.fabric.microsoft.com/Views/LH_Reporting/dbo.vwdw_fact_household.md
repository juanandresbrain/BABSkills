# dbo.vwdw_fact_household

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_fact_household"]
    dbo_household_facts(["dbo.household_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.household_facts |

## View Code

```sql
CREATE VIEW vwdw_fact_household
 AS  
   
  SELECT  TOP 1
   household_key  
   ,customer_geography_key  
   ,loyalty_signup_date_key  
   ,last_visit_date_key  
   ,nearest_store_key  
   ,lifetime_visit_count_key  
   ,first_visit_date_key  
   ,web_first_visit_date_key  
   ,web_last_visit_date_key  
   ,future_nearest_store_key  
   ,web_lifetime_visit_count_key  
  FROM LH_Mart.dbo.household_facts  
  -- The where clause will ensure only SFS households are brought into the cube  
  WHERE loyalty_signup_date_key > 0
```

