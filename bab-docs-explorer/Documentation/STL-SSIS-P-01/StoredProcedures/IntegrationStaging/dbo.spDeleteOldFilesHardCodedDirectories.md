# dbo.spDeleteOldFilesHardCodedDirectories

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDeleteOldFilesHardCodedDirectories"]
    dbo_usp_delete_old_files(["dbo.usp_delete_old_files"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.usp_delete_old_files |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spDeleteOldFilesHardCodedDirectories]

as

set nocount on

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-sftp-p-01\ecommerce\to-bab\from-Deck\PendingOrders\ARCHIVE\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\CRM\FTP\archive\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\CRM\DataExtension\archive\', 
@filemask = '*.zip', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\Dynamics\DBSchenker_FullInGate\Archive\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\firstData\Archive\', 
@filemask = '*.TXT', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HA\CartonCancelled\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HA\CartonCreate\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HA\CartonSummary\Archive\', 
@filemask = '*.CSV', 
@retention = 7

--EXEC papamart.dw.dbo.usp_delete_old_files 
--@path = '\\stl-ssis-p-01\IntegrationStaging\HR\UHCM\Archive\', 
--@filemask = '*.CSV', 
--@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HR\UltiproADphoneExt\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HR\UltiProImport\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HR\UltiproTermSamaccount\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\HR\UTA\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\ShopperTrak\Download\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\UK_POS_Data\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\MasterDataXtras\AltImageTagsArchive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Coupons\Archive\', 
@filemask = '*.ZIP', 
@retention = 21

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Inventory\Archive\', 
@filemask = '*.ZIP', 
@retention = 5

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Locations\Archive\', 
@filemask = '*.xml', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\Archive\', 
@filemask = '*.xml', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\ProductCatalogMaster\Archive\', 
@filemask = '*.xml', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\ProductCatalogStoreFront\Archive\', 
@filemask = '*.xml', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Stores\Archive\', 
@filemask = '*.xml', 
@retention = 3


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\ShopperTrak\Download\Archive\', 
@filemask = '*.csv', 
@retention = 30

---TEST
EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\CRM\FTP\archive\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\CRM\DataExtension\archive\', 
@filemask = '*.zip', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\Dynamics\DBSchenker_FullInGate\Archive\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\firstData\Archive\', 
@filemask = '*.TXT', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HA\CartonCancelled\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HA\CartonCreate\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HA\CartonSummary\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HR\UHCM\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HR\UltiproADphoneExt\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HR\UltiProImport\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HR\UltiproTermSamaccount\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\HR\UTA\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\ShopperTrak\Download\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\UK_POS_Data\Archive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\MasterDataXtras\AltImageTagsArchive\', 
@filemask = '*.CSV', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\Coupons\Archive\', 
@filemask = '*.ZIP', 
@retention = 21

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\Inventory\Archive\', 
@filemask = '*.ZIP', 
@retention = 5

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\Locations\Archive\', 
@filemask = '*.xml', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\Pricebook\Archive\', 
@filemask = '*.xml', 
@retention = 7

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\ProductCatalogMaster\Archive\', 
@filemask = '*.xml', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\ProductCatalogStoreFront\Archive\', 
@filemask = '*.xml', 
@retention = 3

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\WEB\Outbound\Stores\Archive\', 
@filemask = '*.xml', 
@retention = 3


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\clb-ssis-t-01\IntegrationStaging\ShopperTrak\Download\Archive\', 
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\Responsys\ExactTarget\RejectedEmails\',
@filemask = '*.txt', 
@retention = 30


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\WebDemandTracking\Archive\',
@filemask = '*.csv', 
@retention = 15

---
EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSOrders\BABW-US\',
@filemask = '*.xml', 
@retention = 30


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSOrders\BABW-US\Success\',
@filemask = '*.xml', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSOrders\RAW\',
@filemask = '*.xml', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSOrders\BABW-UK\Success\LoggedFiles\',
@filemask = '*.xml', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSTransactionDetails\RAW\',
@filemask = '*.csv', 
@retention = 30

EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\OMSTransactionDetails\Archive\',
@filemask = '*.csv', 
@retention = 30


-- Added entries below on 6/14/2022 - Tim C 


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\DynamicAction\Archive\', 
@filemask = '*.csv', 
@retention = 30


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\DynamicAction\Archive\', 
@filemask = '*.csv', 
@retention = 30


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\GoogleAdsStoreInventory\Archive\', 
@filemask = '*.csv', 
@retention = 30

-- Added entries below on 8/22/2023 - Tim C 
EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Feedonomics\Inventory\Archive\', 
@filemask = '*.zip', 
@retention = 8


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\kermode\FileRepository\PLM\CartonDimensions\Archive\', 
@filemask = '*.csv', 
@retention = 8


EXEC papamart.dw.dbo.usp_delete_old_files 
@path = '\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Feedonomics\PriceBook\Archive\', 
@filemask = '*.xml', 
@retention = 8
```

