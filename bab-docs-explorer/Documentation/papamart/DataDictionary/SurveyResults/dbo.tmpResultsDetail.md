# dbo.tmpResultsDetail

**Database:** SurveyResults  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RespondentID | nvarchar | 50 | 0 |  |  |  |
| ResultsHeader_Key | int | 4 | 0 |  |  |  |
| QuestionMap_Key | int | 4 | 0 |  |  |  |
| AnswerMap_Key | int | 4 | 0 |  |  |  |
| Value | varchar | 1000 | 1 |  |  |  |
| SubType | varchar | 50 | 1 |  |  |  |
