import time

def loading_gui():
    """
    Displays a loading GUI with a spinning cursor.
    """
    print("\nLoading", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(2)
    print("\n\nLoading complete!\n\n")

if __name__ == "__main__":
    loading_gui()