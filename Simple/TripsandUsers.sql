# Write your MySQL query statement below

Select Request_at As "Day",
CAST((COUNT(case Status when 'Completed' then null else 1 end) / COUNT(*) ) As DECIMAL(10,2)) As "Cancellation Rate"
 From (Trips Right Join (Select Users_Id From Users Where Banned = "No" and Role = "client") As Unbannded_client On Unbannded_client.Users_Id = Trips.client_Id) Where (Request_at <= "2013-10-03" and Request_at >= "2013-10-01") Group By Request_at
