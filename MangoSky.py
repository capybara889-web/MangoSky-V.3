# MangoSky.py
import os
import time

# 🎨 Colores ANSI
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# 🍩 Animación
donut_frames = ["-", "\\", "|", "/"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""
{YELLOW}{BOLD}✨ MangoSky – Custom Roblox Skies ✨{RESET}
{CYAN}🌌 Developed by MangoV2 🌌{RESET}

{MAGENTA}🎨 Custom Roblox Skyboxes Made Easy 🎨
{BLUE}⚡ Enhanced Menu with Colors & Emojis ⚡{RESET}
""")

def menu():
    clear()
    banner()
    print(f"{YELLOW}{'★' * 60}{RESET}\n")
    print(f"{BLUE}{BOLD}[ 🎮 MAIN MENU 🎮 ]{RESET}\n")
    print(f"{GREEN}1.{RESET} ☁️ Apply a Custom Skybox")
    print(f"{BLUE}2.{RESET} 🌅 Apply Default Skybox")
    print(f"{RED}0.{RESET} 🚪 Exit\n")
    print(f"{CYAN}ℹ️  All files are stored in: %localappdata%\\MangoSky{RESET}\n")
    choice = input(f"{YELLOW}✨ Select an option: {RESET}")
    return choice.strip()

def downloading_effect(task_name, seconds=20):
    clear()
    print(f"\n{CYAN}{task_name}...{RESET}\n")
    steps = seconds * 5
    for i in range(steps + 1):
        pct = int((i / steps) * 100)
        frame = donut_frames[i % len(donut_frames)]
        bar = "[" + "#" * (pct // 5) + "-" * (20 - (pct // 5)) + "]"
        print(f"{YELLOW}Downloading {frame} {bar} {pct:3d}%{RESET}", end="\r")
        time.sleep(0.2)
    print(f"\n\n{GREEN}✅ Done! Sky Successfully Applied!{RESET}")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        choice = menu()
        if choice == "1":
            downloading_effect("☁️ Applying Custom Skybox", seconds=20)
        elif choice == "2":
            downloading_effect("🌅 Restoring Default Skybox", seconds=20)
        elif choice == "0":
            clear()
            print(f"{RED}🚪 Exiting MangoSky... Goodbye!{RESET}")
            time.sleep(1)
            break
        else:
            print(f"{RED}❌ Invalid option! Try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
