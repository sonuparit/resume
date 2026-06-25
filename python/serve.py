from livereload import Server
import subprocess


def build():
    print("Building resume...")
    subprocess.run(["python", "resume.py"])


# Build once when server starts
build()

server = Server()

# Watch files
server.watch("../data/resume.yaml", build)
server.watch("../data/template.j2", build)
server.watch("../data/styles.css")

# Serve output directory
server.serve(root="../")