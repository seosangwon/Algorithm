-- 코드를 입력하세요
# 1. 자동차 종류가 트럭
# 2. 대여 기록 구하기 
# 3. 기록별로 금액 계산하기 
# 대여 기록 Id , 금액 리스트 출력 

with sub_table as(
   select  c.daily_fee , c.car_type , c.car_id , h.history_id , datediff(h.end_date,h.start_date)+1 as period,
    case 
        when datediff(h.end_date,h.start_date)+1 >= 90 then "90일 이상"
        when  datediff(h.end_date,h.start_date)+1 >= 30 then "30일 이상"
        when  datediff(h.end_date,h.start_date)+1 >= 7 then "7일 이상"
        else null
    end as duration
    from CAR_RENTAL_COMPANY_CAR as c 
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h on c.car_id = h.car_id 
    where car_type="트럭"
    
)

select s.history_id , 
    round(s.daily_fee *s.period *(100 - ifnull(p.discount_rate,0)) / 100,0) as FEE
from sub_table as s
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p on s.duration = p.duration_type
and p.car_type = s.car_type
order by fee desc , s.history_id desc



