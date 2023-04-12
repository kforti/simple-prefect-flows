from prefect import flow, task

@task
def print_hello(name):
    print(f"Hello {name}!")

@flow(name="Hello Flow")
def hello_world(name="world"):
    print_hello(name)


@task
def print_hello_again(name):
    print(f"Hello {name}!")

@flow(name="Hello Again Flow")
def hello_world_again(name="world"):
    print_hello(name)
    print_hello_again(name)