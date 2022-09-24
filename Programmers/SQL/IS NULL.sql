-- 이름이 없는 동물의 아이디
-- 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID 조회
-- ID는 오름차순 정렬
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID


-- 이름이 있는 동물의 아이디
-- 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID 조회
-- ID는 오름차순 정렬
SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID


-- NULL 처리하기
-- 동물의 생물 종, 이름, 성별 및 중성화 여부 조회
-- 아이디 순으로 정렬
-- 이름이 없는 동물의 이름은 "No name"으로 표시
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID