# WEB.AlternateImagePivot

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.AlternateImagePivot"]
    WEB_AlternateImagesStage(["WEB.AlternateImagesStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.AlternateImagesStage |

## View Code

```sql
CREATE view [WEB].[AlternateImagePivot]

as

-----------------------------------------------------------------------------------------------------------------------------------------------
--Dan Tweedie - 2017-08-11 -- Created view to support web master catalog xml, to allow for easy lookup of alternate images assiged to products
-----------------------------------------------------------------------------------------------------------------------------------------------

WITH
ProductImageMap as
	(
		select ImageName, right(replicate('0',6) + cast(substring(ImageName, 1, (patindex('%Alt%', ImageName)-1)) as varchar), 6) BABWProductID
		from WEB.AlternateImagesStage
		where (patindex('%Alt%', ImageName)-1) <= 6
	),
ProductImagePivot as
	(
		select
			BABWProductID, 
			case 
				when ImageName like '%Alt1x.jpg' 
				then ImageName
			end as AltImage1,
			case 
				when ImageName like '%Alt2x.jpg' 
				then ImageName
			end as AltImage2,
			case
				when ImageName like '%Alt3x.jpg'
				then Imagename
			end as AltImage3,
			case
				when ImageName like '%Alt4x.jpg'
				then Imagename
			end as AltImage4,
			case
				when ImageName like '%Alt5x.jpg'
				then Imagename
			end as AltImage5
		from ProductImageMap
	)
select 
	BABWProductID, 
	min(AltImage1) as AltImage1,
	min(AltImage2) as AltImage2,
	min(AltImage3) as AltImage3,
	min(AltImage4) as AltImage4,
	min(AltImage5) as AltImage5
from ProductImagePivot
group by BABWProductID
```

