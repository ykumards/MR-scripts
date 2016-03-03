DEFINE streamer `streamer.py` SHIP ('streamer.py');
A = LOAD 'input.txt';
tweet_count = STREAM A THROUGH streamer AS (Java:int, hackathon:int, Chicago:int, Dec:int);
club = GROUP tweet_count ALL;
Java = foreach club generate SUM(tweet_count.Java);
Chicago = foreach club generate SUM(tweet_count.Chicago);
hackathon = foreach club generate SUM(tweet_count.hackathon);
Dec = foreach club generate SUM(tweet_count.Dec);
-- Storing the counts

STORE Java INTO 'Java';
STORE Chicago INTO 'Chicago';
STORE hackathon INTO 'hackathon';
STORE Dec INTO 'Dec';

