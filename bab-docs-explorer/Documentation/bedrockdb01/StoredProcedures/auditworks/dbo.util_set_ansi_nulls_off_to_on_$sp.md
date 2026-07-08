# dbo.util_set_ansi_nulls_off_to_on_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_set_ansi_nulls_off_to_on_$sp"]
    dbo_ansi_null_fix_error_log(["dbo.ansi_null_fix_error_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ansi_null_fix_error_log |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.util_set_ansi_nulls_off_to_on_$sp

AS

/* Proc Name: util_set_ansi_nulls_off_to_on_$sp
   Desc : Identifies any objects that were compiled with ANS_NULLS set to OFF. It grabs the definition of the object, stores 

it, drops the old object, then recreates it from the stored definition with ANSI_NULLS set to ON. If the recreation fails it 

rolls the object back to its former states and logs the issue in a table for manual review (ansi_null_fix_error_log).
          

HISTORY
Date     Name         Def# Desc
Sep18,15 Sean Smith   Author
*/

SET NOCOUNT ON
SET ANSI_NULLS ON


-----------------------------------------------------------------------------------------------------------------------------
--	Declarations / Sets: Declare And Set Variables
-----------------------------------------------------------------------------------------------------------------------------

DECLARE
	 @Definition AS NVARCHAR (MAX)
	,@Drop_Statement AS NVARCHAR (500)
	,@Error_Message AS NVARCHAR (4000)
	,@Error_Number AS INT
	,@Error_Severity AS INT
	,@Error_State AS INT
	,@Object_ID AS INT
	,@Transaction_Count AS INT


-----------------------------------------------------------------------------------------------------------------------------
--	Error Trapping: Check If Temp Table(s) Already Exist(s) And Drop If Applicable
-----------------------------------------------------------------------------------------------------------------------------

IF OBJECT_ID (N'tempdb.dbo.#temp_objects_ansi_nulls_off', N'U') IS NOT NULL
BEGIN

	DROP TABLE dbo.#temp_objects_ansi_nulls_off

END


-----------------------------------------------------------------------------------------------------------------------------
--	Table Creation: Create Temp Table(s)
-----------------------------------------------------------------------------------------------------------------------------

CREATE TABLE dbo.#temp_objects_ansi_nulls_off

	(
		 [object_id] INT NOT NULL
		,drop_statement NVARCHAR (500) NULL
		,[definition] NVARCHAR (MAX) NULL
	)


-----------------------------------------------------------------------------------------------------------------------------
--	Table Creation: Create Permanent Table(s)
-----------------------------------------------------------------------------------------------------------------------------

IF OBJECT_ID (N'dbo.ansi_null_fix_error_log', N'U') IS NULL
BEGIN

	CREATE TABLE dbo.ansi_null_fix_error_log

		(
			 log_id INT NOT NULL IDENTITY (1, 1)
			,[schema_name] NVARCHAR (128) NULL
			,[object_name] NVARCHAR (128) NULL
			,[error_severity] INT NULL
			,[error_state] INT NULL
			,[error_number] INT NULL
			,[error_message] NVARCHAR (4000) NULL
			,drop_statement NVARCHAR (500) NULL
			,[definition] NVARCHAR (MAX) NULL
			,log_date DATETIME NULL
		)

END


-----------------------------------------------------------------------------------------------------------------------------
--	Table Insert: Objects With ANSI_NULLS Set To OFF
-----------------------------------------------------------------------------------------------------------------------------

INSERT INTO dbo.#temp_objects_ansi_nulls_off

	(
		 [object_id]
		,drop_statement
		,[definition]
	)

SELECT
	 SM.[object_id]
	,N'DROP ' + (CASE
					WHEN O.[type] IN ('FN', 'IF', 'TF') THEN N'FUNCTION'
					WHEN O.[type] = 'P' THEN N'PROCEDURE'
					WHEN O.[type] = 'TR' THEN N'TRIGGER'
					WHEN O.[type] = 'V' THEN N'VIEW'
					END) + N' [' + S.name +'].[' + O.name + N']' AS drop_statement
	,SM.[definition]
FROM
	sys.sql_modules SM
	INNER JOIN sys.objects O ON O.[object_id] = SM.[object_id]
		AND O.[type] IN ('FN', 'IF', 'P', 'TF', 'TR', 'V')
	INNER JOIN sys.schemas S ON S.[schema_id] = O.[schema_id]
WHERE
	SM.uses_ansi_nulls = 0


-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Recreate All Objects With ANSI_NULLS Set To ON
-----------------------------------------------------------------------------------------------------------------------------

SET @Object_ID = (SELECT TOP (1) ttOANO.[object_id] FROM dbo.#temp_objects_ansi_nulls_off ttOANO ORDER BY ttOANO.[object_id])


SET @Transaction_Count = @@TRANCOUNT


WHILE @Object_ID IS NOT NULL
BEGIN

	SELECT
		 @Drop_Statement = ttOANO.drop_statement
		,@Definition = ttOANO.[definition]
	FROM
		dbo.#temp_objects_ansi_nulls_off ttOANO
	WHERE
		ttOANO.[object_id] = @Object_ID


	BEGIN TRY

		IF @Transaction_Count > 0
		BEGIN

			SAVE TRANSACTION Recreate_Object

		END
		ELSE BEGIN

			BEGIN TRANSACTION

		END


		EXECUTE (@Drop_Statement)


		EXECUTE (@Definition)


		IF @Transaction_Count = 0
		BEGIN

			COMMIT TRANSACTION

		END

	END TRY
	BEGIN CATCH

		SET @Error_Message = ERROR_MESSAGE ()


		SET @Error_Number = ERROR_NUMBER ()


		SET @Error_Severity = ERROR_SEVERITY ()


		SET @Error_State = ERROR_STATE ()


		IF @Transaction_Count = 0
		BEGIN

			ROLLBACK TRANSACTION

		END
		ELSE BEGIN

			IF XACT_STATE () <> -1
			BEGIN

				ROLLBACK TRANSACTION Recreate_Object

			END

		END


		INSERT INTO dbo.ansi_null_fix_error_log

			(
				 [schema_name]
				,[object_name]
				,[error_severity]
				,[error_state]
				,[error_number]
				,[error_message]
				,drop_statement
				,[definition]
				,log_date
			)

		SELECT
			 OBJECT_SCHEMA_NAME (@Object_ID) AS [schema_name]
			,OBJECT_NAME (@Object_ID) AS [object_name]
			,@Error_Severity AS [error_severity]
			,@Error_State AS [error_state]
			,@Error_Number AS [error_number]
			,@Error_Message AS [error_message]
			,@Drop_Statement AS drop_statement
			,@Definition AS [definition]
			,GETDATE () AS log_date

	END CATCH


	SET @Object_ID = (SELECT TOP (1) ttOANO.[object_id] FROM dbo.#temp_objects_ansi_nulls_off ttOANO WHERE ttOANO.[object_id] > @Object_ID ORDER BY ttOANO.[object_id])

END


-----------------------------------------------------------------------------------------------------------------------------
--	Cleanup: Drop Any Remaining Temp Tables
-----------------------------------------------------------------------------------------------------------------------------

IF OBJECT_ID (N'tempdb.dbo.#temp_objects_ansi_nulls_off', N'U') IS NOT NULL
BEGIN

	DROP TABLE dbo.#temp_objects_ansi_nulls_off

END
```

