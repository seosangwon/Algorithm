-- 코드를 입력하세요
SELECT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH ,
U.GENDER, COUNT(DISTINCT U.USER_ID) AS USERS
FROM ONLINE_SALE S
INNER JOIN USER_INFO U ON S.USER_ID = U.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR,MONTH,GENDER
ORDER BY YEAR , MONTH , GENDER