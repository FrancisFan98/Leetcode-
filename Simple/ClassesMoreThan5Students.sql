# Write your MySQL query statement below
Select class From (Select Distinct * From courses) as cleanCourse Group By class Having COUNT(*) >= 5
