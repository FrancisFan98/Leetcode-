# Write your MySQL query statement below
Select DISTINCT l1.Num as ConsecutiveNums from Logs l1
Left Join Logs l2 On l1.id = l2.id-1
Left Join Logs l3 On l1.id = l3.id-2
Where l1.Num = l2.Num and l2.num = l3.num
