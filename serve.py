from livereload import Server
import subprocess


def build():
    print("Building resume...")
    subprocess.run(["python", "resume.py"])


# Build once when server starts
build()

server = Server()

# Watch files
server.watch("resume.yaml", build)
server.watch("resume_template.j2", build)
server.watch("styles.css")

# Serve output directory
server.serve(root="output")