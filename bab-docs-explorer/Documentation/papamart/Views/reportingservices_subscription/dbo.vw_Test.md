# dbo.vw_Test

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_Test"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vw_Test]
AS

select '[Product].[Products].[Division].&[R-B-B]' as 'Value'
union
select '[Product].[Products].[Division].&[R-B-C]' as 'value'
union
select '[Product].[Products].[Division].&[R-B-D]' as 'Value'
union
select '[Product].[Products].[Division].&[R-B-E]' as 'Value'
union 
select '[Product].[Products].[Division].&[R-B-U]' as 'Value'
union 
select '[Product].[Products].[Division].&[R-R-R]' as 'value'
```

