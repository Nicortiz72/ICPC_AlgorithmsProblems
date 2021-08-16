import java.io.*;
import java.util.*;

public class ends {

	public static int tab(final int [] c) {
		int N = c.length;
		int [][] tab = new int[N + 1][N + 1];
		for (int i = 0; i < N; ++ i) {
			if (i < N) {
				tab[i][i + 1] = -c[i];
			}
		}
		int n = N - 2;
		int m = N;

		while (n != -1) {
			if (m == N + 1) {
				n = n - 1;
				m = n + 2;
			}
			if (n == -1) {
				break;
			}
			int tmp = Math.max(c[n], c[m - 1]);
			if (c[n] >= c[m - 1]) {
				tab[n][m] = Math.max(c[n + 1] + tab[n + 2][m], c[m - 1] + tab[n + 1][m - 1]) - tmp;
			} else {
				tab[n][m] = Math.max(c[n] + tab[n + 1][m - 1], c[m - 2] + tab[n][m - 2]) - tmp;
			}
			m += 1;
		}
		int ans = Math.max(c[0] + tab[1][N], c[N - 1] + tab[0][N - 1]);
		return ans;
	}
	
	public static void main(final String [] args) throws Exception {
		final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));	
		String line = reader.readLine().trim();
		int cont = 1;
		String [] parts = null;
		while (!line.equals("0")) {
			parts = line.split(" ");
			int [] c = new int[parts.length - 1];
			for (int i = 1; i <= c.length; ++ i) {
				c[i - 1] = Integer.parseInt(parts[i]);
			}
			writer.write("In game " + cont + ", the greedy strategy might lose by as many as " + tab(c) + " points.\n");
			line = reader.readLine().trim();
			cont += 1;
		}	 
		writer.close();
		reader.close();
	}
}