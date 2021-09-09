WITH period (period_start, period_end)
AS
(SELECT 
/*
This is the code in ANSI SQL
 
  CAST('2020-01-01' AS DATE) period_start, 
  CAST('2020-01-31' AS DATE) period_end

For SQLite we need to use DATE() instead of CAST() for the
example to work properly */

DATE('2020-01-01') period_start,
DATE('2020-01-31') period_end 
),

start_subscribers (subscriber_id)
AS
(SELECT 
  subscribers.subscriber_id
FROM
  subscribers CROSS JOIN period
WHERE
  subscribers.start_date < period.period_start AND
  COALESCE(subscribers.end_date, period.period_start) >= period.period_start
),

churn_subscribers (subscriber_id)
AS
(SELECT
  subscribers.subscriber_id
FROM
  subscribers CROSS JOIN period
WHERE
  subscribers.start_date < period.period_start AND
  subscribers.end_date >= period.period_start AND
  subscribers.end_date <= period.period_end
)

SELECT
  COUNT(start_subscribers.subscriber_id) AS inital_active_subscribers,
  COUNT(churn_subscribers.subscriber_id) AS churn_subscribers,
  (CAST(COUNT(churn_subscribers.subscriber_id) AS FLOAT) /
  CAST(COUNT(start_subscribers.subscriber_id) AS FLOAT)) * 100.0 AS churn_rate
FROM
  start_subscribers 
    LEFT JOIN churn_subscribers 
    ON start_subscribers.subscriber_id = churn_subscribers.subscriber_id

