import termcolor
from utils.banner_utils import banner as generate_banner

def main() -> None:
    """Orchestrates & Manage depends of cost export workflow."""
    
    # Banner
    banner_format, copyright_notice = generate_banner()
    print(f"\n\n {termcolor.colored(banner_format, color="green")}")
    print(f"{termcolor.colored(copyright_notice, color="green")}", end="\n\n")
    
    
    
if __name__ == "__main__":
    main()