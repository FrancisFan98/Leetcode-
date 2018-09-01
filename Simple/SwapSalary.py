# Write your MySQL query statement below
Update salary 
Set sex = 
Case When (sex = 'f') Then 'm'
     When (sex = 'm') Then 'f' 
End;;
