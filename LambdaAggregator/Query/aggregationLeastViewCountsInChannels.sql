SELECT *
FROM (
		SELECT DISTINCT a.time_id,
			b.view_count,
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
					view_count,
					channel_id
				FROM "{database}"."factchannel"
			) AS b ON a.time_id = b.time_id
			INNER JOIN(
				SELECT *
				FROM "{database}"."dimchannel"
			) AS c ON b.channel_id = c.channel_id
	)
ORDER BY view_count ASC
LIMIT 3;