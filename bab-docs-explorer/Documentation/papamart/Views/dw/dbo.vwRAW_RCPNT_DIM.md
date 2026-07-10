# dbo.vwRAW_RCPNT_DIM

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwRAW_RCPNT_DIM"]
    RAW_RCPNT_DIM(["RAW_RCPNT_DIM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| RAW_RCPNT_DIM |

## View Code

```sql
CREATE view [dbo].[vwRAW_RCPNT_DIM] as
select * from RAW_RCPNT_DIM with (nolock)
```

