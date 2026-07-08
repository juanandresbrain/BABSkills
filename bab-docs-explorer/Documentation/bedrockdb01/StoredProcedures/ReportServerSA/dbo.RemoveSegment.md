# dbo.RemoveSegment

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveSegment"]
    ChunkSegmentMapping(["ChunkSegmentMapping"]) --> SP
    dbo_ChunkSegmentMapping(["dbo.ChunkSegmentMapping"]) --> SP
    Segment(["Segment"]) --> SP
    dbo_Segment(["dbo.Segment"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ChunkSegmentMapping |
| dbo.ChunkSegmentMapping |
| Segment |
| dbo.Segment |

## Stored Procedure Code

```sql
create proc [dbo].[RemoveSegment]
	@DeleteCountPermanent int, 
	@DeleteCountTemp int
as
begin
	SET DEADLOCK_PRIORITY LOW
	
	-- Locking:
	-- Similar idea as in RemovedSegmentedMapping.  Readpast
	-- any Segments which are currently locked and run the 
	-- inner scan with nolock.	
	declare @numDeleted int;
	declare @toDeleteMapping table (
		SegmentId uniqueidentifier );
	
	insert into @toDeleteMapping (SegmentId)	
	select top (@DeleteCountPermanent) SegmentId 
	from Segment with (readpast)	
	where not exists (
		select 1 from ChunkSegmentMapping CSM with (nolock)
		where CSM.SegmentId = Segment.SegmentId
		) ;
		
	delete from Segment with (readpast)
	where Segment.SegmentId in (
		select td.SegmentId from @toDeleteMapping td
		where not exists (
			select 1 from ChunkSegmentMapping CSM
			where CSM.SegmentId = td.SegmentId ));
			
	select @numDeleted = @@rowcount ;
	
	declare @toDeleteTempSegment table (
		SegmentId uniqueidentifier );
	
	insert into @toDeleteTempSegment (SegmentId)		
	select top (@DeleteCountTemp) SegmentId
	from [ReportServerSATempDB].dbo.Segment with (readpast)	
	where not exists (
		select 1 from [ReportServerSATempDB].dbo.ChunkSegmentMapping CSM with (nolock)
		where CSM.SegmentId = [ReportServerSATempDB].dbo.Segment.SegmentId
		) ;
		
	delete from [ReportServerSATempDB].dbo.Segment with (readpast)
	where [ReportServerSATempDB].dbo.Segment.SegmentId in (
		select td.SegmentId from @toDeleteTempSegment td 
		where not exists (
			select 1 from [ReportServerSATempDB].dbo.ChunkSegmentMapping CSM
			where CSM.SegmentId = td.SegmentId
			)) ;
	select @numDeleted = @numDeleted + @@rowcount ;
	
	select @numDeleted;
end
```

