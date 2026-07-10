# Azure.vwFcastDays

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwFcastDays"]
    Azure_NewDateDim(["Azure.NewDateDim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.NewDateDim |

## View Code

```sql
CREATE view [Azure].[vwFcastDays]

AS


-- get last 10 days starting with yesterday
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-1,126) 
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-2,126) 
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-3,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-4,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-5,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-6,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-7,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-8,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-9,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-10,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-11,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-12,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-13,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-14,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-15,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-16,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-17,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-18,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-19,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-20,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-21,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-22,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-23,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-24,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-25,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-26,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-27,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-28,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-29,126)
union
select Date_Key from [Azure].[NewDateDim] where Date_Key = CONVERT(char(10), GetDate()-30,126)
```

