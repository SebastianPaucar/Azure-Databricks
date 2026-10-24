WITH items AS (
    SELECT i.seller_id,
           o.order_id,
           o.purchase_ts,
           o.is_late,
           i.price
    FROM {silver_items} i
    JOIN {silver_orders} o ON o.order_id = i.order_id
    WHERE o.order_status = 'delivered'
      AND o.delivered_ts IS NOT NULL
      AND CAST(o.purchase_ts AS DATE) <= DATE'{cutoff}'
),
cohort AS (
    SELECT seller_id,
           trunc(CAST(MIN(purchase_ts) AS DATE), 'MM') AS cohort_month
    FROM items
    GROUP BY seller_id
)
SELECT c.cohort_month,
       CAST(months_between(trunc(CAST(i.purchase_ts AS DATE), 'MM'), c.cohort_month) AS INT) AS mob,
       CAST(SUM(CASE WHEN i.is_late THEN i.price ELSE 0 END) AS DECIMAL(18,2)) AS late_amount,
       CAST(SUM(i.price) AS DECIMAL(18,2))                                     AS total_amount,
       COUNT(DISTINCT i.order_id)                                              AS order_count,
       COUNT(DISTINCT CASE WHEN i.is_late THEN i.order_id END)                 AS late_order_count
FROM items i
JOIN cohort c ON c.seller_id = i.seller_id
WHERE months_between(trunc(CAST(i.purchase_ts AS DATE), 'MM'), c.cohort_month) <= {max_mob}
GROUP BY c.cohort_month,
         CAST(months_between(trunc(CAST(i.purchase_ts AS DATE), 'MM'), c.cohort_month) AS INT)
