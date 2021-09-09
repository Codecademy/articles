SELECT
  COUNT(start_subscribers.subscriber_id) AS inital_active_subscribers,
  COUNT(churn_subscribers.subscriber_id) AS churn_subscribers,
  (CAST(COUNT(churn_subscribers.subscriber_id) AS FLOAT) /
  CAST(COUNT(start_subscribers.subscriber_id) AS FLOAT)) * 100.0 AS churn_rate
FROM
  (SELECT 
    subscribers.subscriber_id
  FROM
    subscribers CROSS JOIN 
    (SELECT 
       CAST('2020-01-01' AS DATE) period_start, 
       CAST('2020-01-31' AS DATE) period_end
    ) AS period
  WHERE
    subscribers.start_date < period.period_start AND
    COALESCE(subscribers.end_date, period.period_start) >= period.period_start
  ) AS start_subscribers
  LEFT JOIN
  (SELECT
     subscribers.subscriber_id
   FROM
     subscribers CROSS JOIN 
     (SELECT 
       CAST('2020-01-01' AS DATE) period_start, 
       CAST('2020-01-31' AS DATE) period_end
      ) AS period
   WHERE
     subscribers.start_date < period.period_start AND
     subscribers.end_date >= period.period_start AND
     subscribers.end_date <= period.period_end
  ) AS churn_subscribers
  ON start_subscribers.subscriber_id = churn_subscribers.subscriber_id
