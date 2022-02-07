SELECT *
FROM (
		SELECT DISTINCT  a.time_id,
			b.subscriber_count,
			b.channel_id,
			c.channel_name
		FROM (
				SELECT time_id,
					day,
					hour
				FROM "{database}"."dimtimechannel"
				WHERE add_date = CAST('{add_date}' AS DATE)
					AND hour = {hour}
			) AS a
			INNER JOIN (
				SELECT time_id,
					subscriber_count,
					channel_id
				FROM "{database}"."factchannel"
			) AS b ON a.time_id = b.time_id
			INNER JOIN(
				SELECT *
				FROM "{database}"."dimchannel"
			) AS c ON b.channel_id = c.channel_id
	)
ORDER BY subscriber_count DESC
LIMIT 3;