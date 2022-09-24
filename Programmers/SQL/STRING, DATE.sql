-- 루시와 엘라 찾기
-- 동물 보호소에 들어온 이름 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디, 이름, 성별 및 중성화 여부 조회
-- 아이디 순으로 조회
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;


-- 이름에 el이 들어가는 동물 찾기
-- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디, 이름 조회
-- 이름 순으로 조회
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE "%EL%"
ORDER BY NAME;


-- 중성화 여부 파악하기
-- 동물의 아이디, 이름, 중성화 여부를 아이디 순으로 조회
-- 중성화가 되어있다면 'O', 아니라면 'X' 라고 표시
-- 중성화된 동물은 SEX_UPON_INTAKE 칼럼에 'Neutered' 또는 'Spayed' 표시됨
SELECT ANIMAL_ID, NAME, 
IF (SEX_UPON_INTAKE NOT LIKE '%INTACT%','O', 'X') '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;


-- 오랜 기간 보호한 동물(2)
-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두마리의 아이디, 이름 조회
-- 보호 기간이 긴 순으로 조회
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATE(O.DATETIME) - DATE(I.DATETIME) DESC
LIMIT 2;

 
-- DATETIME에서 DATE로 형 변환
-- ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디, 이름, 들어온 날짜 조회
-- 아이디 순으로 정렬
SELECT ANIMAL_ID, NAME, LEFT(DATETIME,10) '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;