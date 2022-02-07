SELECT *
FROM (
		SELECT DISTINCT  a.time_id,
			b.like_count,
			b.video_id,
			c.title
		FROM (
				SELECT *
				FROM "{database}"."dimtimechannel"
				WHERE add_date = CAST(`{add_date}` AS DATE)
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