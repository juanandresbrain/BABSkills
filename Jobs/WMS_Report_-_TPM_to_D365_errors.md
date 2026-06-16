# Job: WMS_Report - TPM_to_D365_errors

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - TPM_to_D365_errors"]
    JOB --> daily_1["Step 1: daily [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
declare @count int     with   ShipmentAPI as      (          select distinct               e.Shipment as TPMShipment,              max(e.sentTo365) ExportDate,              case                   when api.ResponseBody like '%hasErrors":true%'                       then 'Yes'                  else 'NO'              end as HasAPIError,              isnull(api.ResponseBody,api.ExceptionError) as APIResponseBody          from WMS.ASN_TPMToDynamics e with (nolock)          join  WMS.DynamicsAPILog api with (nolock)              on api.IntegrationName='WMS_ASNCreate'              and e.BatchID=api.BatchID              and e.Shipment=api.TPMShipmentNumber          where datediff(dd, api.InsertDate, getdate()) <= 1          group by               e.Shipment,              case                   when api.ResponseBody like '%hasErrors":true%'                       then 'Yes'                  else 'NO'              end,              isnull(api.ResponseBody,api.ExceptionError)      ),  ASNConfirmation as      (          select               ASnShipmentNumber as ShipmentNumberConfirmed,              case                   when message like 'Aptos PO % successfully assigned to ASN%'                      then 1                  else 0              end as isASNCreated,              case                   when errorMessage = ''                       then NULL                   else errorMessage               end as errorMessage,              EnqueuedTimeCST ASNConfirmationDate,              replace(right(message,14),'.','') as DynamicsLoadNumber          from wms.ASN_CreateConfirmation          group by               ASnShipmentNumber,              case                   when message like 'Aptos PO % successfully assigned to ASN%'                      then 1                  else 0              end,              case                   when errorMessage = ''                       then NULL                   else errorMessage               end,              EnqueuedTimeCST,              replace(right(message,14),'.','')      )  select @count = (select count(*) from ShipmentAPI api  left join ASNConfirmation asn on api.TPMShipment=asn.ShipmentNumberConfirmed  where api.HasAPIError='yes' or asn.errorMessage is not null)    if (@count > 0)     begin     exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name  = '2BFCE507-FD4D-4164-8EE5-78C3110002CE'    end      
```


