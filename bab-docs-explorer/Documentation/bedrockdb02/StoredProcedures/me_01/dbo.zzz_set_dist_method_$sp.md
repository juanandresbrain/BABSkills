# dbo.zzz_set_dist_method_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.zzz_set_dist_method_$sp"]
    dbo_distribution(["dbo.distribution"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[zzz_set_dist_method_$sp]
AS

/*
* This is a workaround for DMER-2392 which prevent users from viewing sku location quantities on completed distributions from external source
* It will set distribution method to 'Manual' on completed external distributions
* Created by PW on 4/20/2017
*/

SET NOCOUNT ON
BEGIN

	DECLARE @count AS INT
	SELECT @count = count(distribution_id) 
	FROM distribution
	WHERE document_source = 10 -- external
	AND distribution_status = 8 -- completed
	AND distribution_method IS NULL

	IF @count = 0
		PRINT 'There is no distribution to update.'
	ELSE
		BEGIN
			UPDATE distribution
			SET distribution_method = 5
			WHERE document_source = 10
			AND distribution_status = 8
			AND distribution_method IS NULL
		PRINT RTRIM(CAST(@count AS VARCHAR(10)))+' distributions were updated.'
		END
END
```

