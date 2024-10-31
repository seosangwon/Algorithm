#BASS , SNAPPER를 잡은 수를 출력
select count(info.fish_type) as FISH_COUNT
from fish_info info
where info.fish_type in (select fish_type 
                         from fish_name_info
                        where fish_name = "BASS" or fish_name="SNAPPER")