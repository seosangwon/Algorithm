-- 코드를 입력하세요
#가격대별로 상품의 개수를 출력하시오 
SELECT  floor(price/10000) * 10000 as PRICE_GROUP , count(*) as PRODUCTS
from product 
group by PRICE_GROUP
order by price_group
