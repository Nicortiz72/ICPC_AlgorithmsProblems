import java.io.*;
import java.util.*;

public class reaux {

	private static final HashMap<String, LinkedList<String>[]> table = new HashMap<String, LinkedList<String>[]>();


	public static String localFormat(final int value) {
		if (value == 1) {
			return "point";
		} else {
			return "points";
		}
	}
	
	public static void main(final String [] args) throws Exception {
		 LinkedList<String>[] cs = new LinkedList[3];
		 cs[0] = new LinkedList<String>();
		 cs[0].add("Kamen");
		 cs[1] = new LinkedList<String>();
		 cs[1].add("Nuzky");
		 cs[2] = new LinkedList<String>();
		 cs[2].add("Papir");

		 table.put("cs", cs);

		 LinkedList<String>[] en = new LinkedList[3];
		 en[0] = new LinkedList<String>();
		 en[0].add("Rock");
		 en[1] = new LinkedList<String>();
		 en[1].add("Scissors");
		 en[2] = new LinkedList<String>();
		 en[2].add("Paper");

		 table.put("en", en);

		 LinkedList<String>[] fr = new LinkedList[3];
		 fr[0] = new LinkedList<String>();
		 fr[0].add("Pierre");
		 fr[1] = new LinkedList<String>();
		 fr[1].add("Ciseaux");
		 fr[2] = new LinkedList<String>();
		 fr[2].add("Feuille");

		 table.put("fr", fr);

		 LinkedList<String>[] de = new LinkedList[3];
		 de[0] = new LinkedList<String>();
		 de[0].add("Stein");
		 de[1] = new LinkedList<String>();
		 de[1].add("Schere");
		 de[2] = new LinkedList<String>();
		 de[2].add("Papier");

		 table.put("de", de);

		 LinkedList<String>[] hu = new LinkedList[3];
		 hu[0] = new LinkedList<String>();
		 hu[0].add("Ko");
		 hu[0].add("Koe");

		 hu[1] = new LinkedList<String>();
		 hu[1].add("Ollo");
		 hu[1].add("Olloo");

		 hu[2] = new LinkedList<String>();
		 hu[2].add("Papir");

		 table.put("hu", hu);

		 LinkedList<String>[] it = new LinkedList[3];
		 it[0] = new LinkedList<String>();
		 it[0].add("Sasso");
		 it[0].add("Roccia");

		 it[1] = new LinkedList<String>();
		 it[1].add("Forbice");

		 it[2] = new LinkedList<String>();
		 it[2].add("Carta");
		 it[2].add("Rete");

		 table.put("it", it);

		 LinkedList<String>[] jp = new LinkedList[3];
		 jp[0] = new LinkedList<String>();
		 jp[0].add("Guu");

		 jp[1] = new LinkedList<String>();
		 jp[1].add("Choki");

		 jp[2] = new LinkedList<String>();
		 jp[2].add("Paa");
		 table.put("jp", jp);

		 LinkedList<String>[] pl = new LinkedList[3];
		 pl[0] = new LinkedList<String>();
		 pl[0].add("Kamien");

		 pl[1] = new LinkedList<String>();
		 pl[1].add("Nozyce");

		 pl[2] = new LinkedList<String>();
		 pl[2].add("Papier");
		 table.put("pl", pl);

		 LinkedList<String>[] es = new LinkedList[3];
		 es[0] = new LinkedList<String>();
		 es[0].add("Piedra");

		 es[1] = new LinkedList<String>();
		 es[1].add("Tijera");

		 es[2] = new LinkedList<String>();
		 es[2].add("Papel");
		 table.put("es", es);

		 final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		 final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		 
		 String line = reader.readLine().trim();
		 int game = 1;
		 String [] parts = null;
		 while (line != null) {
		 	parts = line.split(" ");
		 	String playerALanguage = parts[0];
		 	String playerAName = parts[1];

		 	parts = reader.readLine().trim().split(" ");
		 	String playerBLanguage = parts[0];
		 	String playerBName = parts[1];

		 	int playerAScore = 0;
		 	int playerBScore = 0;

		 	line = reader.readLine().trim();
		 	while (line.length() != 1) {
		 		if (line.equals(".") || line.equals("-"))
		 			break;

		 		parts = line.split(" ");
		 		String playerAThrow = parts[0];
		 		String playerBThrow = parts[1];

		 		int playerAIndex = 0;
		 		int playerBIndex = 0;

		 		outer : for (int i = 0; i < table.get(playerALanguage).length; ++ i) {
		 			for (String word : table.get(playerALanguage)[i]) {
		 				if (word.equals(playerAThrow)) {
		 					playerAIndex = i;
		 					break outer;
		 				}
		 			}
		 		}

		 		outer : for (int i = 0; i < table.get(playerBLanguage).length; ++ i) {
		 			for (String word : table.get(playerBLanguage)[i]) {
		 				if (word.equals(playerBThrow)) {
		 					playerBIndex = i;
		 					break outer;
		 				}
		 			}
		 		}

		 		if (playerAIndex == 0 && playerBIndex == 1) {
					playerAScore += 1;
				}

				if (playerAIndex == 0 && playerBIndex == 2) {
					playerBScore += 1;
				}

				if (playerAIndex == 1 && playerBIndex == 0) {
					playerBScore += 1;
				}

				if (playerAIndex == 1 && playerBIndex == 2) {
					playerAScore += 1;
				}

				if (playerAIndex == 2 && playerBIndex == 0) {
					playerAScore += 1;
				}

				if (playerAIndex == 2 && playerBIndex == 1) {
					playerBScore += 1;
				}

				line = reader.readLine();
				if (line == null) {
					break;
				} else {
					line = line.trim();
				}
		 	}

			writer.write("Game #" + game + ":\n");
			writer.write(playerAName + ": " + playerAScore + " " + localFormat(playerAScore) + "\n");
			writer.write(playerBName + ": " + playerBScore + " " + localFormat(playerBScore) + "\n");
			if (playerAScore == playerBScore) {
				writer.write("TIED GAME\n");
			} else if (playerAScore > playerBScore) {
				writer.write("WINNER: " + playerAName + "\n");
			} else {
				writer.write("WINNER: " + playerBName + "\n");
			}
			writer.write("\n");

			game += 1;
			if (line.equals(".")) {
				break;
			}
			line = reader.readLine().trim();
		}
		writer.close();
		reader.close();
	}
}