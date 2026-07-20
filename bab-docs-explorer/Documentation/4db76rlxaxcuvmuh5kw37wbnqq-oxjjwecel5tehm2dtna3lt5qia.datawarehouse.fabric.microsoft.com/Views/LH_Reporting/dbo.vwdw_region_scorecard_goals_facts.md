# dbo.vwdw_region_scorecard_goals_facts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_region_scorecard_goals_facts"]
    dbo_region_scorecard_goals_facts(["dbo.region_scorecard_goals_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.region_scorecard_goals_facts |

## View Code

```sql
CREATE VIEW vwdw_region_scorecard_goals_facts
AS
SELECT * FROM LH_Mart.dbo.region_scorecard_goals_facts
```

