import sys
import platform
import pkg_resources

if __name__ == "__main__":
    print("This is a test program to print information about the python environment")
    print(f"Python path: {sys.executable}")
    print(f"Python version: {platform.version()}")
    installed_packages = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
    print("installed packages:")
    for pkg in installed_packages:
        print(f"{pkg}")
        
