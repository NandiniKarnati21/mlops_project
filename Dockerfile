import typer

app = typer.Typer()

@app.command()
def main():
    print("Hello from my DTU MLOps project!")

if __name__ == "__main__":
    app()
