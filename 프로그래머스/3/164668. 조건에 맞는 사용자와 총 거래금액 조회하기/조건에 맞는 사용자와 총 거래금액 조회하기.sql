-- 코드를 입력하세요
SELECT USER_ID , NICKNAME , SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER
INNER JOIN USED_GOODS_BOARD ON USER_ID = WRITER_ID
WHERE STATUS='DONE'
GROUP BY WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES

