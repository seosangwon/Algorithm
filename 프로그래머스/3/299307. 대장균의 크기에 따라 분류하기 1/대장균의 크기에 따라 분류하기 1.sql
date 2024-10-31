#대장균의 크기에 따라 분류하기 
select id , 
    case
        when size_of_colony <= 100 then "LOW"
        when 100<size_of_colony and size_of_colony<=1000 then "MEDIUM"
        else "HIGH"
    end 
        as SIZE
from ecoli_data
order by id

