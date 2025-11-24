import docker
from docker.errors import DockerException


def get_running_containers():
    """Get all currently running Docker containers using official docker library"""
    try:
        # Connect to Docker daemon
        client = docker.from_env()

        # Get all running containers
        containers = client.containers.list()

        return containers, client

    except DockerException as e:
        print(f"Error connecting to Docker: {e}")
        return [], None


def main():
    print("Searching for running Docker containers...\n")

    containers, client = get_running_containers()

    if not containers:
        print("No running containers found.")
        return

    print(f"Found {len(containers)} running container(s):\n")

    for container in containers:
        # Get container details
        print(f"Container ID: {container.id[:12]}")
        print(f"Short ID: {container.short_id}")
        print(f"Name: {container.name}")
        print(
            f"Image: {container.image.tags[0] if container.image.tags else container.image.id[:12]}"
        )
        print(f"Status: {container.status}")
        print(f"Labels: {container.labels}")

        # Port mappings
        if container.ports:
            print(f"Ports: {container.ports}")
        else:
            print("Ports: None")

        # Network info
        print(
            f"Networks: {list(container.attrs['NetworkSettings']['Networks'].keys())}"
        )

        print("-" * 60)


if __name__ == "__main__":
    main()
