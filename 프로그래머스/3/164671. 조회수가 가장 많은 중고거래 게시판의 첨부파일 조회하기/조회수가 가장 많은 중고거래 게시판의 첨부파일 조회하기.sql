# 조회수가 가장 높은 게시물에 대한 첨부 파일 경로를 출력
select concat("/home/grep/src/",board.board_id ,"/",file.file_id,file.file_name,file.file_ext) as file_path
from used_goods_board as board
inner join used_goods_file as file on board.board_id = file.board_id
where board.board_id = (select board_id 
                 from used_goods_board
                 order by views desc limit 1)
order by file.file_id desc
