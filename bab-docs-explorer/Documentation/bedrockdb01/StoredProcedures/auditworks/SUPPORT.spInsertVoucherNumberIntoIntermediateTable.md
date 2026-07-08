# SUPPORT.spInsertVoucherNumberIntoIntermediateTable

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["SUPPORT.spInsertVoucherNumberIntoIntermediateTable"]
    SUPPORT_VoucherImportProgramLiabilityNumbers(["SUPPORT.VoucherImportProgramLiabilityNumbers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SUPPORT.VoucherImportProgramLiabilityNumbers |

## Stored Procedure Code

```sql
CREATE   Procedure [SUPPORT].[spInsertVoucherNumberIntoIntermediateTable]
(
   @ReferenceNumber		varchar(20) ,
   @ReferenceType                    smallint
    
)

As
-- =============================================================================================================
-- Name: spInsertVoucherNumberIntoIntermediateTable
--
-- Description:	
--	
--
-- Input:		Voucher identifier
--
-- Output: N/A
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		?				09/02/2010		Initial version in source control.
-- =============================================================================================================

    set nocount on

	INSERT INTO [auditworks].[SUPPORT].[VoucherImportProgramLiabilityNumbers]([reference_type], [reference_no], [key_store_no], [VoucherCreateDate])
VALUES(@ReferenceType, @ReferenceNumber, -1, getdate())
```

