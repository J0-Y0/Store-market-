import os
import subprocess
import win32service
import win32serviceutil
import django
import logging
import win32event
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DjangoService(win32serviceutil.ServiceFramework):
    _svc_name_ = "DjangoPipenvService"
    _svc_display_name_ = "Django Pipenv Service"
    _svc_description_ = (
        "This service runs a Django application with Pipenv and Waitress."
    )

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True
        self.process = None

        # Set Django environment
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
        django.setup()

        # Configure logging
        logging.basicConfig(
            filename="django_service.log",
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger("django_service")
        self.logger.info("Service initialized.")

    def SvcStop(self):
        """Handle service stop event."""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.logger.info("Service is stopping...")
        if self.process:
            self.process.terminate()
            self.process.wait()  # Ensure process stops completely
        win32event.SetEvent(self.stop_event)
        self.running = False
        self.logger.info("Service stopped.")

    def SvcDoRun(self):
        """Handle service run event."""
        self.logger.info("Service is starting...")
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()

    def main(self):
        """Main logic of the service."""
        project_dir = os.getenv("PROJECT_DIR")  # Use .env variable

        if not project_dir:
            self.logger.error("PROJECT_DIR environment variable is not set.")
            return

        command = [
            "pipenv",
            "run",
            "waitress-serve",
            "--port=8000",
            "core.wsgi:application",
        ]

        self.logger.info(f"Starting Waitress server from: {project_dir}")
        try:
            self.process = subprocess.Popen(command, cwd=project_dir)
        except FileNotFoundError as e:
            self.logger.error(f"Failed to start server: {e}")
            return

        # Monitor the process
        while self.running:
            if self.process.poll() is not None:
                self.logger.error("Waitress server has stopped unexpectedly.")
                break
            time.sleep(1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        # Run the main logic directly without using the service infrastructure
        print("Running in debug mode...")
        service = DjangoService(["dummy_arg"])  # Dummy arg for initialization
        try:
            service.main()
        except KeyboardInterrupt:
            print("Service interrupted.")
            if service.process:
                service.process.terminate()
                service.process.wait()
    else:
        # Service management through command line
        win32serviceutil.HandleCommandLine(DjangoService)
