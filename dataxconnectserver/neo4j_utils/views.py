from django.shortcuts import render
from neo4j import GraphDatabase


from django.http import HttpResponse


def index(request):
    uri = "neo4j+s://9bb10c14.databases.neo4j.io"  # Replace with your Neo4j database URI
    username = "neo4j"             # Replace with your Neo4j username
    password = "7TN4nQroYBrRg7CGgRznDDZEt7mGkJCK17cCOY3tXOE"          # Replace with your Neo4j password
    
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        with driver.session() as session:
            result = session.run("RETURN 1 AS result")
            record = result.single()
            if record["result"] == 1:
                print("Connection to Neo4j successful")
                print(record)
                return HttpResponse(f"<h1>Hello, world. You're at the neo4j utils index <h1>")
            else:
                print("Connection to Neo4j failed")
            
        driver.close()
        
    except Exception as e:
        print("Error connecting to Neo4j:", e)
    
