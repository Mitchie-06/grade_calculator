

def heal(player_hp, max_hp):  # Function that heals the player
    # Add 30 HP but do not go above max_hp (100)
    player_hp = min(player_hp + 40, max_hp)

    # Print the updated HP after healing
    print(f"Healed! Current HP: {player_hp}")

heal(50, 200)  # Call the heal function to run it

player_hp = 100  # Player starts with 100 HP
monster_hp = 80  # Monster starts with 80 HP (not used yet, but for future expansion)

def monster_attack(player_hp, damage):
    # Function where the monster attacks the player

    player_hp -= damage  # Subtract damage from player HP

    player_hp = max(player_hp, 0)  # Make sure HP does not go below 0

    print(f"Monster attacks! Player takes {damage} damage.")  # Show attack message
    print(f"Player HP: {player_hp}")  # Show updated HP

    return player_hp  # Return updated HP back to main code


player_hp = monster_attack(player_hp, 15)  # Monster deals 15 damage to player

