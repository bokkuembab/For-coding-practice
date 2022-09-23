-- 고양이와 개는 몇 마리 있을까 
-- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회
-- 고양이보다 개 먼저 조회
SELECT ANIMAL_TYPE, COUNT(DISTINCT(ANIMAL_ID)) 'count' 
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE;


-- 동명 동물 수 찾기
-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수 조회
-- 이름이 없는 동물은 집계에서 제외, 이름 순으로 조회
SELECT NAME, COUNT(*) 'COUNT' FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME HAVING COUNT(NAME) >= 2
ORDER BY NAME;


-- 입양 시각 구하기(1)
-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- 시간대 순으로 조회
SELECT HOUR(DATETIME) 'HOUR', COUNT(*) 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME);




-- 입양 시각 구하기(2)
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이 발생했는지 조회
-- 시간대 순으로 정렬
-- SET 함수, @변수 사용
-- SET 함수는 변수 선언 함수
-- '@변수'는 프로시저가 끝나도 계속 유지됨
-- ':=' 은 대입연산. 비교 연산(=)과의 혼동을 피하기 위함

SET @hour := -1;        -- 변수 초기화

SELECT (@hour := @hour + 1) AS HOUR,    -- @hour 변수가 1씩 증가
(SELECT COUNT(*) FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) = @hour) AS COUNT      -- @hour가 0~23일 때의 입양 count
FROM ANIMAL_OUTS
WHERE @hour < 23;    -- @hour가 23보다 작을 동안 반복