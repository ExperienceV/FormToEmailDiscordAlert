from fastapi import FastAPI, APIRouter
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.routers import send
from dotenv import load_dotenv

# Initialize FastAPI application
app = FastAPI()

# Load environment variables from the specified .env file
load_dotenv('./.env')

class FastServer:
    """
    A class to set up a FastAPI server with middleware, routers, and static file handling.

    Attributes:
        routers (list[APIRouter]): List of API routers to include in the application.
        paths (list[dict]): List of dictionaries specifying static file paths.
    """

    def __init__(self, routers: list[APIRouter], paths: list[dict]) -> None:
        """
        Initializes the server with middleware, routers, and static paths.

        Args:
            routers (list[APIRouter]): List of API routers to include.
            paths (list[dict]): List of dictionaries for static file configurations.
        """
        self._configure_middleware()
        self._register_routers(routers)
        self._configure_static_files(paths)

    def _configure_middleware(self) -> None:
        """
        Configures middleware for the FastAPI application. Adds CORS middleware
        to allow cross-origin requests.
        """
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allow all origins
            allow_credentials=True,  # Allow cookies and credentials
            allow_methods=["*"],  # Allow all HTTP methods
            allow_headers=["*"],  # Allow all headers
        )

    def _configure_static_files(self, paths_data: list[dict]) -> None:
        """
        Configures static file handling by mounting directories to specific routes.

        Args:
            paths_data (list[dict]): List of dictionaries specifying the static path name and directory.

        Raises:
            RuntimeError: If the specified static directory does not exist.
        """
        for path_config in paths_data:
            # Extract route name and directory path from the dictionary
            route_name, directory_path = list(path_config.items())[0]

            static_dir = Path(__file__).resolve().parent / directory_path
            if not static_dir.exists():
                raise RuntimeError(f"Directory '{static_dir}' does not exist")

            # Mount the static directory to the specified route
            app.mount(f"/{route_name}", StaticFiles(directory=static_dir), name=route_name)

    def _register_routers(self, routers: list[APIRouter]) -> None:
        """
        Includes API routers in the FastAPI application.

        Args:
            routers (list[APIRouter]): List of API routers to include.
        """
        for router in routers:
            app.include_router(router)

# Define the list of API routers to include in the application
routers_list = [
    send.app  # Example router imported from 'routers'
]

# Define the list of static paths to mount
paths_list = [
    {
        'routers': './routers'  # Static directory for routers
    }
]

# Initialize the FastServer with the defined routers and static paths
server = FastServer(
    routers=routers_list,
    paths=paths_list
)
