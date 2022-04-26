SELECT *
FROM (
		SELECT DISTINCT  a.time_id,
		    a.add_date,
		    a.hour,
			b.like_count,
			b.video_id,
			c.title
		FROM (
				SELECT time_id,
					add_date,
					hour
				FROM "{database}"."dimtimevideo"
				WHERE add_date = CAST('{add_date}' AS DATE)
					AND hour = {hour}
			) AS a
			INNER JOIN (
				SELECT *
				FROM "{database}"."factvideo"
			) AS b ON a.time_id = b.time_id
			INNER JOIN(
				SELECT *
				FROM "{database}"."dimvideo"
			) AS c ON b.video_id = c.video_id
	)
ORDER BY like_count DESC
LIMIT 3;