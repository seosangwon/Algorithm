# parent_item_id에 없는 값들을 조회
select info.item_id , info.item_name , info.rarity 
from item_info as info
left join item_tree as tree on info.item_id = tree.parent_item_id
where tree.parent_item_id is null
order by info.item_id desc
