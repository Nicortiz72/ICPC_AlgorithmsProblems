from py2neo import Graph, Node, Relationship
from sys import stdin
import os

twitter = Graph("http://localhost:7474/browser/", host="localhost", password="1234")

def genesis():
	dic=twitter.run(
	"""
	CREATE (Nicol:User {Name:'Nicolás Ortiz', UserName:'Worm@twitter.com', Password:'w000rm', UserType:'Private', City:'Bogota'})
	CREATE (Jhoan:User {Name:'Jhoan Lozano',UserName:'JhoanLoz@twitter.com',Password:'y15s52', UserType:'Public', City:'Bogota', Country:'Colombia'})
	CREATE (xg:User    {Name:'Xavier Garzón', UserName:'xg@twitter.com', Password:'Cr46kq', UserType:'Private', City:'Cali'})

	CREATE (User2:User {Name:'Natalia Ruiz', UserName:'NataRuiz@twitter.com', Password:'54wgh54f', UserType:'Public', City:'Yumbo'})
	CREATE (User3:User {Name:'Sofía Giraldo', UserName:'SofiGi98@twitter.com', Password:'fg5$G5F4', UserType:'Public', Country:'Chile'})
	CREATE (User4:User {Name:'Mariana Revilla', UserName:'marianare@twitter.com', Password:'fgbF4S4', UserType:'Public', City:'Palmira'})
	CREATE (User5:User {Name:'Valentina Ramirez', UserName:'tinara@twitter.com', Password:'4vbfdbv', UserType:'Private', City:'Salento', Country:'Colombia'})

	CREATE (Visitante1:general)
	CREATE (Visitante2:general)
	CREATE (Visitante3:general)

	
	CREATE (tw0:Tweet {Id:0, Contenido:'¡Tengo hambre!', Dirigido:['xg@twitter.com', 'Worm@twitter.com']})
	CREATE (tw1:Tweet {Id:1, Contenido:'¿Quién para McDonalds?', Hashtag:'#TengoHambre', Dirigido:['JhoanLoz@twitter.com', 'xg@twitter.com']})
	CREATE (tw2:Tweet {Id:2, Contenido:'Vamos y me pagas la apuesta que me debes', Hashtag:'#PaguenLasApuestas', Dirigido:['Worm@twitter.com']})
	CREATE (tw3:Tweet {Id:3, Contenido:'Dale, vamos'})
	CREATE (tw4:Tweet {Id:4, Contenido:'¡Qué gran fiesta la de ayer! ¡Fue increible!', Hashtag:['#GranNoche','#HayQueRepetir'], Dirigido:['xg@twitter.com']})
	CREATE (tw5:Tweet {Id:5, Contenido:'Buena esa'})
	CREATE (tw6:Tweet {Id:6, Contenido:'Buenas noches'})
	CREATE (tw7:Tweet {Id:7, Contenido:'Mi equipo favorito ganó el campeonato'})
	CREATE (tw8:Tweet {Id:8, Contenido:'Me retiro de la aviación', Hashtag:['#FAC']})
	CREATE (tw9:Tweet {Id:9, Contenido:'Adiós septiembre, hola octubre...', Hashtag:['#Hallowen']})

	CREATE (Nicol)-[:Puede_Leer_A]->(xg)
	CREATE (Jhoan)-[:Puede_Leer_A]->(xg)
	CREATE (xg)-[:Puede_Leer_A]->(Nicol)
	CREATE (xg)-[:Sigue_a]->(Jhoan)
	CREATE (Jhoan)-[:Puede_Leer_A]->(Nicol)
	CREATE (Nicol)-[:Sigue_a]->(Jhoan)

	CREATE (xg)-[:Sigue_a]->(User2)
	CREATE (xg)-[:Sigue_a]->(User3)
	CREATE (xg)-[:Sigue_a]->(User4)

	CREATE (User2)-[:Sigue_a]->(xg)
	CREATE (User3)-[:Sigue_a]->(xg)
	CREATE (User4)-[:Sigue_a]->(xg)
	CREATE (User5)-[:Sigue_a]->(xg)

	CREATE (User2)-[:Sigue_a]->(User3)
	CREATE (User3)-[:Sigue_a]->(Nicol)
	CREATE (User4)-[:Sigue_a]->(Jhoan)
	CREATE (User5)-[:Sigue_a]->(User2)

	CREATE (Nicol)-[:Sigue_a]->(User2)
	CREATE (Nicol)-[:Sigue_a]->(User3)
	CREATE (Nicol)-[:Sigue_a]->(User4)

	CREATE (Jhoan)-[:Sigue_a]->(User3)

	CREATE (User5)-[:Sigue_a]->(User3)

	CREATE (Jhoan)-[:Realizó_Publicación]->(tw0)
	CREATE (Nicol)-[:Leyó_Tweet]->(tw0)
	CREATE (xg)-[:Leyó_Tweet]->(tw0)
	CREATE (Nicol)-[:Realizó_Publicación]->(tw1)
	CREATE (xg)-[:Leyó_Tweet]->(tw1)
	CREATE (Jhoan)-[:Leyó_Tweet]->(tw1)
	CREATE (xg)-[:Realizó_Publicación]->(tw2)
	CREATE (Jhoan)-[:Leyó_Tweet]->(tw2)
	CREATE (Nicol)-[:Leyó_Tweet]->(tw2)
	CREATE (Jhoan)-[:Realizó_Publicación]->(tw3)

	CREATE (User2)-[:Realizó_Publicación]->(tw4)

	CREATE (Visitante1)-[:Leyó_Tweet]->(tw0)
	CREATE (Visitante1)-[:Leyó_Tweet]->(tw3)

	CREATE (xg)-[:Realizó_Publicación]->(tw5)

	CREATE (User1)-[:Realizó_Publicación]->(tw6)
	CREATE (User2)-[:Realizó_Publicación]->(tw7)
	CREATE (User3)-[:Realizó_Publicación]->(tw8)
	CREATE (User3)-[:Realizó_Publicación]->(tw9)
	""")


