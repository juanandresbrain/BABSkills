# dbo.Sl_Sv_OutputPage

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Sv_OutputPage"]
    dbo_Sv_OutputPage(["dbo.Sv_OutputPage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_OutputPage |

## View Code

```sql
create view  dbo.Sl_Sv_OutputPage (
output_id, 
page_number, 
page_data 
)
AS SELECT 
output_id, 
page_number, 
page_data 
FROM foundation.dbo.Sv_OutputPage
```

