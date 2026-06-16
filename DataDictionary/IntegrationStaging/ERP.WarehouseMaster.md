# ERP.WarehouseMaster

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AreAdvancedWarehouseManagementProcessesEnabled | nvarchar | 510 | 1 |  |  |  |
| AreItemsCoveragePlannedManually | nvarchar | 510 | 1 |  |  |  |
| AreLaborStandardsAllowed | nvarchar | 510 | 1 |  |  |  |
| ArePickingListsDeliveryModeSpecific | nvarchar | 510 | 1 |  |  |  |
| ArePickingListsShipmentSpecificOnly | nvarchar | 510 | 1 |  |  |  |
| AreWarehouseLocationCheckDigitsUnique | nvarchar | 510 | 1 |  |  |  |
| DefaultContainerTypeId | nvarchar | 510 | 1 |  |  |  |
| ExternallyLocatedWarehouseVendorAccountNumber | nvarchar | 510 | 1 |  |  |  |
| FormattedPrimaryAddress | nvarchar | 510 | 1 |  |  |  |
| InventoryStatusChangeReservationRemovalLevel | nvarchar | 510 | 1 |  |  |  |
| IsBillOfLadingPrintingBeforeShipmentConfirmationEnabled | nvarchar | 510 | 1 |  |  |  |
| IsFallbackWarehouse | nvarchar | 510 | 1 |  |  |  |
| IsFinancialNegativeRetailStoreInventoryAllowed | nvarchar | 510 | 1 |  |  |  |
| IsPalletMovementDuringCycleCountingAllowed | nvarchar | 510 | 1 |  |  |  |
| IsPhysicalNegativeRetailStoreInventoryAllowed | nvarchar | 510 | 1 |  |  |  |
| IsPrimaryAddressAssigned | nvarchar | 510 | 1 |  |  |  |
| IsRefilledFromMainWarehouse | nvarchar | 510 | 1 |  |  |  |
| IsRetailStoreWarehouse | nvarchar | 510 | 1 |  |  |  |
| MainRefillingWarehouseId | nvarchar | 510 | 1 |  |  |  |
| MasterPlanningWorkCalendardId | nvarchar | 510 | 1 |  |  |  |
| MaximumBatchPickingListQuantity | int | 4 | 1 |  |  |  |
| MaximumPickingListLineQuantity | int | 4 | 1 |  |  |  |
| OperationalSiteId | int | 4 | 1 |  |  |  |
| PrimaryAddressCity | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressCountryRegionId | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressCountyId | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressDescription | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressDistrictName | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressLatitude | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressLocationRoles | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressLocationSalesTaxGroupCode | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressLongitude | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressStateId | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressStreet | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressTimeZone | nvarchar | 510 | 1 |  |  |  |
| PrimaryAddressZipCode | nvarchar | 510 | 1 |  |  |  |
| QuarantineWarehouseId | nvarchar | 510 | 1 |  |  |  |
| RawMaterialPickingInventoryIssueStatus | nvarchar | 510 | 1 |  |  |  |
| RetailStoreQuantityAllocationReplenismentRuleWeight | numeric | 17 | 1 |  |  |  |
| ShouldWarehouseLocationIdIncludeAisleId | nvarchar | 510 | 1 |  |  |  |
| TransitWarehouseId | nvarchar | 510 | 1 |  |  |  |
| WarehouseId | nvarchar | 510 | 1 |  |  |  |
| WarehouseLocationIdBinIdFormat | nvarchar | 510 | 1 |  |  |  |
| WarehouseLocationIdRackIdFormat | nvarchar | 510 | 1 |  |  |  |
| WarehouseLocationIdShelfIdFormat | nvarchar | 510 | 1 |  |  |  |
| WarehouseName | nvarchar | 510 | 1 |  |  |  |
| WarehouseSpecificDefaultInventoryStatusId | nvarchar | 510 | 1 |  |  |  |
| WarehouseType | nvarchar | 510 | 1 |  |  |  |
| WillAutomaticLoadReleaseReserveInventory | nvarchar | 510 | 1 |  |  |  |
| WillInventoryStatusChangeRemoveBlocking | nvarchar | 510 | 1 |  |  |  |
| WillManualLoadReleaseReserveInventory | nvarchar | 510 | 1 |  |  |  |
| WillOrderReleasingConsolidateShipments | nvarchar | 510 | 1 |  |  |  |
| WillProductionBOMsReserveWarehouseLevelOnly | nvarchar | 510 | 1 |  |  |  |
| WillShippingCancellationDecrementLoadQuanity | nvarchar | 510 | 1 |  |  |  |
| WillWarehouseLocationIdIncludeBinIdByDefault | nvarchar | 510 | 1 |  |  |  |
| WillWarehouseLocationIdIncludeRackIdByDefault | nvarchar | 510 | 1 |  |  |  |
| WillWarehouseLocationIdIncludeShelfIdByDefault | nvarchar | 510 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spPartyStageForDynamics](../../StoredProcedures/IntegrationStaging/WMS.spPartyStageForDynamics.md)

