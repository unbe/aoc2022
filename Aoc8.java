import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Aoc8 {
	public static void main(String[] args) throws Exception {
		Scanner scanner = new Scanner(new File("input.txt"));
		List<int[]> listmap = new ArrayList<>();
		while (scanner.hasNextLine()) {
			listmap.add(Arrays.stream(scanner.nextLine().split("")).mapToInt(x -> Integer.parseInt(x)).toArray());
		}
		int[][] map = new int[0][0];
		map = listmap.toArray(map);
		// part1(map);
		part2(map);
	}

	private static void part1(int[][] map) {
		boolean[][] visible = new boolean[map.length][map[0].length];
		for (int i = 0; i < map.length; i++) {
			updateLineVisibility(map, visible, i, i + 1, 1, 0, map[0].length, 1);
			updateLineVisibility(map, visible, i, i + 1, 1, map[0].length - 1, -1, -1);
		}
		for (int j = 0; j < map[0].length; j++) {
			updateLineVisibility(map, visible, 0, map.length, 1, j, j+1, 1);
			updateLineVisibility(map, visible, map.length -1, -1, -1, j, j+1, 1);
		}
		int count = 0;
		for (int i = 0; i < visible.length; i++) {
			for (int j = 0; j < visible[i].length; j++) {
				if(visible[i][j]) {
					count++;
				}
			}
		}
		System.out.println(count);
	}

	private static void updateLineVisibility(int[][] map, boolean[][] visible, int istart, int iend, int istep, int jstart, int jend,
			int jstep) {
		int blocker = -1;
		for (int i = istart; i != iend; i += istep) {
			for (int j = jstart; j != jend; j += jstep) {
				if (map[i][j] > blocker) {
					visible[i][j] = true;
					blocker = map[i][j];
				}
			}
		}
	}

	private static void part2(int[][] map) {
		int[][] view = new int[map.length][map[0].length];
		for (int i = 0; i < view.length; i++) {
			Arrays.fill(view[i], 1);
		}
		for (int i = 0; i < map.length; i++) {
  		  updateLineView(map, view, i, i+1, 1, 0, map[0].length, 1, 0, 1);
  		  updateLineView(map, view, i, i + 1, 1, map[0].length - 1, -1, -1, 0, 1);
		}
		for (int j = 0; j < map[0].length; j++) {
			updateLineView(map, view, 0, map.length, 1, j, j+1, 1, 1, 0);
			updateLineView(map, view, map.length -1, -1, -1, j, j+1, 1, 1, 0);
		}
		int max = 0;
		for (int i = 0; i < view.length; i++) {
			max = Math.max(max, Arrays.stream(view[i]).max().getAsInt());
		}
		System.out.println(max);
	}

	private static void updateLineView(int[][] map, int[][] view,int istart, int iend, int istep, int jstart, int jend,
			int jstep, int imul, int jmul) {
		int[] blockers = new int[10];
		Arrays.fill(blockers, istart*imul + jstart*jmul);
		for (int i = istart; i != iend; i += istep) {
			for (int j = jstart; j != jend; j += jstep) {
				int idx = i*imul + j*jmul;
				int blockerIdx = blockers[map[i][j]];
				view[i][j] *= Math.abs(idx - blockerIdx);
				for (int b = 0; b <= map[i][j]; b++) {
					blockers[b] = idx;
				}
			}
		}
	}

}
