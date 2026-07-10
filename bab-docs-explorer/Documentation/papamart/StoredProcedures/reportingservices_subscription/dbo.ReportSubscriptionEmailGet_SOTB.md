# dbo.ReportSubscriptionEmailGet_SOTB

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ReportSubscriptionEmailGet_SOTB"]
    Email(["Email"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Email |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Gary Murrish
-- Create date: 6/28/2012
-- Description:	Retrieves the list of email users associated with the Reports
-- Restricted just to the State of the Business Reports
--		G Murrish	9/8/2015	Added Bryson Ahrens (164)
--		Kevin Shyr	6/1/2015	Added Gary Murrish
--		Kevin Shyr	4/6/2015	Removed Judy Shillinger (126) from the distribution.
--		G Murrish	2/14/2014	Removed Mark Geldmacher (123) from list and added Brian Popp (153)
--		G Murrish	12/23/2013	Removed Michele Gonzalez (131) from the distribution.
--		G Murrish	8/8/2013	Added Michele Gonzalez (131) to the distribution
--		G Murrish	8/8/2013	Added Maria Cucci (38) and Tonya Seals-Robinson (128) to the distribution
--		G Murrish	6/10/2013	Removed Josh Hawkins (125) from the distribution
--		G Murrish	8/20/2012	Added Judy Shillinger (126) to the distribution.
--		G Murrish	12/31/2012	Added Shari Stout (34) to the distribution
--		G Murrish	1/11/2013	Added Julie Zuick (134) to the distribution
--		G Murrish	1/21/2013	Added Carla Amschler (135) to the distribution
--		G Murrish	2/5/2013	Added Nancy Schwartz (60) to the distribution
--		G Murrish	2/18/2013	Added Marsha Fuchs (136) to the distribution.
--		G Murrish	4/8/2013	Added Maria Sharma (138) to the distribution per Michael Segura
-- =============================================
CREATE PROCEDURE [dbo].[ReportSubscriptionEmailGet_SOTB]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT e.Email
		 , e.Name
		 , e.EmailId
	FROM
		Email e
	WHERE
		e.EmailId IN (98, 96, 9, 117, 118, 47, 27, 15, 153, 124, 18, 34,134, 60, 136, 138, 38, 128, 176, 164)
		AND e.Enabled = 1
	ORDER BY
		e.Name

END
```

