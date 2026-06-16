# WMS.spShippedNotReceivedReport

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spShippedNotReceivedReport"]
    WMS_ShippedNotReceived(["WMS.ShippedNotReceived"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ShippedNotReceived |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spShippedNotReceivedReport]
@district integer

WITH RECOMPILE 

as 

set nocount on 


----------------------------------------------------------------------------------------------------
--//       	                                                                    //--
----------------------------------------------------------------------------------------------------

if @district = 0
BEGIN
select * from [WMS].[ShippedNotReceived] where  DmId is not null
END
ELSE 
BEGIN
select * from [WMS].[ShippedNotReceived] where DmId = @district
END
```

