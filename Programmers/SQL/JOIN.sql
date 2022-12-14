-- 없어진 기록 찾기
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID, 이름 조회
-- ID 순으로 조회
SELECT ao.ANIMAL_ID, ao.NAME FROM ANIMAL_OUTS ao
LEFT JOIN ANIMAL_INS ai ON ao.ANIMAL_ID = ai.ANIMAL_ID
WHERE ai.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID;
-- 다른 풀이법 --
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS  
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS)
ORDER BY ANIMAL_ID;


-- 있었는데요 없었습니다
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디, 이름 조회
-- 보호 시작일이 빠른 순으로 조회
SELECT I.ANIMAL_ID, I.NAME FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME;


-- 오랜 기간 보호한 동물(1)
-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름, 보호시작일 조회
-- 보호 시작일 순으로 정렬
SELECT I.NAME, I.DATETIME FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3;
-- 다른 풀이법 --
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS INS
WHERE INS.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY INS.DATETIME
LIMIT 3;


-- 보호소에서 중성화한 동물
-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디, 생물 종, 이름 조회
-- 아이디 순으로 조회
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE "Intact %" 
AND O.SEX_UPON_OUTCOME NOT LIKE"Intact %"
ORDER BY I.ANIMAL_ID;