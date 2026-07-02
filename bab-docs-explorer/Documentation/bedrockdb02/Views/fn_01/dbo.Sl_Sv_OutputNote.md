# dbo.Sl_Sv_OutputNote

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Sv_OutputNote"]
    dbo_Sv_OutputNote(["dbo.Sv_OutputNote"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_OutputNote |

## View Code

```sql
create view  [dbo].[Sl_Sv_OutputNote] (
       	output_id, 
       	page_number, 
       	note_text, 
       	user_id, 
       	created_date, 
       	positionX, 
       	positionY, 
       	note_id
)
AS SELECT 
       	output_id, 
       	page_number, 
       	note_text, 
       	user_id, 
       	created_date, 
       	positionX, 
       	positionY, 
       	note_id
FROM fn_01.dbo.Sv_OutputNote
```

