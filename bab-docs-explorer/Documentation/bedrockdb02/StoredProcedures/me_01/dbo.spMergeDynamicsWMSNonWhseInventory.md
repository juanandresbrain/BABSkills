# dbo.spMergeDynamicsWMSNonWhseInventory

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeDynamicsWMSNonWhseInventory"]
    dbo_DynamicsWMSNonWhseInventory(["dbo.DynamicsWMSNonWhseInventory"]) --> SP
    dbo_DynamicsWMSNonWhseInventoryStage(["dbo.DynamicsWMSNonWhseInventoryStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DynamicsWMSNonWhseInventory |
| dbo.DynamicsWMSNonWhseInventoryStage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeDynamicsWMSNonWhseInventory] -- Update to Proper Name 

as 

---------------------------------------------------------------------------------------------------------
----	Tim Callahan	-	2023-08-29	-	Created proc - Merges Dynamics Inentory Data from DynamicsWMSNonWhseInventoryStage to DynamicsWMSNonWhseInventory
---------------------------------------------------------------------------------------------------------

set nocount on

merge into me_01.dbo.DynamicsWMSNonWhseInventory as target
using	( 
			select
			s.LocationCode, 
			s.StyleCode, 
			s.SKUDescription,
			s.Qty 
			from DynamicsWMSNonWhseInventoryStage s
		) as source 
on 
	(
		-- Key 
		target.[LocationCode]=source.[LocationCode] 
			and
		target.[StyleCode]=source.[StyleCode]
	)


When Not Matched by target
Then Insert
	(
		-- Fields to be inserted 
		   [LocationCode],
		   [StyleCode],
		   [SKUDescription], 
		   [Qty], 
		   [InsertDate]
         
	)
Values
	(
           source.[LocationCode],
		   source.[StyleCode],
		   source.[SKUDescription], 
		   source.[Qty],
           getdate()

	)

When Matched and
	(		
			-- Besure to use isnull logic for compare otherwise may have unintended results 
		    isnull(target.[Qty],0)<>isnull(source.[Qty],0) 
		      
	)
Then Update
	-- Fields to be updated
	set     
		 target.[Qty]=source.[Qty],		 
		 target.[UpdateDate]=getdate()
 
 -- If we find records that exist in target but not the source, we just want to set them to zero 
 WHEN NOT MATCHED BY Source 
  THEN Update 
	set target.Qty = 0 , 
	target.[UpdateDate]=getdate()

;
```

