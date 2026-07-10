# dbo.AnswerMap

**Database:** SurveyResults  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AnswerMap_Key | int | 4 | 0 | YES |  |  |
| SurveyProvider_Key | int | 4 | 0 |  |  |  |
| QuestionMap_Key | int | 4 | 1 |  |  |  |
| QuestionId | varchar | 50 | 0 |  |  |  |
| AnswerId | varchar | 50 | 0 |  |  |  |
| Value | varchar | 50 | 0 |  |  |  |
| Text | varchar | 4000 | 0 |  |  |  |
