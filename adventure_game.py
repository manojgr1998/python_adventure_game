# adventure_game.py
# A simple text-based adventure game where the player searches for a legendary treasure.

def get_choice(prompt, options):
    """
    Helper function to get a valid choice from the player.
    `options` should be a dict like {"1": "forest", "2": "cave"}.
    """
    while True:
        print(prompt)
        for key, value in options.items():
            print(f"{key}. {value.capitalize()}")
        choice = input("Enter your choice: ").strip().lower()

        # Accept both number and word (e.g., "1" or "forest")
        if choice in options:
            return options[choice]
        # Also allow matching by value (like "forest", "cave")
        for key, value in options.items():
            if choice == value.lower():
                return value
        print("Invalid choice. Please try again.\n")


def forest_path(player_name):
    """
    Describes the forest scenario.
    The player can follow a river or climb a tree.
    One path eventually leads toward the treasure (via the cave),
    and the other leads to a losing outcome.
    """
    print("\n--- The Dark Forest ---")
    print(f"{player_name}, you step into a dense, dark forest. The air is cool and silent.")
    print("After walking for a while, you reach a clearing where you see:")
    print("- A gentle river flowing to your left.")
    print("- A tall, ancient tree with strong branches.")

    options = {
        "1": "follow the river",
        "2": "climb the tree"
    }

    choice = get_choice("What do you want to do?", options)

    if choice == "follow the river":
        print("\nYou decide to follow the river.")
        print("The water sparkles as it winds through the forest.")
        print("After some time, the river disappears into the entrance of a mysterious cave.")
        print("You carefully follow the path and arrive at the cave entrance.")
        # Move to cave scenario from the forest
        return cave_path(player_name, entered_from_forest=True)

    else:  # "climb the tree"
        print("\nYou decide to climb the ancient tree to get a better view.")
        print("You climb higher and higher. The view is incredible, but the branches are slippery.")
        print("Suddenly, a branch snaps!")
        print("You fall to the ground and are injured. You can no longer continue your journey.")
        print("\n*** You lost the adventure. ***")
        return "lose"


def cave_path(player_name, entered_from_forest=False):
    """
    Describes the cave scenario.
    The player can light a torch or proceed in the dark.
    Lighting a torch leads to the treasure, proceeding in the dark leads to a loss.
    `entered_from_forest` indicates whether the player came here via the forest path.
    """
    print("\n--- The Mysterious Cave ---")
    if entered_from_forest:
        print("Following the river has led you to a hidden cave entrance.")
    else:
        print(f"{player_name}, you stand before a massive cave carved into the side of a mountain.")

    print("The cave looks ancient and mysterious. It is pitch dark inside.")
    print("You find an old unlit torch lying near the entrance.")

    options = {
        "1": "light the torch",
        "2": "proceed in the dark"
    }

    choice = get_choice("How do you want to continue?", options)

    if choice == "light the torch":
        print("\nYou light the torch. The cave lights up with a warm glow.")
        print("You carefully walk deeper, avoiding sharp rocks and hidden pits.")
        print("Soon, you see something shining at the end of the tunnel.")
        print("It's a large chest covered in ancient symbols!")
        print("You open the chest and find the legendary treasure you were searching for!")
        print("\n*** Congratulations, you found the treasure and WON the adventure! ***")
        return "win"
    else:  # "proceed in the dark"
        print("\nYou decide to proceed without lighting the torch.")
        print("You slowly step into the darkness, feeling your way along the walls.")
        print("Suddenly, the ground disappears beneath your feet!")
        print("You fall into a deep pit and cannot climb out.")
        print("\n*** You lost the adventure in the depths of the cave. ***")
        return "lose"


def start_game():
    """
    Starts the adventure game:
    - Introduces the quest
    - Asks for the player's name
    - Provides the initial choice (forest or cave)
    Returns "win" or "lose" depending on the outcome.
    """
    print("\n=====================================")
    print("  Welcome to the Python Adventure!   ")
    print("=====================================\n")

    player_name = input("Brave explorer, what is your name? ").strip()
    if not player_name:
        player_name = "Explorer"

    print(f"\nWelcome, {player_name}!")
    print("Your quest is to find the legendary treasure hidden in an ancient land.")
    print("You stand at a crossroads with two paths ahead of you:")
    print("- One path leads into a dark, dense forest.")
    print("- The other leads to a mysterious cave in the mountains.\n")

    options = {
        "1": "forest",
        "2": "cave"
    }

    choice = get_choice("Where would you like to go first?", options)

    if choice == "forest":
        outcome = forest_path(player_name)
    else:  # "cave"
        outcome = cave_path(player_name, entered_from_forest=False)

    return outcome


def main():
    """
    Main loop to run the adventure game.
    The game restarts if the player chooses to play again.
    """
    while True:
        outcome = start_game()

        # Outcome summary
        if outcome == "win":
            print("\nYou successfully completed your quest. Well done!")
        else:
            print("\nYour quest has ended, but you can always try again.")

        # Ask if the player wants to restart
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for playing the Python Adventure. Goodbye!")
            break


if __name__ == "__main__":
    # Simple statement to confirm that the setup is working (Task 1).
    print("Loading adventure game...\n")
    main()
