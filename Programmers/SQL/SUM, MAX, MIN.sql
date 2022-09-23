# 최댓값 구하기
# 가장 최근에 들어온 동물은 언제 들어왔는지 조회
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
# SELECT MAX(DATETIME) FROM ANIMAL_INS


# 최솟값 구하기
# 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회
SELECT DATETIME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
# SELECT MIN(DATETIME) FROM ANIMAL_INS


# 동물 수 구하기
# 동물 보호소에 동물이 몇 마리 들어왔는지 조회
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS


# 중복 제거하기
# 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회
# 이름이 NULL인 경우는 집계 X, 중복 이름은 하나로 간주
SELECT COUNT(DISTINCT(NAME)) FROM ANIMAL_INS
WHERE NAME IS NOT NULL