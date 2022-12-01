import java.io.File;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Aoc1p2 {

	public static void main(String[] args) throws Exception {
		Scanner scanner = new Scanner(new File("input.txt"));
		PriorityQueue<Integer> top3 = new PriorityQueue<>();
		int elfsum = 0;
		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();
			if (line.isEmpty()) {
				top3.add(elfsum);
				while (top3.size() > 3) {
					top3.poll();
				}
				elfsum = 0;
			} else {
				elfsum += Integer.parseInt(line);
			}
			
		}
		scanner.close();
		System.out.println(top3.stream().mapToInt(Integer::intValue).sum());
	}
}
