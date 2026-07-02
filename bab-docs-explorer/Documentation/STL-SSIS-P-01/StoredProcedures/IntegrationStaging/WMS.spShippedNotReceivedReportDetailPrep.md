# WMS.spShippedNotReceivedReportDetailPrep

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spShippedNotReceivedReportDetailPrep"]
    dbo_BEARITORY_DIM(["dbo.BEARITORY_DIM"]) --> SP
    dbo_CNTCT_DIM(["dbo.CNTCT_DIM"]) --> SP
    dbo_Dynamics_EcoResProduct(["dbo.Dynamics_EcoResProduct"]) --> SP
    dbo_Dynamics_EcoResProductTranslation(["dbo.Dynamics_EcoResProductTranslation"]) --> SP
    dbo_dynamics_inventtransferline(["dbo.dynamics_inventtransferline"]) --> SP
    dbo_dynamics_inventtransfertable(["dbo.dynamics_inventtransfertable"]) --> SP
    dbo_dynamics_purchline(["dbo.dynamics_purchline"]) --> SP
    dbo_dynamics_purchtable(["dbo.dynamics_purchtable"]) --> SP
    dbo_dynamics_salestable(["dbo.dynamics_salestable"]) --> SP
    dbo_STR_DIM(["dbo.STR_DIM"]) --> SP
    WMS_ShippedNotReceivedDetail(["WMS.ShippedNotReceivedDetail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.BEARITORY_DIM |
| dbo.CNTCT_DIM |
| dbo.Dynamics_EcoResProduct |
| dbo.Dynamics_EcoResProductTranslation |
| dbo.dynamics_inventtransferline |
| dbo.dynamics_inventtransfertable |
| dbo.dynamics_purchline |
| dbo.dynamics_purchtable |
| dbo.dynamics_salestable |
| dbo.STR_DIM |
| WMS.ShippedNotReceivedDetail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spShippedNotReceivedReportDetailPrep]
--@district varchar(150)

WITH RECOMPILE 

as 

set nocount on 


----------------------------------------------------------------------------------------------------
--//       	                                                                    //--
----------------------------------------------------------------------------------------------------


truncate table [WMS].[ShippedNotReceivedDetail]

 insert into [WMS].[ShippedNotReceivedDetail]  ([OrderNumber],[OrderStatus],[FromWarehouse],[ToWarehouse],[Receipt Date],[ModeOfDelivery],[AptosShipmentNumber]
 ,[ItemId], [Name], [QuantityShipped],[QuantityReceived],[QuantityNotReceived],[DistrictName],[DistrictManager],[DmId],[DMfirstName],[DMlastName])

select p.PurchId as 'OrderNumber', 'Open Order' as 'OrderStatus' , s.InventLocationId as 'From Warehouse',  p.InventLocationId as 'To Warehouse',
p.DeliveryDate as 'Receipt Date', isnull(p.DlvMode,'') as 'ModeOfDelivery', isnull(p.BABAptosPOShipmentNum,'') as 'AptosShipmentNumber'
,pl.ItemId, ept.Name
,isnull(sum(PurchQty),0) as 'Quantity Shipped',  isnull(sum(PurchQty) - sum(RemainInventPhysical),0) as 'Quantity Received', isnull(sum(RemainInventPhysical),0) as 'Quantity Not Received'
,sd.NM as 'District Name', sd.EMAIL as 'District Manager' -- sd.FRST_NM, sd.LAST_NM
,sd.BEARITORY_ID, sd.FRST_NM as 'DMfirstName', sd.LAST_NM as 'DMlastName'
from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_purchtable p
left join SilverDeltaLake.SilverDeltaLake.dbo.dynamics_salestable s on p.PurchId = s.InterCompanyPurchId --and p.DataAreaId = s.DataAreaId --  p.InterCompanySalesId = s.SalesId and p.DataAreaId = s.DataAreaId
inner join SilverDeltaLake.SilverDeltaLake.dbo.dynamics_purchline pl on p.PurchId = pl.PurchId

join [SILVERDELTALAKE].[silverdeltalake].dbo.Dynamics_EcoResProduct ep on pl.ItemId = ep.DisplayProductNumber
join [SILVERDELTALAKE].[silverdeltalake].dbo.Dynamics_EcoResProductTranslation ept on ep.RECID = ept.Product

left join (
select case when s.STR_NUM < 1000 then 1000 + s.STR_NUM else s.STR_NUM end as STR_NUM,s.BEARITORY_ID ,BD.BEARITORY_NUM, BD.NM, CD.FRST_NM, CD.LAST_NM, CD.EMAIL
FROM KODIAK.babwmstrdata.dbo.STR_DIM s
left join KODIAK.babwmstrdata.dbo.BEARITORY_DIM BD on S.BEARITORY_ID = BD.BEARITORY_ID
join KODIAK.babwmstrdata.dbo.CNTCT_DIM CD WITH (NOLOCK) ON BD.CNTCT_ID = CD.CNTCT_ID
) as sd on p.InventLocationId = cast(sd.STR_NUM as varchar)
where 1=1 
--and p.PurchId in ('PO170003239')
--and p.PurchId in ('PO170007735','PO170007738','PO170007864')
and p.PurchStatus = 1
and p.OrderAccount = '99001'
and cast(p.DeliveryDate as date) < cast(getdate() as date) 
--and  p.InventLocationId < 3333
--and ISNUMERIC(p.InventLocationId) = 1
--and p.InventLocationId not like '8%'
--and p.InventLocationId not like '9%'
and pl.RemainInventPhysical is not null
group by p.PurchId ,p.PurchStatus ,  s.InventLocationId,  p.InventLocationId, p.DeliveryDate, p.DlvMode,
p.BABAptosPOShipmentNum,sd.NM, sd.FRST_NM, sd.LAST_NM, sd.EMAIL,sd.BEARITORY_ID, sd.FRST_NM, sd.LAST_NM
,pl.ItemId, ept.Name

--select * from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_purchline where PurchId = 'PO170003239'
--select * from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_purchline where PurchId = 'PO210007183'


union

select itt.TransferId as 'OrderNumber', 'Shipped' as 'OrderStatus',  --itt.ReceiveDate as 'ReceiptDate',
 itt.InventLocationIdFrom as 'From Warehouse'  , itt.InventLocationIdTo as 'To Warehouse' , itt.ReceiveDate as 'Receipt Date',
isnull(itt.DlvModeId,'') as 'ModeOfDelivery', isnull(itt.BABAptosShipmentNumber,'')  as 'AptosShipmentNumber'
,itl.ItemId, ept.Name
,isnull(sum(itl.QtyShipped),0) as 'Quantity Shipped', isnull(sum(itl.QtyReceived),0) as 'Quantity Received', isnull(sum(itl.QtyRemainReceive),0) as 'Quantity Not Received'
,sd.NM as 'District Name', sd.EMAIL as 'District Manager' -- sd.FRST_NM, sd.LAST_NM
,sd.BEARITORY_ID, sd.FRST_NM as 'DMfirstName', sd.LAST_NM as 'DMlastName'
from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_inventtransfertable itt
join SilverDeltaLake.SilverDeltaLake.dbo.dynamics_inventtransferline itl on itt.TransferId = itl.TransferId

join [SILVERDELTALAKE].[silverdeltalake].dbo.Dynamics_EcoResProduct ep on itl.ItemId = ep.DisplayProductNumber
join [SILVERDELTALAKE].[silverdeltalake].dbo.Dynamics_EcoResProductTranslation ept on ep.RECID = ept.Product

left join (
select case when s.STR_NUM < 1000 then 1000 + s.STR_NUM else s.STR_NUM end as STR_NUM,s.BEARITORY_ID ,BD.BEARITORY_NUM, BD.NM, CD.FRST_NM, CD.LAST_NM, CD.EMAIL
FROM KODIAK.babwmstrdata.dbo.STR_DIM s
left join KODIAK.babwmstrdata.dbo.BEARITORY_DIM BD on S.BEARITORY_ID = BD.BEARITORY_ID
join KODIAK.babwmstrdata.dbo.CNTCT_DIM CD WITH (NOLOCK) ON BD.CNTCT_ID = CD.CNTCT_ID
) as sd on itt.InventLocationIdTo = cast(sd.STR_NUM as varchar)
where 1=1
--and sd.NM = 'St. Louis / Kansas City'
and itt.TransferStatus = 1
--and ISNUMERIC(itt.InventLocationIdTo) = 1
--and  itt.InventLocationIdTo < 3333
--and itt.InventLocationIdTo not like '8%'
--and itt.InventLocationIdTo not like '9%'
--and itt.TransferID = 'TO0000358448'
and itl.QtyRemainReceive is not null
and cast(itt.ReceiveDate as date) < cast(getdate() as date) 
group by itt.TransferId , itt.TransferStatus,   itt.ReceiveDate, itt.DlvModeId , itt.BABAptosShipmentNumber , itt.InventLocationIdTo,
itt.InventLocationIdFrom ,sd.NM, sd.FRST_NM, sd.LAST_NM, sd.EMAIL,sd.BEARITORY_ID, sd.FRST_NM, sd.LAST_NM
,itl.ItemId, ept.Name
--order by itt.InventLocationIdTo asc 
 
--select * from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_inventtransfertable  where TransferID = 'TO0000358448'
--select * from SilverDeltaLake.SilverDeltaLake.dbo.dynamics_inventtransferline   where TransferID = 'TO0000358448' and QtyRemainReceive is not null

--if @district = 'All'
--BEGIN
--select * from [WMS].[ShippedNotReceived]
--END
--ELSE 
--BEGIN
--select * from [WMS].[ShippedNotReceived] where DistrictName = @district
--END
```

