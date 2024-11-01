#2022년 10월 16일에 대여중인 자동차는 대여중 , 대여중이지 않는 자동차는 대여 가능 
#최근 날짜 판별하는 방법 : max 
select car_id , 
    case
        when car_id in (select car_id 
                       from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        where "2022-10-16" between start_date and end_date
                       ) then "대여중"
        else "대여 가능"
    end as AVAILABILITY

from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc