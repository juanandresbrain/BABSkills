# dbo.vwDW_SFSCube_DMA

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_DMA"]
    dbo_demographics_dim(["dbo.demographics_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.demographics_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_DMA]
AS
SELECT     dma_code, MAX(dma_name) AS dma_name
FROM         dbo.demographics_dim
GROUP BY dma_code
union all 
select '-1', 'Not Assigned'
```

