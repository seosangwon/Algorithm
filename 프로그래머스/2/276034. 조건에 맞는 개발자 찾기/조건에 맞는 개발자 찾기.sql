# Python이나 C# 스킹르 가진 개발자의 정보를 조회 
SELECT D.ID , D.EMAIL , D.FIRST_NAME , D.LAST_NAME
FROM DEVELOPERS AS D 
WHERE D.SKILL_CODE & (SELECT S.CODE FROM SKILLCODES S WHERE NAME = "C#") 
OR D.SKILL_CODE & (SELECT S.CODE FROM SKILLCODES S WHERE NAME = "Python") 
ORDER BY D.ID
                      
                      
                      
 