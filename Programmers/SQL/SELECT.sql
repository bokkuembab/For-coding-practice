# 모든 레코드 조회하기 #
# 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID


# 역순 정렬하기 #
# 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일 조회
# ANIMAL_ID 역순으로 출력
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC


# 아픈 동물 찾기 #
# 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름 조회
# 아이디 순으로 출력
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID


# 어린 동물 찾기 #
# 동물 보호소에 들어온 동물 중 젊은 동물의 아이디, 이름 조회
# 아이디 순으로 출력
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION <> 'Aged'
ORDER BY ANIMAL_ID
# SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID


# 동물의 아이디와 이름 #
# 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID 순으로 조회
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
ORDER BY ANIMAL_ID


# 여러 기준으로 정렬하기 #
# 동물 보호소에 들어온 모든 동물의 아이디, 이름, 보호 시작일을 이름 순으로 조회
# 단, 이름이 같은 동물은 보호를 나중에 시작한 동물을 먼저 보여줘야 함
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC


# 상위 n개 레코드 #
# 동물 보호소에 가장 먼저 들어온 동물의 이름 조회
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1