package qa.qcri.tweetsretrieval;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Properties;
import java.util.logging.Logger;
import java.util.zip.GZIPInputStream;

import javax.json.Json;
import javax.json.JsonArray;
import javax.json.JsonReader;

import oauth.signpost.OAuthConsumer;
import oauth.signpost.basic.DefaultOAuthConsumer;
import oauth.signpost.exception.OAuthException;

public class TwitterAPI {
	
	private static final Logger log = Logger.getLogger(TwitterAPI.class.getName());
	private static final String BASE = "https://api.twitter.com";

	private OAuthConsumer consumer;
	
	public TwitterAPI(Properties p) {
		consumer = new DefaultOAuthConsumer(p.getProperty("consumer.key"), p.getProperty("consumer.secret"));
		consumer.setTokenWithSecret(p.getProperty("access.token"), p.getProperty("access.token.secret"));
	}
	
	protected Object call(String url) throws IOException, InterruptedException, OAuthException {
		URL url2 = new URL(consumer.sign(url));
		HttpURLConnection conn = (HttpURLConnection) url2.openConnection();
		conn.setRequestProperty("Accept-Encoding", "gzip");
		int rc = conn.getResponseCode();
		InputStream stream = null;
		switch (rc) {
		case HttpURLConnection.HTTP_OK:
			stream = conn.getInputStream();
			break;
		case HttpURLConnection.HTTP_FORBIDDEN:
			stream = conn.getErrorStream();
			break;
		case 429: // https://dev.twitter.com/rest/public/rate-limiting
			long reset = 1000 * conn.getHeaderFieldLong("X-Rate-Limit-Reset", 0);
			long millis = reset - System.currentTimeMillis();
			if (millis < 60000) {
				log.info(String.format("waiting for %d sec (API call rate limit exceeded)", millis/1_000));
			} else {
				log.info(String.format("waiting for %d min (API call rate limit exceeded)", millis/60_000));
			}
			Thread.sleep(millis+1000);
			return call(url);
		default:
			throw new IOException(conn.getResponseMessage());
		}
		if ("gzip".equals(conn.getHeaderField("Content-Encoding")))
			stream = new GZIPInputStream(stream);
		
		int limit = conn.getHeaderFieldInt("X-Rate-Limit-Limit", 0);
		int remaining = conn.getHeaderFieldInt("X-Rate-Limit-Remaining", 0);
		long reset = conn.getHeaderFieldLong("X-Rate-Limit-Reset", 0);
		log.info(String.format("%d/%d(%d)", limit, remaining, reset));
		
		JsonReader in = Json.createReader(stream);
		return in.read();
	}

	public JsonArray getStatusesLookup(String jobid) throws IOException, InterruptedException, OAuthException {
		String endpoint = BASE+"/1.1/statuses/lookup.json?id="+jobid;
		return (JsonArray) call(endpoint);
	}

}
