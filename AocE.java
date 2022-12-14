import java.awt.Point;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;

public class AocD {
	private static Map<Integer, SortedSet<Integer>> rocks = new HashMap<>();

	private static Integer floor = null;

	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(new File("input.txt"));
		while (scanner.hasNextLine()) {
			String[] nodes = scanner.nextLine().split(" -> ");
			for (int i = 0; i < nodes.length - 1; i++) {
				fillRock(nodes[i], nodes[i + 1]);
			}
		}
		part2();
	}

	private static void part2() {
		floor = rocks.values().stream().map(col -> col.last()).max(Integer::compare).get() + 2;
		part1();
	}

	private static void part1() {
		int i;
		for (i = 0; i < 50000; i++) {
			Point sand = new Point(500, 0);
			if (drop(sand) != 1) {
				break;
			}
		}
		System.out.println(i);
	}

	private static Integer landingPoint(Point sand) {
		SortedSet<Integer> column = rocks.get(sand.x);
		if (column == null) {
			return floor;
		}
		SortedSet<Integer> below = column.tailSet(sand.y);
		if (below.isEmpty()) {
			return floor;
		}
		return below.first();
	}

	private static int drop(Point sand) {
		Integer land = landingPoint(sand);
		if (land == null) {
			return -1;
		}
		if (land <= sand.y) {
			return 0;
		}
		int dropSide = drop(new Point(sand.x - 1, land));
		if (dropSide != 0) {
			return dropSide;
		}
		dropSide = drop(new Point(sand.x + 1, land));
		if (dropSide != 0) {
			return dropSide;
		}
		place(new Point(sand.x, land - 1));
		return 1;
	}

	private static void fillRock(String fromString, String toString) {
		Point from = parsePoint(fromString);
		Point to = parsePoint(toString);
		Point d = new Point(to);
		d.translate(-from.x, -from.y);
		if (d.x != 0) {
			d.x = d.x / Math.abs(d.x);
		}
		if (d.y != 0) {
			d.y = d.y / Math.abs(d.y);
		}
		while (!from.equals(to)) {
			place(from);
			from.translate(d.x, d.y);
		}
		place(from);
	}

	private static void place(Point rock) {
		if (rocks.get(rock.x) == null) {
			rocks.put(rock.x, new TreeSet<>());
		}
		rocks.get(rock.x).add(rock.y);
	}

	private static Point parsePoint(String point) {
		String[] coords = point.split(",");
		return new Point(Integer.valueOf(coords[0]), Integer.valueOf(coords[1]));
	}
}