def reset():
	twitter.run("MATCH (n) DETACH DELETE n")

def esUser(usuario):
	user = twitter.run("MATCH (a:User) WHERE a.UserName='{}' RETURN a.UserName".format(usuario)).evaluate()
	if user == usuario: return True
	else: return False

# 1.
def publicacion(usuario):
	"""
	Los mensajes que el usuario ha enviado, y si son dirigidos, la lista de los usuarios a quien los envió. Estos
	mensajes deben estar en orden cronológico, empezando por el más reciente.
	"""
	a = """
	MATCH (a)-[:Realizó_Publicación]->(t) WHERE a.UserName = '{}'
	RETURN a.Name AS Remitente, t.Id as ID_Tweet, t.Contenido AS Tweet, t.Dirigido AS Receptor
	""".format(usuario)
	info = twitter.run(a).data()

	for i in range(len(info)):
		print("\nRemitente:", info[i]["Remitente"], "\nID_Tweet:", info[i]["ID_Tweet"], "\nContenido:", info[i]["Tweet"], end=" ")
		print( "\nReceptor(es):", info[i]["Receptor"] if info[i]["Receptor"] != None else "Sin etiquetados")
		print("\n=================================")

def dirigidos(usuario):
	"""
	Los mensajes dirigidos que recibió, quien se los envió y si está disponible, la ciudad del usuario que lo
	envió. Estos mensajes deben estar en orden cronológico, empezando por el más reciente.
	"""
	a = """
	MATCH (a:User)-[:Realizó_Publicación]->(b:Tweet), (c:User)
	UNWIND b.Dirigido as word
	WITH a, b, c, word
	WHERE word = '{}' AND c.UserName = word
	RETURN a.Name AS Remitente, b.Id as ID_Tweet, b.Contenido AS Tweet, c.Name AS Receptor
	""".format(usuario)
	info = twitter.run(a).data()
	print( "\nReceptor:", info[0]["Receptor"])
	for i in range(len(info)):
		print("\nRemitente:", info[i]["Remitente"], "\nID_Tweet:", info[i]["ID_Tweet"], "\nContenido:", info[i]["Tweet"])		
		print("\n=================================")

def ultimos_mns(usuario):
	"""
	Los últimos 5 mensajes que han publicado cada uno de los usuarios a los que sigue. Estos mensajes deben
	estar en orden cronológico, empezando por el más reciente, y agrupados por el usuario que los publica.
	"""
	ans = [[] for _ in range(5)]
	a = """
	MATCH (a:User)-[:Sigue_a]->(b:User)-[:Realizó_Publicación]->(c:Tweet)
	WHERE a.UserName = '{}'
	RETURN a.Name AS El_Seguidor, b.Name AS Remitente, c.Id AS ID_Tweet, c.Contenido AS Tweet
	ORDER BY c.Id, b.UserName
	LIMIT 5
	""".format(usuario)
	info = twitter.run(a).data()
	print( "\nEl Seguidor:", info[0]["El_Seguidor"])
	for i in range(len(info)-1,-1,-1):
		print("\nRemitente:", info[i]['Remitente'], "\nID Tweet:", info[i]["ID_Tweet"], "\nContenido:", info[i]["Tweet"])
		print("\n=================================")

def ingresar_app(usuario):
	"""
	1. Recuperar los datos que se van a mostrar al usuario cuando ingresa a la aplicación (recibe como
	parámetro el dato del usuario).
	"""
	print("\n||||||||||||||||||||||||||||||",1.1,"||||||||||||||||||||||||||||||\n")
	publicacion(usuario)
	print("\n||||||||||||||||||||||||||||||",1.2,"||||||||||||||||||||||||||||||\n")
	dirigidos(usuario)
	print("\n||||||||||||||||||||||||||||||",1.3,"||||||||||||||||||||||||||||||\n")
	ultimos_mns(usuario)



