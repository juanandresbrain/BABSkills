# catalog.catalog_properties

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["catalog.catalog_properties"]
    internal_catalog_properties(["internal.catalog_properties"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| internal.catalog_properties |

## View Code

```sql
CREATE VIEW [catalog].[catalog_properties]
AS
SELECT     [property_name], 
           [property_value]
FROM       [internal].[catalog_properties]
```

