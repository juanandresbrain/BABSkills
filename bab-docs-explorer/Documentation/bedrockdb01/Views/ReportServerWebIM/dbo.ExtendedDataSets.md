# dbo.ExtendedDataSets

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.ExtendedDataSets"]
    DataSets(["DataSets"]) --> VIEW
    dbo_TempDataSets(["dbo.TempDataSets"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DataSets |
| dbo.TempDataSets |

## View Code

```sql
CREATE VIEW [dbo].ExtendedDataSets
AS 
SELECT 
	ID, LinkID, [Name], ItemID
FROM DataSets
UNION ALL
SELECT
	ID, LinkID, [Name], ItemID
FROM [ReportServerWebIMTempDB].dbo.TempDataSets
```

