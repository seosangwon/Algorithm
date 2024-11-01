#평균 대여기간이 7일 이상인 자동차 
SELECT CAR_id ,round(avg(datediff(end_date,start_date)+1),1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by car_id
having round(avg(datediff(end_date,start_date)+1),1) >= 7
ORDER BY AVERAGE_DURATION DESC , car_id desc
