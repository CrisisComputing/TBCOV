package qa.qcri.tweetsretrieval;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOError;
import java.io.IOException;
import java.io.Writer;
import java.nio.file.Files;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.stream.Collectors;

import javax.json.JsonArray;

public class TweetsRetrievalTool {
	
	private static final String NEWLINE = System.getProperty("line.separator");

	public static void main(String[] args) throws IOException {
		if (args.length<2) {
			System.err.println("This app needs two parameters: source and destination files.");
			return;
		}
		
		Properties p = new Properties();
		p.load(new FileInputStream("twitter.properties"));
		
		TwitterAPI twitter = new TwitterAPI(p);
		
		List<String> lines = Files.readAllLines(new File(args[0]).toPath());
		int[] r = new int[]{0};
		Map<Object, List<String>> groups = lines.stream()
				.collect(Collectors.groupingBy(x -> r[0]++ / 100));
		
		try(Writer dest = new FileWriter(new File(args[1]))) {
			groups.forEach((key, value) -> {
				List<String> ids = value.stream()
						.map(s -> s.replace("'", ""))
						.collect(Collectors.toList());
				try {
					JsonArray tweets = 
							(JsonArray) twitter.getStatusesLookup(String.join(",", ids));
					tweets.forEach(t -> {
						try { 
							dest.write(t.toString());
							dest.write(NEWLINE);
						} catch (IOException e) {
							throw new IOError(e);
						}
					});
					//System.out.println(key+" "+tweets.size()+"/"+ids.size());
				} catch (Exception e) {
					throw new IOError(e);
				}
			});
		}
	}
	
}
