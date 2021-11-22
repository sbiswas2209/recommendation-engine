from src.common.constants import uri, username, password
from neo4j import GraphDatabase


async def getMovieByNameService(title: str):
    driver = GraphDatabase.driver(uri, auth=(username, password))

    def getMovieByName(tx, title):
        movies = []
        res = tx.run(
            "MATCH (m:Movie {title: $title})<-[r1:ACTED_IN]-(a:Person)-[r2:ACTED_IN]->(newMovie: Movie) RETURN newMovie as movie",
            title=title,
        )
        for record in res:
            movies.append(record["movie"])
        return movies

    with driver.session() as session:
        result = session.read_transaction(getMovieByName, title)
        print("Number of Results: ", len(result))

    driver.close()
    return result

async def getMoviesByActorsService(name: str):
    driver = GraphDatabase.driver(uri, auth=(username, password))

    def getMovieByActors(tx, name):
        movies = []
        res = tx.run(
            "MATCH (p:Person {name: $name})-[r: ACTED_IN]->(m:Movie) RETURN m as movie",
            name=name,
        )
        for record in res:
            movies.append(record["movie"])
        return movies

    with driver.session() as session:
        result = session.read_transaction(getMovieByActors, name)
        print("Number of Results: ", len(result))

    driver.close()
    return result