# 2.
def seguidos(usuario):
	"""
	2. Listar los usuarios a los que sigue un usuario dado (recibe como parámetro el dato del usuario).
	"""
	a = """MATCH (a:User)-[:Sigue_a]->(b:User)
	WHERE a.UserName = '{}'
	RETURN b.Name AS Seguidos
	""".format(usuario)
	info = twitter.run(a).data()
	print("\nSigue a:")
	for i in range(len(info)):
		print("\n{}. ".format(i+1), info[i]['Seguidos'])

#3.
def seguidores(usuario): 
	"""
	Listar los usuarios que siguen a un usuario dado (recibe como parámetro el dato del usuario).
	"""
	a = """
	MATCH (a:User)-[:Sigue_a]->(b:User)
	WHERE b.UserName = '{}'
	RETURN a.Name AS Seguidores
	""".format(usuario)
	info = twitter.run(a).data()
	print("\n lo siguen:")
	for i in range(len(info)):
		print("\n{}. ".format(i+1), info[i]['Seguidores'])
#4. Quinto_Seguidor('xg@twitter.com')
def Quinto_Seguidor(usuario):
	"""
	Listar los seguidores de los seguidores de los seguidores (hasta nivel 5) de un usuario dado (recibe
	como parámetro el dato del usuario).
	"""
	a = """
	MATCH (p:User)-[:Sigue_a]->(a:User)-[:Sigue_a]->(b:User)-[:Sigue_a]->(c:User)-[:Sigue_a]->(d:User)-[:Sigue_a]->(e:User)
	WHERE e.UserName = '{}' AND (e.UserName <> a.UserName) AND (e.UserName <> b.UserName) AND (e.UserName <> c.UserName) AND (e.UserName <> d.UserName) AND (e.UserName <> p.UserName)
	RETURN DISTINCT p.Name AS Sigue_Al_De_Alla0, a.Name AS Sigue_Al_De_Alla1, b.Name AS Sigue_Al_De_Alla2,  c.Name AS Sigue_Al_De_Alla3,  d.Name AS Sigue_Al_De_Alla4, e.Name AS Busqueda
	""".format(usuario)
	info =twitter.run(a).data()
	print(info)
	print("\nQuinto seguidor:")
	for i in range(len(info)):
		print("\n","{}.".format(i+1),info[i]['Sigue_Al_De_Alla0'], "-->", info[i]['Sigue_Al_De_Alla1'], "-->", info[i]["Sigue_Al_De_Alla2"], "-->", info[i]["Sigue_Al_De_Alla3"], "-->", info[i]["Sigue_Al_De_Alla4"], "-->", info[i]["Busqueda"])
	

def main():
	os.system('cls')	
	i=1
	users = twitter.run("MATCH (a:User) RETURN a.UserName").data()
	while (i==1):
		print("---------------->   T W I T T E R   <----------------\n")
		print("                  Menú de consultas\n\n")
		print("1. Consultar datos de un usuario\n")
		print("2. Seguidos de un usuario\n")
		print("3. Seguidores de un usuario\n")
		print("4. Quinto seguidor en cadena de un usuario\n")
		print("5. Salir\n")

		opcion = input()


		if (opcion == '1'):
			print("Ingrese el nombre del usuario que desea consultar: ")
			usuario_i = input()
			usuario_i=usuario_i+"@twitter.com"
			if (esUser(usuario_i)):
				ingresar_app(usuario_i)
			else:
				print("El usuario no se encuentra en el sistema")

		elif (opcion == '2'):
			print("Ingrese el nombre del usuario que desea consultar: ")
			usuario_i = input()
			usuario_i=usuario_i+"@twitter.com"
			if (esUser(usuario_i)):
				seguidos(usuario_i)
			else:
				print("El usuario no se encuentra en el sistema")
		elif (opcion == '3'):
			print("Ingrese el nombre del usuario que desea consultar: ")
			usuario_i = input()
			usuario_i=usuario_i+"@twitter.com"
			if (esUser(usuario_i)):
				seguidores(usuario_i)
			else:
				print("El usuario no se encuentra en el sistema")
		elif (opcion == '4'):
			print("Ingrese el nombre del usuario que desea consultar: ")
			usuario_i = input()
			usuario_i=usuario_i+"@twitter.com"
			if (esUser(usuario_i)):
				Quinto_Seguidor(usuario_i)
			else:
				print("El usuario no se encuentra en el sistema")
		elif (opcion == '5'):
			i=0
		else:
			os.system('cls')
		print("Ingrese una opción válida")		
		print("\n Presiones enter para continuar...")	
		x=input()		
		os.system('cls')
main()