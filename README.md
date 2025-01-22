# Space Shooter Game

A classic arcade-style space shooter game built with Pygame. Take control of your spaceship, shoot down enemies, and rack up points while avoiding collisions.

---

## Features
- **Player Movement**: Control the spaceship using arrow keys.
- **Shooting Mechanic**: Fire bullets to destroy enemies with the `SPACE` key.
- **Enemies**: Randomly spawning enemy ships with continuous downward movement.
- **Collision Detection**: Destroy enemies with bullets or lose the game if an enemy collides with the player.
- **Game Over Screen**: Restart the game anytime by pressing the `R` key.
- **Dynamic Background**: A visually appealing background to enhance gameplay.

---

## Requirements
- Python 3.7 or above
- Pygame library

Install Pygame by running:
```bash
pip install pygame
```

---

## How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/urtype-affaan782/space-shooter-game.git
   cd space-shooter-game
   ```
2. Ensure the following image files are present in the same directory:
   - `player.jpg`: The player’s spaceship.
   - `enemy.jpg`: Enemy ships.
   - `bullet.jpg`: Bullets fired by the player.
   - `background.jpg`: Game background.

3. Run the game:
   ```bash
   python space_shooter.py
   ```

4. **Game Controls**:
   - `LEFT/RIGHT Arrow Keys`: Move the player left or right.
   - `SPACE`: Fire bullets.
   - `R`: Restart the game after game over.

---

## Game Structure
### File Structure
- `space_shooter.py`: The main game script.
- `player.jpg`, `enemy.jpg`, `bullet.jpg`, `background.jpg`: Required assets for the game.

### Code Breakdown
1. **Player**: Controlled by the user, moves horizontally and shoots bullets.
2. **Enemy**: Randomly spawns at the top and moves downwards.
3. **Bullet**: Fired by the player to destroy enemies.
4. **Collision Logic**: Detects bullet-enemy and player-enemy collisions.

---

## Future Enhancements
- Add sound effects and background music.
- Introduce power-ups (e.g., shields, rapid fire).
- Implement difficulty levels.
- Add a leaderboard to track high scores.
- Include multiple enemy types with varied behaviors.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## Contact
- **Name**: Affaan
- **GitHub**: [urtype-affaan782](https://github.com/urtype-affaan782)

Enjoy the game and have fun blasting those enemies! 🚀

