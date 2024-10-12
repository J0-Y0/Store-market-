import os
import subprocess

# from pywin32 import servicemanager

import win32service
import win32serviceutil
import django
import logging
import win32event
import time
from dotenv import load_dotenv

load_dotenv()


class DjangoService(win32serviceutil.ServiceFramework):
    _svc_name_ = "DjangoPipenvService"
    _svc_display_name_ = "Django Pipenv Service"
    _svc_description_ = (
        "This service runs a Django application with Pipenv and Waitress."
    )

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32service.CreateEvent(None, 0, 0, None)
        self.running = True
        self.process = None

        # Set up Django environment
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "core.settings.dev"
        )  # Update this
        django.setup()

        # Get the service logger
        self.logger = logging.getLogger("django_service")
        self.logger.info("Service initialized.")

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.logger.info("Service is stopping...")
        if self.process:
            self.process.terminate()
        win32event.SetEvent(self.stop_event)
        self.running = False
        self.logger.info("Service stopped.")

    def SvcDoRun(self):
        self.logger.info("Service is starting...")
        self.main()

    def main(self):
        # Set your project directory where Pipfile is located
        project_dir = os.getenv("PROJECT_DIR")  # Update this

        self.logger.info("Starting Waitress server...")
        command = [
            "pipenv",
            "run",
            "waitress-serve",
            "--port=8000",
            "core.wsgi:application",
        ]
        self.process = subprocess.Popen(command, cwd=project_dir)

        while self.running:
            if self.process.poll() is not None:
                self.logger.error("Waitress server has stopped unexpectedly.")
                break  # Process has ended
            time.sleep(1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        # Directly call the main method for debugging
        service = DjangoService(None)
        service.main()  # Call the main method directly
    else:
        win32serviceutil.HandleCommandLine(DjangoService)
