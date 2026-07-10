# dbo.vwfact_kiosk_registrations

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwfact_kiosk_registrations"]
    dbo_transaction_kiosk_facts(["dbo.transaction_kiosk_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_kiosk_facts |

## View Code

```sql
create view vwfact_kiosk_registrations
as 
SELECT 
--[tdf_key]
--      ,[transaction_id]
      [product_key]
      ,[customer_key]
      ,[address_key]
      ,[household_key]
      ,[store_key]
      ,[distance_to_store_TOP]
      ,[nearest_store_key_TOP]
      ,[First_vs_Repeat]
      ,[date_key]
      ,[time_key]
      ,[animal_key]
      ,[guest_type_key]
      ,[purpose_key]
      ,[reason_key]
      ,[event_key]
--      ,[source_key]
--      ,[process_name]
--      ,[process_date]
  FROM [dw].[dbo].[transaction_kiosk_facts]
```

